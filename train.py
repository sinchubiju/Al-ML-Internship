from ultralytics import YOLO

model = YOLO("yolov8n.pt")

print("YOLO Model Loaded Successfully")

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data=r"C:\Users\dell\downloads\dataset\data.yaml",
    epochs=10
)



model = YOLO(
  
    "runs/detect/train-12/weights/best.pt"
)


results = model(r"C:\Users\dell\Downloads\helmet_test.jpg")

results[0].show()