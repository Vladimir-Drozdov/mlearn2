import numpy as np
def sigmoid(x):#функция активации
    return 1/(1+np.exp(-x))
training_inputs=np.array([[0.3,0,1],[0.4,1,1],[0.7,0,1],[0,1,1]])
training_outputs=np.array([[0.3,0.4,0.7,0]]).T
np.random.seed(1)
synaptic_weights=2*np.random.random((3,1))-1
print("Случайные инициаизирующие веса:")
print(synaptic_weights)
#Метод обратного распространения
for i in range(20000):
    input_layer=training_inputs
    outputs=sigmoid(np.dot(input_layer, synaptic_weights))#np.dot-скалярное произведение

    err=training_outputs-outputs
    adjustment=np.dot(input_layer.T, err*(outputs*(1-outputs)))
    synaptic_weights+=adjustment
print("Веса после обучения")
print(synaptic_weights)
print("Результат после обучения")
print(outputs)
#Тест
new_inputs=np.array([1,1,0])#новая ситуация
output=sigmoid(np.dot(new_inputs, synaptic_weights))
print("Новая ситуация")
print(output)
dd=np.float64(7.08876)
dd2=np.float64(7.08876)
print(dd==dd2)
