# coding=utf-8
# @Time     :2020/5/9 0009 17:17
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :my_dataset.py
# @Software :PyCharm
from torch.utils.data import Dataset
import os
from PIL import Image


class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_iter_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_iter_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)


# 创建蚂蚁数据集
root_dir = r'E:\Files_plus\Project01\Pytorch_Practice\hymenoptera_data\hymenoptera_data\train'
ants_label_dir = 'ants'
ants_dataset = MyData(root_dir, ants_label_dir)
img, label = ants_dataset[0]
img.show()

# 创建蜜蜂数据集
bees_label_dir = 'bees'
bees_dataset = MyData(root_dir, bees_label_dir)
img, label = bees_dataset[0]
img.show()

train_dataset = ants_dataset + bees_dataset
