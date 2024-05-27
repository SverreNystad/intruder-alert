# Intruder Alert

Intruder Alert is a Python-based face detection system that utilizes OpenCV's classifiers to identify and record faces in real-time video. This system captures images of detected faces, logging the time of detection, which can be used for security monitoring and intruder detection purposes.

## Features
- Real-time face detection from webcam feed.
- Timestamped logging of detected faces.
- Headless mode for running on servers without a display (or on the laptop during lunch meetings or so).
- Saving detections as images for further analysis or evidence.

## Prerequisites
Before you can run the Intruder Alert system, ensure you have the following installed:
- Python 3.x

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