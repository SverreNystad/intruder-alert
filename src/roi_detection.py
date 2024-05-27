import cv2
from cv2.typing import MatLike, Rect
from cv2 import CascadeClassifier


def detect_rois(image: MatLike, classifier: CascadeClassifier) -> list[cv2.typing.Rect]:
    """
    Detect regions of interest (ROIs) in an image using the specified classifier.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    regions_of_interest: list[Rect] = classifier.detectMultiScale(
        gray_image, 1.1, 5, minSize=(40, 40)
    )
    return regions_of_interest


def draw_on_image(image: MatLike, regions_of_interest: list[Rect]) -> None:
    """
    Draw crosshairs on the center of regions of interest on the image.
    """

    CROSSHAIR_SIZE: int = 100
    THICKNESS: int = 2
    # Color is in BGR format
    COLOR = (0, 0, 255)
    for x, y, w, h in regions_of_interest:
        # Bounding box
        # cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)

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
