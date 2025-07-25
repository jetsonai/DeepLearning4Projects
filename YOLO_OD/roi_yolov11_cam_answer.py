import ultralytics
import cv2
from PIL import Image
import numpy as np

gst_usb_str = ("v4l2src device=/dev/video0 ! video/x-raw, width=640, height=480, format=(string)YUY2,framerate=30/1 ! videoconvert ! video/x-raw,width=640,height=480,format=BGR ! appsink")

ultralytics.checks()

from ultralytics import YOLO

model = YOLO('yolo11n.pt')
#model = YOLO("yolo11n.engine")

class_colors = {
    'person': (10,10,240),
    'mouse': (10,255,10),
    'cup': (240,10,10),
}
def_color = (255,255,255)

#video_source = 0
video_source = gst_usb_str

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
yd = 40

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
        guestcount = 0
        for result in results:
            for box in result.boxes:
                clsID = int(box.cls)
                clsName = model.names[clsID]
                print(box.xyxy[0])
                xmin, ymin, xmax, ymax = map(int, box.xyxy[0])
                
                xmin = xmin + xd
                ymin = ymin + yd
                xmax = xmax + xd
                ymax = ymax + yd
                print(clsName)

                #if(clsName == 'person' or clsName == 'mouse' or clsName == 'cup'):
                if(clsName == 'person'):
                    print(clsName)
                    color = class_colors.get(clsName, def_color)
                    cv2.rectangle(frame, (xmin,ymin), (xmax, ymax), color, thickness=3)
                    print("xmin:{}, ymin:{}, xmax:{}, ymax:{}".format(xmin, ymin, xmax, ymax))
                    
                    confidence = float(box.conf)
                    labeltext = f'{clsName}{confidence:.2f}'
                    textsize, _ = cv2.getTextSize(labeltext, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                    text_y = max(ymin, textsize[1]+10)
                    cv2.rectangle(frame, (xmin, text_y-textsize[1]-10), (xmin+textsize[0] , text_y), color, -1)
                    cv2.putText(frame, labeltext, (xmin, text_y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,def_color, 1) 
                    guestcount = guestcount+1

        #infotext = "customer count : {}".format(guestcount)
        
        infotext = "guest count : {}".format(guestcount)
        cv2.putText(frame, infotext, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,0,250), 2)
        cv2.imshow("YOLOv11", frame)
        
    else:
        break
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


