import cv2
from ultralytics import YOLO
import numpy as np
model = YOLO('Yolo-Weights/yolov8l.pt')
results = model("Source/1.jpg", show= True)
cv2.waitKey(0)