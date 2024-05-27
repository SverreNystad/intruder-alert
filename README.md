# Intruder Alert

<div align="center">
    <img src="docs/images/logo.png" alt="Logo" width="300" height="300">
</div>


Intruder Alert is a face detection system that utilizes OpenCV's classifiers to identify and record faces in real-time video. This system captures images of detected faces, logging the time of detection, which can be used for security monitoring and intruder detection purposes.

## Features
- Real-time face detection from webcam feed.
- Timestamped logging of detected faces.
- Headless mode for running on servers without a display (or on the laptop during lunch meetings or so).
- Saving detections as images for further analysis or evidence.

## Prerequisites
Ensure Python 3.9 or newer is installed on your machine. [Download Python](https://www.python.org/downloads/)

Then, install the required packages by running the following command in the project directory:
```bash
pip install -r requirements.txt
```

## Usage
To start the face detection, navigate to the project directory and run:

```bash
python main.py
```

The system will activate the webcam and begin scanning for faces. Detected faces will be displayed in real-time, and images will be saved in the detections/ directory under the project folder.

Press `q` while focused on the video window to quit the application.


### Headless Mode
To run the system in headless mode, use the `--headless` flag:
```bash
python main.py --headless
```