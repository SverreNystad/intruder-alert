import argparse
from cv2 import CascadeClassifier
from cv2.data import haarcascades

from src.roi_detection import detect_and_save_rois
from src.alerter import alert_on_configured_channels


if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--headless", action="store_true", help="Run the application in headless mode."
    )
    args = parser.parse_args()

    # Run the face detection pipeline
    classifier = CascadeClassifier(haarcascades + "haarcascade_frontalface_default.xml")
    detect_and_save_rois(classifier, args.headless)
    alert_on_configured_channels()
