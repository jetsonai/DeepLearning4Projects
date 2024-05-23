sudo apt-get update

sudo apt-get install libpython3-dev -y

sudo apt install python-dev python3-dev python-pip python3-pip python-numpy python3-numpy \
  python3-matplotlib python3-venv -y

sudo -H pip install -U jetson-stats

echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/cuda/lib64" >> ~/.bashrc
echo "export PATH=\$PATH:/usr/local/cuda/bin" >> ~/.bashrc
echo "export OPENBLAS_CORETYPE=ARMV8" >> ~/.bashrc

sudo -H pip3 install --upgrade --ignore-installed pip setuptools

sudo apt install libcanberra-gtk-module libcanberra-gtk3-module -y
