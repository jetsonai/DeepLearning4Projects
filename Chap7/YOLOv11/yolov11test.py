import ultralytics
import cv2
from PIL import Image
import numpy as np


ultralytics.checks()

from ultralytics import YOLO

model = YOLO('yolo11n.pt')

#results = model(source = 0, show=True, conf=0.3, save=True)

video_source = "cctv.mp4"
#video_source = 0

cap = cv2.VideoCapture(video_source)
if cap.isOpened():
    print("Video Opened")
else:
    print("Video Not Opened")
    print("Program Abort")
    exit()
#cv2.namedWindow("YOLOv8", cv2.WINDOW_GUI_EXPANDED)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        #cv2.imshow("RAW", frame)
        
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv11", annotated_frame)
        
    else:
        break
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


