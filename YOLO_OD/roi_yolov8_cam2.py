import ultralytics
import cv2
from PIL import Image
import numpy as np


ultralytics.checks()

from ultralytics import YOLO

model = YOLO('yolov8n.pt')

#results = model(source = 0, show=True, conf=0.3, save=True)

#video_source = "personbottle.mp4"

class_colors = {
    'person': (10,10,240),
    'mouse': (10,255,10),
    'cup': (240,10,10),
}
def_color = (255,255,255)

video_source = 0

cap = cv2.VideoCapture(video_source)
if cap.isOpened():
    print("Video Opened")
else:
    print("Video Not Opened")
    print("Program Abort")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('width:{}'.format(width))
print('height:{}'.format(height))

# 1
# Draw rectangle width as -100 from left and right
# and height as -50 from top and bottom
# color : yellow, thickness 3
# 2
# crop frame width as -100 from left and right
# crop frame height as -50 from top and bottom
xd = 80
yd = 20

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        #cv2.imshow("RAW", frame)
        ROIcolor = (0,255,255)
        cv2.rectangle(frame, (xd,yd), (width-xd, height-yd), ROIcolor, thickness=3)
        roi_xmin = xd
        roi_ymin = yd
        roi_xmax = width-xd
        roi_ymax = height-yd        
        crop_frame = frame[yd:height-yd, xd:width-xd]
        #crop_frame = frame[xd:width-xd, yd:height-yd]
                    
        results = model(crop_frame)
        for result in results:
            for box in result.boxes:
                clsID = int(box.cls)
                clsName = model.names[clsID]
                print(box.xyxy[0])
                xmin, ymin, xmax, ymax = map(int, box.xyxy[0])
                
                #print(clsName)
                if(clsName == 'person' or clsName == 'mouse' or clsName == 'cup'):
                    print(clsName)
                    color = class_colors.get(clsName, def_color)
                    cv2.rectangle(crop_frame, (xmin,ymin), (xmax, ymax), color, thickness=3)
                    print("xmin:{}, ymin:{}, xmax:{}, ymax:{}".format(xmin, ymin, xmax, ymax))
                    
                    confidence = float(box.conf)
                    labeltext = f'{clsName}{confidence:.2f}'
                    textsize, _ = cv2.getTextSize(labeltext, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                    text_y = max(ymin, textsize[1]+10)
                    cv2.rectangle(crop_frame, (xmin, text_y-textsize[1]-10), (xmin+textsize[0] , text_y), color, -1)
                    cv2.putText(crop_frame, labeltext, (xmin, text_y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,def_color, 1)                    
                    
            
        cv2.imshow("YOLOv8", crop_frame)
        
    else:
        break
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


