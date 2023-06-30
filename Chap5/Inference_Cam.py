#!python3
import torch
import cv2
from PIL import Image
import torchvision.transforms as transforms
import numpy as np
from Model_Class_From_the_Scratch import MODEL_From_Scratch
from Model_Class_Transfer_Learning_MobileNet import MobileNet
import argparse
import cv2


class Inference_Class():
    def __init__(self):
        USE_CUDA = torch.cuda.is_available()
        self.DEVICE = torch.device("cuda" if USE_CUDA else "cpu")
        self.model = None
        self.label_map = None
        self.transform_info = transforms.Compose([
                transforms.Resize(size=(224, 224)),
                transforms.ToTensor()
                ])


    def load_model(self, is_train_from_scratch, label_map_file = "label_map.txt"):
        self.label_map = np.loadtxt(label_map_file, str, delimiter='\t')
        num_classes = len(self.label_map)
        model_str = None
        if is_train_from_scratch:
            self.model = MODEL_From_Scratch(num_classes).to(self.DEVICE)
            model_str = "PyTorch_Training_From_Scratch"
        else:
            self.model = MobileNet(num_classes).to(self.DEVICE)
            model_str = "PyTorch_Transfer_Learning_MobileNet"
        model_str += ".pt"
        self.model.load_state_dict(torch.load(model_str, map_location=self.DEVICE))
        self.model.eval()
        
        
    def inference_video(self, video_source="test_video.mp4"):
        cap = cv2.VideoCapture(video_source)
        if cap.isOpened():
            print("Video Opened")
        else:
            print("Video Not Opened")
            print("Program Abort")
            exit()
        cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)
        with torch.no_grad():
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    output = self.inference_frame(frame)
                    cv2.imshow("Output", output)
                else:
                    break
                if cv2.waitKey(33) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
        return
    

    def inference_frame(self, opencv_frame):
        opencv_rgb = cv2.cvtColor(opencv_frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(opencv_rgb)
        image_tensor = self.transform_info(image)
        image_tensor = image_tensor.unsqueeze(0)
        image_tensor = image_tensor.to(self.DEVICE)
        inference_result = self.model(image_tensor)
        inference_result = inference_result.squeeze()
        inference_result = inference_result.cpu().numpy()
        result_frame = np.copy(opencv_frame)
        label_text = self.label_map[np.argmax(inference_result)]
        label_text += " " + str(inference_result[np.argmax(inference_result)])
        result_frame = cv2.putText(result_frame, label_text, (10, 50), cv2.FONT_HERSHEY_PLAIN, fontScale=2.0, color=(0,0,255), thickness=3)
        return result_frame
    
    
    def inference_image(self, opencv_image):
        opencv_rgb = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(opencv_rgb)
        image_tensor = self.transform_info(image)
        image_tensor = image_tensor.unsqueeze(0)
        image_tensor = image_tensor.to(self.DEVICE)
        with torch.no_grad():
            inference_result = self.model(image_tensor)
        inference_result = inference_result.squeeze()
        inference_result = inference_result.cpu().numpy()
        result_frame = np.copy(opencv_image)
        label_text = self.label_map[np.argmax(inference_result)]
        class_prob = str(inference_result[np.argmax(inference_result)])
        result_frame = cv2.putText(result_frame, label_text + " " + class_prob, (10, 50), cv2.FONT_HERSHEY_PLAIN, fontScale=2.0, color=(0,0,255), thickness=3)
        return result_frame, label_text, class_prob


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--is_scratch", 
            required=False,
            action="store_true", 
            help="inference with model trained from the scratch")
    parser.add_argument("-src", "--source", 
            required=False,
            type=str, 
            default="./test_video.mp4", 
            help="OpenCV Video source")
    args = parser.parse_args()
    is_train_from_scratch = False
    source = args.source
    if args.is_scratch:
        is_train_from_scratch = True
    if source.isdigit():
        source = int(source)
    inferenceClass = Inference_Class()
    inferenceClass.load_model(is_train_from_scratch)
    inferenceClass.inference_video(source)
