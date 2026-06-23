from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
     data=r"C:\Users\dell\Downloads\helmet dataset\data.yaml",
    epochs=20
)

import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO(r"runs\detect\train-19\weights\best.pt")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    # Detect helmets
    results = model(frame)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    cv2.imshow("Helmet Detection", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()