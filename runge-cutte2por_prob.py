import math
import numpy
from matplotlib import pyplot as plt
def fun1(x, y1, y2, y3, y4):
    return 2*x*pow(y2, -0.5)*y4
def fun2(x,y1,y2, y3,y4):
    if(abs(y3)>60):
        y3=60*numpy.sign(y3)
    return 2*(-2)*x*(math.exp((-1)*(y3.real+2)))*y4
def fun3(x,y1,y2,y3,y4):
    return 4*x*y4
def fun4(x,y1,y2,y3,y4):
    return (-2)*x*math.log(abs(y1.real))###
def y1accurate(x):
    return math.exp(math.sin(pow(x, 2)))
def y2accurate(x):
    return math.exp((-2)*math.sin(pow(x, 2)))
def y3accurate(x):
    return 2*(math.sin(pow(x, 2)))-2
def y4accurate(x):
    return math.cos(pow(x, 2))
x0=0
y10=1
y20=1
y30=-2
y40=1
h=1 #0.1-повляеются комплексные и работает не очень, 0.01-хорошо работает и комплексные пропадают, 0.001-оч хорошо
k2 = [0]*4
#Метод второго порядка
b1 = (-7) / 3
b2 = 10 / 3
for i in range(1,5+1):
    k1=[fun1(x0,y10,y20,y30,y40), fun2(x0,y10,y20,y30,y40),
        fun3(x0,y10,y20,y30,y40), fun4(x0,y10,y20,y30,y40)]
    k2[0]=fun1(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[1]=fun2(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[2]=fun3(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[3]=fun4(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    y11=y10+h*(b1*k1[0]+b2*k2[0])
    y21=y20+h*(b1*k1[1]+b2*k2[1])
    y31=y30+h*(b1*k1[2]+b2*k2[2])
    y41=y40+h*(b1*k1[3]+b2*k2[3])
    print(x0,y10,y20,y30,y40)
    print(h*i, y11,y21,y31,y41, fun1(x0,y10,y20,y30,y40))
    #h=h+0.1
    x0=x0+h
    y10=y11
    y20=y21
    y30=y31
    y40=y41
print(2*pow(-1, -0.5))