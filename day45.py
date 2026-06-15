from ultralytics import YOLO

model = YOLO("yolov8n.pt")
print("Model Loaded Successfully")

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("C:/Users/dell/Downloads/dog.jpg", save=True)

results[0].show()

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model(
   [
    r"C:\Users\dell\Downloads\image1.jpg",
    r"C:\Users\dell\Downloads\image2.jpg",
    r"C:\Users\dell\Downloads\dog.jpg"
], save=True)
    
