import os

from PIL import Image

import torch
from torch.utils.data import Dataset


########## Custom DataLoader ##########
class PyTorchCustomDataset(Dataset):
    def __init__(self, root_dir="cats_and_dogs_filtered/train", transform=None):
        self.image_abs_path = root_dir
        self.transform = transform
        self.label_list = os.listdir(self.image_abs_path)
        self.label_list.sort()
        self.x_list = []
        self.y_list = []
        for label_index, label_str in enumerate(self.label_list):
            img_path = os.path.join(self.image_abs_path, label_str)
            img_list = os.listdir(img_path)
            for img in img_list:
                self.x_list.append(os.path.join(img_path, img))
                self.y_list.append(label_index)
        pass

    def __len__(self):
        return len(self.x_list)

    def __getitem__(self, idx):
        image = Image.open(self.x_list[idx])
        if image.mode != "RGB":
            image = image.convert('RGB')
        if self.transform is not None:
            image = self.transform(image)
        return image, torch.tensor(self.y_list[idx]).type(torch.LongTensor)

    def __save_label_map__(self, dst_text_path="label_map.txt"):
        label_list = self.label_list
        f = open(dst_text_path, 'w')
        for i in range(len(label_list)):
            f.write(label_list[i]+'\n')
        f.close()
        pass

    def __num_classes__(self):
        return len(self.label_list)