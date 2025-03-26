#jetson tx2 onboard camera gstreamer string
#gst_str = ("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)NV12, framerate=(fraction)60/1 ! nvvidconv flip-method=0 ! video/x-raw, width=(int)1280, height=(int)720, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
#gst_str = ("rtspsrc location=rtsp://192.168.0.69:9000/stream latency=0 ! rtph264depay ! h264parse ! omxh264dec ! videoconvert ! appsink")
gst_str = ("v4l2src device=/dev/video0 ! video/x-raw, width=640, height=480, format=(string)YUY2,framerate=30/1 ! videoconvert ! video/x-raw,width=640,height=480,format=BGR ! appsink")

import cv2
import numpy as np

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
    #영상을 보여주기 위한 opencv 윈도우 생성
    cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)

    while cap.isOpened():
        # 이미지 프레임 읽어오기기
        ret, frame = cap.read()
        if ret:
            # 이미지 프로세싱을 진행한 후 그 결과 이미지 보여주기
            cv2.imshow("frame", frame)
        else:
            break
        # waitKey(int(1000.0/fps)) for matching fps of video
        if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
            break
    # 모든 작업이 완료되면 모든 리소스를 해제
    cap.release()
    cv2.destroyAllWindows()
    return
   
if __name__=="__main__":
    videoProcess(gst_str)
