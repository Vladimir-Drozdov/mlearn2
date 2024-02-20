#github.com/spbcoding/ml-aws-course/blob/main/lab07-cnn-1.ipynb - github преподавателя
#https://github.com/spbcoding/ml-aws-course/blob/torch/lab07-cnn-1-pytorch.ipynb
#пример LeNet приведет, надо сделать AlexNet самостоятельно
#AlexNet не релевантно запускать на выданной датасете, просто все сигмоиды и тангенсы(если есть) в lenet-е заменить на ReLU
#занятие 09.12 - transfer learning - обучаем нейронку при помощи resnet (уже готовая программа) потом добавляем свои слои в обучение и получаем рез-тат
# pip install tqdm pytorche
import torch
from torch import nn
import torch.optim as optim

import pickle

import numpy as np
import matplotlib.pyplot as plt
# setting device on GPU if available, else CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
# Open the files:
train_fh = open('data/lego-train.pickle', 'rb')
test_fh = open('data/lego-test.pickle', 'rb')

# Use pickle to load files into runtime objects:
train_data = pickle.load(train_fh)
test_data = pickle.load(test_fh)

# train_data -> [] of tuples: (ndarray, uint8 label)

class_names = ['2x3 Brick', '2x2 Brick', '1x3 Brick', '2x1 Brick', '1x1 Brick', '2x2 Macaroni', '2x2 Curved End', 'Cog 16 Tooth', '1x2 Handles', '1x2 Grill']
transformer = transforms.Compose([  #соталось с mxnet непонятно как use
    transforms.ToTensor(),
    transforms.Normalize(0.13, 0.31)])

train_data = train_data.transform_first(transformer)
test_data = test_data.transform_first(transformer)
train_image_no = 44

images_data, label_data = train_data[train_image_no]
print('Original shape is ', images_data.shape)
plt.figure()
plt.imshow(images_data.reshape((48,48)))
plt.colorbar()
plt.xlabel(class_names[label_data])
plt.show()