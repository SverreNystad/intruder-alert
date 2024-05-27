import argparse
from datetime import datetime
import cv2

from src.roi_detection import detect_rois, draw_on_image

IMAGE_PATH = "detections/"


def detect_and_save_faces(headless: bool = False):

    video_capture = cv2.VideoCapture(0)
    classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    last_timestamp = None

    while True:
        # read frames from the video
        result, video_frame = video_capture.read()

        # If the there are no frames to read, break the loop
        if result is False:
            break

        # detect regions of interest in the frame
        rois = detect_rois(video_frame, classifier)
        if len(rois) > 0:
            timestamp = datetime.now()
            print(f"Regions of interest detected: {rois} at {timestamp.strftime("%Y-%m-%d %H:%M:%S")}.")
            draw_on_image(video_frame, rois)

            # Save the frame as an image
            if last_timestamp is None:
                last_timestamp = timestamp

            else:
                time_diff = timestamp - last_timestamp
                if time_diff.microseconds >= 1:
                    cv2.imwrite(f"{IMAGE_PATH}face_detected_{timestamp.strftime("%Y-%m-%d %H:%M:%S")}.png", video_frame)
                    last_timestamp = timestamp
            
        # If the application is running in headless mode, skip displaying the frame
        if headless:
            continue

        # display the processed frame in a window
        cv2.imshow("Intruder Alert", video_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    # release the video capture object and close the windows
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--headless", action="store_true", help="Run the application in headless mode.")
    args = parser.parse_args()
    detect_and_save_faces(args.headless)
    
