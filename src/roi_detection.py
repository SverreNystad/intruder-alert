import cv2
from cv2.typing import MatLike, Rect
from cv2 import CascadeClassifier
from datetime import datetime

IMAGE_PATH = "detections/"


def detect_and_save_faces(headless: bool = False):
    """
    Detect faces in a video stream from the webcam and save the frames containing the faces.
    """
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
            draw_crosshair_over_rois_on_image(video_frame, rois)

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


def detect_rois_in_video(
    video_path: str, classifier: CascadeClassifier
) -> list[MatLike]:
    """
    Detect regions of interest in a video using the specified classifier.
    Returns a list of frames containing the detected regions of interest.
    """
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error opening video stream or file")
        return

    frames_containing_rois = []

    # Read until video is completed
    while True:
        ret, frame = video.read()
        frame_count = video.get(cv2.CAP_PROP_POS_FRAMES)
        if not ret:
            # Video has ended
            break

        regions_of_interest = detect_rois(frame, classifier)
        draw_crosshair_over_rois_on_image(frame, regions_of_interest)
        frames_containing_rois.append(frame)

        cv2.imwrite(f"{IMAGE_PATH}frame_{frame_count}.png", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

    return frames_containing_rois


def detect_rois(image: MatLike, classifier: CascadeClassifier) -> list[cv2.typing.Rect]:
    """
    Detect regions of interest (ROIs) in an image using the specified classifier.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    regions_of_interest: list[Rect] = classifier.detectMultiScale(
        gray_image, 1.1, 5, minSize=(40, 40)
    )
    return regions_of_interest


def draw_crosshair_over_rois_on_image(image: MatLike, regions_of_interest: list[Rect]) -> None:
    """
    Draw crosshairs on the center of regions of interest on the image.
    """

    CROSSHAIR_SIZE: int = 100
    THICKNESS: int = 2
    # Color is in BGR format
    COLOR = (0, 0, 255)
    for x, y, w, h in regions_of_interest:
        center = (x + w // 2, y + h // 2)
        # crosshair
        image = cv2.line(
            image,
            (center[0], center[1] - CROSSHAIR_SIZE),
            (center[0], center[1] + CROSSHAIR_SIZE),
            COLOR,
            THICKNESS,
        )
        image = cv2.line(
            image,
            (center[0] - CROSSHAIR_SIZE, center[1]),
            (center[0] + CROSSHAIR_SIZE, center[1]),
            COLOR,
            THICKNESS,
        )
        image = cv2.circle(image, center, CROSSHAIR_SIZE, COLOR, THICKNESS)

def draw_bounding_boxes_over_rois_on_image(image: MatLike, regions_of_interest: list[Rect]) -> None:
    """
    Draw bounding boxes around regions of interest on the image.
    """
    COLOR = (0, 0, 255)
    THICKNESS = 2
    for x, y, w, h in regions_of_interest:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), COLOR, THICKNESS)

