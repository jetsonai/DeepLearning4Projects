#!/bin/bash
sudo add-apt-repository ppa:jonathonf/ffmpeg-4
sudo apt-get update
sudo apt install gcc make cmake curl vim git python-dev python3-dev \
 python-pip python3-pip libgflags-dev v4l-utils pyqt5-dev-tools build-essential \
 python3-dev cython3 python3-setuptools python3-pip python3-wheel python3-numpy \
 python3-pytest python3-blosc python3-brotli python3-snappy python3-lz4 zlib1g-dev \
 libblosc-dev liblzma-dev liblz4-dev libzstd-dev libpng-dev libwebp-dev libbz2-dev \
 libopenjp2-7-dev libjpeg-turbo8-dev libjxr-dev liblcms2-dev libcharls-dev libaec-dev \
 libbrotli-dev libsnappy-dev libzopfli-dev libgif-dev libtiff-dev qt5-default \
 libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev -y
sudo apt-get install -y \
apt-utils cmake unzip curl pkg-config build-essential \
gstreamer1.0-tools gstreamer1.0-alsa \
 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
 gstreamer1.0-libav \
 libgstreamer1.0-dev \
 libgstreamer-plugins-base1.0-dev \
 libgstreamer-plugins-bad1.0-dev \
 cmake libgflags-dev pyqt5-dev-tools\
 libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev \
 libswscale-dev libxvidcore-dev libx264-dev libxine2-dev \
 libv4l-dev ffmpeg v4l-utils gstreamer1.0-tools gstreamer1.0-alsa \
 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
 gstreamer1.0-plugins-ugly gstreamer1.0-libav libgstreamer1.0-dev \
 libgstreamer-plugins-base1.0-dev  \
 libgstreamer-plugins-bad1.0-dev qtbase5-dev libqt4-dev mesa-utils libgl1-mesa-dri \
 libqt4-opengl-dev libatlas-base-dev gfortran libeigen3-dev python2.7-dev \
 python3-dev python-numpy python3-numpy python-pip python3-pip python3-matplotlib
cd && mkdir OPENCV_INSTALL && cd OPENCV_INSTALL && wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.1.zip && unzip opencv.zip && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.1.zip && unzip opencv_contrib.zip && rm opencv.zip && rm opencv_contrib.zip
cd && cd OPENCV_INSTALL/opencv-4.5.1/ && mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_CUDA=OFF \
-D WITH_TBB=OFF \
-D WITH_IPP=OFF \
-D WITH_1394=OFF \
-D BUILD_WITH_DEBUG_INFO=OFF \
-D BUILD_DOCS=OFF \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D BUILD_EXAMPLES=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_PERF_TESTS=OFF \
-D WITH_QT=ON \
-D WITH_OPENGL=ON \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.1/modules \
-D WITH_V4L=ON  \
-D WITH_FFMPEG=ON \
-D WITH_XINE=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D OPENCV_GENERATE_PKGCONFIG=ON \
../
make -j $(nproc)
sudo make install && sudo ldconfig
echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/lib" >> ~/.bashrc