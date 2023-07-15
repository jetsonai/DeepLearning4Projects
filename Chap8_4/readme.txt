./build_darknet_on_jetson_nano.sh

cd darknet

python3 darknet_video.py \
--input blackbox.avi \
--weights yolov4-tiny_voc_last.weights \
--config_file yolov4-tiny_voc.cfg \
--data_file vocdata.txt \
--thresh 0.25

