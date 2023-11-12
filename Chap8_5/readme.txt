# trt 변환

./yolov5_det -s yolov5s_voc.wts yolov5s_voc.engine s

#추론

./yolov5_det -d yolov5s_voc.engine ../images
