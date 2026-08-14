from ultralytics import YOLO

model = YOLO('yolov8n.pt')

result = model('picture\endoscope_20260807_172937_334.jpg',save = True)

result[0].show()