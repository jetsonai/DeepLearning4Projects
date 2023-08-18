#jetson tx2 onboard camera gstreamer string
#gst_str = ("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)NV12, framerate=(fraction)60/1 ! nvvidconv flip-method=0 ! video/x-raw, width=(int)1280, height=(int)720, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
#gst_str = ("rtspsrc location=rtsp://192.168.0.69:9000/stream latency=0 ! rtph264depay ! h264parse ! omxh264dec ! videoconvert ! appsink")
gst_str = ("v4l2src device=/dev/video0 ! video/x-raw, width=640, height=480, format=(string)YUY2,framerate=30/1 ! videoconvert ! video/x-raw,width=640,height=480,format=BGR ! appsink")

import cv2
import numpy as np
def imageProcessing(input):
    output = np.copy(input)
    output = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    return output

def videoProcess(openpath, savepath = None):
    cap = cv2.VideoCapture(openpath)
    if cap.isOpened():
        print("Video Opened")
    else:
        print("Video Not Opened")
        print("Program Abort")
        exit()
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = None

    cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            # Our operations on the frame come here
            #output = imageProcessing(frame)

            # Display the resulting frame
            cv2.imshow("frame", frame)
        else:
            break
        # waitKey(int(1000.0/fps)) for matching fps of video
        if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()

    cv2.destroyAllWindows()
    return
   
if __name__=="__main__":
    videoProcess(gst_str)
