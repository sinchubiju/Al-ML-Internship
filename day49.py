from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data=r"C:\Users\dell\Downloads\dataset\data.yaml",
    epochs=10,
    imgsz=640
)