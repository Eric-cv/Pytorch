# coding=utf-8
# @Time     :2020/5/9 0009 21:06
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tensorboard01.py
# @Software :PyCharm
from tensorboardX import SummaryWriter
from PIL import Image
import numpy as np
# writer.add_scalar()
writer = SummaryWriter('logs')

# y = x
for i in range(100):
    writer.add_scalar('y=x', i, i)

writer.close()

# y = 2x
# for i in range(100):
#     writer.add_scalar('y=2x', 2*i, i)
#
# writer.close()

# tensorboard --logdir=logs


# writer.add_image()
image_path = r'Pytorch_Practice\hymenoptera_data\hymenoptera_data\train\ants\0013035.jpg'
img_PIL = Image.open(image_path)
# 将PIL类型的图片转为numpy类
img_array = np.array(img_PIL)
print(type(img_PIL))
print(type(img_array))

writer.add_image('test', img_array, 1, dataformats='HWC')
writer.close()