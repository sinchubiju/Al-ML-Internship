from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Run detection
results = model("C:/Users/dell/Downloads/dog.jpg")


# Show result image
results[0].show()


for result in results:
    for box in result.boxes:
        class_id = int(box.cls)
        class_name = result.names[class_id]
        confidence = float(box.conf)

        print("Object:", class_name)
        print("Confidence:", confidence)
        print("----------------")


        results = model.predict("C:/Users/dell/Downloads/dog.jpg", conf=0.3)

        results = model.predict("C:/Users/dell/Downloads/dog.jpg", conf=0.5)
        results = model.predict("C:/Users/dell/Downloads/dog.jpg", conf=0.8)

       

results = model("C:/Users/dell/Downloads/dog.jpg")

for result in results:
    print(result.boxes)



for result in results:
    for box in result.boxes:

        class_id = int(box.cls)
        class_name = result.names[class_id]

        confidence = float(box.conf)

        coordinates = box.xyxy.tolist()

        print("Class:", class_name)
        print("Confidence:", confidence)
        print("Bounding Box:", coordinates)
        print("----------------------")