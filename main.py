import argparse

from src.roi_detection import detect_and_save_faces


if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--headless", action="store_true", help="Run the application in headless mode."
    )
    args = parser.parse_args()

    # Run the face detection pipeline
    detect_and_save_faces(args.headless)
