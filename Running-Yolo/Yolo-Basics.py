import cv2
from ultralytics import YOLO

model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("Images/3.png", show=True)
cv2.waitKey(0)