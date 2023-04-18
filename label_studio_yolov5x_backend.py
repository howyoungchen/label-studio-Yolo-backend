import os
import logging
import torch
import cv2
import requests
from label_studio_ml.model import LabelStudioMLBase
from label_studio_ml.utils import get_image_size, get_single_tag_keys
from label_studio.core.utils.io import json_load, get_data_dir
from label_studio.core.settings.base import DATA_UNDEFINED_NAME
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

yolov5_repo_dir = "/Path/To/Your/yolov5"
pretrained_model_path = "/Path/To/Your/yolov5.pt"

class YOLO_Model(LabelStudioMLBase):
    """Load a YOLOv5 model by torch-hub from local"""
    def __init__(self, yolov5_repo_dir=yolov5_repo_dir, pretrained_model_path=pretrained_model_path, train_output=None, **kwargs):
        super(YOLO_Model, self).__init__(**kwargs)
        upload_dir = os.path.join(get_data_dir(), 'media', 'upload')
        self.image_dir = upload_dir
        logger.debug(f'{self.__class__.__name__} reads image from {self.image_dir}')
        self.model = torch.hub.load(yolov5_repo_dir, "custom", path=pretrained_model_path, source="local")
        
    def _get_image_url(self, task):
        print(task)
        image_url = task['data']["image"] or task['data'].get(DATA_UNDEFINED_NAME)
        return image_url
    
    def predict(self, tasks, **kwargs):
        predictions = []
        print("tasks: ", tasks)

        for task in tasks:
            image_url = self._get_image_url(task)
            # Get image local path
            image_path = self.get_local_path(image_url, project_dir=self.image_dir)
            
            print("img_path: ", image_path)
            image = cv2.imread(image_path)
            original_height, original_width = image.shape[:2]

            results = self.model(image)
            result_list = []

        for *xyxy, conf, cls in results.xyxy[0]:
            x, y, width, height = self.convert_to_ls(*xyxy, original_width, original_height)
            result_list.append({
                'from_name': 'label',
                'to_name': 'image',
                'type': 'rectanglelabels',
                'value': {
                    'x': float(x.item()),
                    'y': float(y.item()),
                    'width': float(width.item()),
                    'height': float(height.item()),
                    'rectanglelabels': [self.model.names[int(cls)]]
                }
            })

            predictions.append({
                'result': result_list,
                'score': float(conf.item())
            })
            print("predictions: ", predictions)

        return predictions

    @staticmethod
    def convert_to_ls(x1, y1, x2, y2, original_width, original_height):
        width = x2 - x1
        height = y2 - y1
        return x1 / original_width * 100.0, y1 / original_height * 100.0, \
               width / original_width * 100.0, height / original_height * 100.0

