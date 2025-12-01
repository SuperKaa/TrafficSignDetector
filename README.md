# TrafficSignDetector

made by me

simple and small trained model to detect traffic signs in pictures and live webcam feed
dataset created using RoboFlow and then trained using yolo

model is best.pt

supports:

- give way
- no entry
- no stop
- no u turn
- road work
- round about
- sharp turn
- speed limit
- stop sign

## How you can recreate it

- take pictures of each of your subjects from many different angles, variations and lighting
- upload all images to RoboFlow and begin drawin your boxes around each subject in each class
- once done download the dataset created
- train the dataset locally or online
- if you train the dataset locally:
  ```
  pip install ultralytics
  ```
  ```
  yolo detect train model=yolov8s.pt data=dataset/data.yaml epochs=50 imgsz=640 batch=8
  ```
