import os
os.system("yolo detect train model=yolov8s.pt data=dataset/data.yaml epochs=50 imgsz=640 batch=8")