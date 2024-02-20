import numpy
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import math
sns.set()
iris = pd.read_csv('./iris.csv')
iris = iris.drop('Id', axis=1)
pd.options.mode.chained_assignment = None #предотвращаем ошибку
iris['Species'] = pd.factorize(iris['Species'])[0]
X_train = iris.drop('Species', axis=1)
y_train = iris['Species']

print(iris)
arrX=X_train.to_numpy()
arrY=np.transpose(y_train.to_numpy())
arrY=np.array(arrY, dtype='f')
for i in range(0,150):

    arrY[i]=np.float64(arrY[i])/10

for i in range(0,150):
    for j in range(0,4):
        arrX[i][j]=float(arrX[i][j])/10
def sigmoid(x):#функция активации
    return 1/(1+np.exp(-x))
training_inputs=np.array(arrX)
training_outputs=np.array([arrY]).T
np.random.seed(1)
synaptic_weights=2*np.random.random((4,1))-1 #генерируем случайные инициаизирующие веса:
#Используем Perceptron
#Метод обратного распространения
for epochs in range(2000):
    input_layer=training_inputs
    outputs=sigmoid(np.dot(input_layer, synaptic_weights))#np.dot-скалярное произведение

    err=training_outputs-outputs
    adjustment=np.dot(input_layer.T, err*(outputs*(1-outputs)))
    synaptic_weights+=adjustment
    #print(outputs)
    correct = 0
    for j in range(0, 150):
        rew = round(outputs[j][0], 1)
        arrYj = np.float64(arrY[j])
        arrYj = round(arrYj, 1)
        if rew == arrYj:
            correct = correct + 1

    accuracy = correct / 150
    with open("logs.csv", "a") as myfile:  # a-append-добавляет текст к существующему тексту
        myfile.write(f"\n{epochs},{accuracy}")


