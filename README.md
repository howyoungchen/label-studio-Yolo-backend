# Label-Studio-Yolo-Backend

This project, named Label-Studio-Yolo-Backend, is an open-source project aimed at providing an assisted labeling backend for [Label Studio](https://labelstud.io/) using `label-studio-ml`. The project consists of a single Python file and leverages the YOLOv5 model, which has been trained using [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5). For more information on how to set up and integrate a machine learning backend with Label Studio, please refer to the [Label Studio ML Backend](https://github.com/heartexlabs/label-studio-ml-backend) repository.

This project was developed with the assistance of the GPT-4 language model, which also helped in the creation of this README file.

## Project Introduction

Label-Studio-Yolo-Backend is a project that provides an efficient way to integrate a YOLOv5 object detection model with Label Studio. This enables users to take advantage of the pre-trained YOLOv5 model to improve their annotation workflow and reduce the time required for manual annotation.

## Features

- Easy integration with Label Studio
- Leverages the powerful YOLOv5 object detection model
- Assisted annotation to speed up the labeling process
- Single Python file for easy setup and deployment

## Dependencies

- [Label Studio](https://labelstud.io/)
- [Label Studio ML Backend](https://github.com/heartexlabs/label-studio-ml-backend)
- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)

## Usage

1. Set up and install Label Studio following the instructions in their [documentation](https://labelstud.io/guide/install.html).
2. Install the Label Studio ML Backend by following the steps in their [repository](https://github.com/heartexlabs/label-studio-ml-backend).
3. Clone the Ultralytics YOLOv5 repository and follow the instructions to set it up.
4. Clone this repository and copy the Python file to the appropriate directory in your Label Studio ML Backend setup.
5. Configure your Label Studio project to use the Label-Studio-Yolo-Backend.

**Important Note**: In some cases, you might need to modify the `get_local_path` function in the `model.py` file of the `label-studio-ml` library. Please refer to this [issue comment](https://github.com/heartexlabs/label-studio-ml-backend/issues/143#issuecomment-1495685625) for more details and a potential solution.

## Acknowledgements

This project was developed with the help of the GPT-4 language model, which also assisted in the creation of this README file.

## License

Label-Studio-Yolo-Backend is released under the [MIT License](https://opensource.org/licenses/MIT).
