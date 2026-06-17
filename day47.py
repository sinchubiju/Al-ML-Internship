from ultralytics import YOLO

model = YOLO("yolov8n.pt")

print("YOLO Model Loaded Successfully")

import cv2
from ultralytics import YOLO

video = cv2.VideoCapture(r"C:\Users\dell\Downloads\dog.mp4")

while True:
    success, frame = video.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Video Detection", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()


camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Live Detection", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()