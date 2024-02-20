import math
import numpy
from matplotlib import pyplot as plt
def fun1(x, y1, y2, y3, y4):
    return 2*x*pow(y2,-0.5)*y4
def fun2(x,y1,y2, y3,y4):
    return 2*(-2)*x*(math.exp((-1)*(y3+2)))*y4
def fun3(x,y1,y2,y3,y4):
    return 4*x*y4
def fun4(x,y1,y2,y3,y4):
    return (-2)*x*math.log(abs(y1))###
def y1accurate(x):
    return math.exp(math.sin(pow(x, 2)))
def y2accurate(x):
    return math.exp((-2)*math.sin(pow(x, 2)))
def y3accurate(x):
    return 2*(math.sin(pow(x, 2)))-2
def y4accurate(x):
    return math.cos(pow(x, 2))
#Метод второго порядка с переменным шагом
x0=0
p=2#порядок метода
tol=pow(10,-3)#погрешность для вычисления начального шага
y10=1
y20=1
y30=-2
y40=1
h=0.01
xstart=x0
xend=5
#Выбираем начальный шаг
h1=[0]*2
h1_start_step=0
for i in range(1,3):
    norma_of_fx0y0 = math.sqrt(pow(fun1(x0,y10,y20,y30,y40),2)+pow(fun2(x0,y10,y20,y30,y40),2)+
                               pow(fun3(x0,y10,y20,y30,y40),2)+pow(fun4(x0,y10,y20,y30,y40),2))
    delta = pow((1/max(xstart,xend)), p+1)+pow(norma_of_fx0y0, p+1)
    h1[i-1] = pow((tol/delta),(1/(p+1)))
    print(h1[i-1], x0,fun1(x0,y10,y20,y30,y40),fun2(x0,y10,y20,y30,y40),fun3(x0,y10,y20,y30,y40),fun4(x0,y10,y20,y30,y40))
    k1 = [fun1(x0,y10,y20,y30,y40), fun2(x0,y10,y20,y30,y40),
            fun3(x0,y10,y20,y30,y40), fun4(x0,y10,y20,y30,y40)]
    y11 = y10 + k1[0]*h1[i-1]
    y21 = y20 + k1[1]*h1[i-1]
    y31 = y30 + k1[2]*h1[i-1]
    y41 = y40 + k1[3]*h1[i-1]
    x0 = x0+h1[i-1]
    y10 = y11
    y20 = y21
    y30 = y31
    y40 = y41
    if i!=1:
        h1_start_step = min(h1[0], h1[1])
print("--------")
#Считаем используя алгоритм удвоения и деления шага пополам
h_max=pow(10,-1)#может другой взять
x0wave=0
y10wave=1
y20wave=1
y30wave=-2
y40wave=1
while x0<=5:
    x0 = x0wave
    y10 = y10wave
    y20 = y20wave
    y30 = y30wave
    y40 = y40wave
    h=h1_start_step
    k2 = [0]*4
    b1 = (-7) / 3
    b2 = 10 / 3
    y_with_cherta=[0]*4
    y_with_1and5_cherta=[0]*4
    y_with_2_cherta=[0]*4
    print("new iteration")
    print(h1_start_step,x0,y10,y20,y30,y40)
    i=1
    while (i<=1):
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
        #print(h*i, y11,y21,y31,y41)
        #h=h+0.1
        x0=x0+h
        y10=y11
        y20=y21
        y30=y31
        y40=y41
        y_with_cherta=[y10, y20, y30, y40]
        i=i+1
    h=h1_start_step/2
    x0 = x0wave
    y10 = y10wave
    y20 = y20wave
    y30 = y30wave
    y40 = y40wave
    k1=[0]*4
    k2=[0]*4
    i=1
    while (i<=2):
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
        #print(h*i, y11,y21,y31,y41)
        #h=h+0.1
        x0=x0+h
        y10=y11
        y20=y21
        y30=y31
        y40=y41
        if(i==1):
            y_with_1and5_cherta=[y10, y20, y30, y40]
        y_with_2_cherta=[y10, y20, y30, y40]
        i=i+1
    rn_tolerance_on_every_step=[0]*4
    #print("y_with_cherta",y_with_cherta)
    #print("y_with_1and5_cherta",y_with_1and5_cherta)
    #print("y_with_2_cherta",y_with_2_cherta)
    aaaaa=0
    for i in range(0,4):
        rn_tolerance_on_every_step[i]=(y_with_2_cherta[i]-y_with_cherta[i])/(1-pow(2,(-1)*p))
        aaaaa=aaaaa+pow(rn_tolerance_on_every_step[i],2)
    norma_of_rn_tolerance_on_every_step=math.sqrt(aaaaa)
    #print(rn_tolerance_on_every_step)
    print(norma_of_rn_tolerance_on_every_step)
    if(norma_of_rn_tolerance_on_every_step>tol*pow(2,p)):
        print("1")
        h1_start_step=h1_start_step/2
        x0wave = x0wave+h1_start_step
        y10wave = y_with_1and5_cherta[0]
        y20wave = y_with_1and5_cherta[1]
        y30wave = y_with_1and5_cherta[2]
        y40wave = y_with_1and5_cherta[3]
    if(norma_of_rn_tolerance_on_every_step>tol and norma_of_rn_tolerance_on_every_step<=tol*pow(2,p)):
        print("2")
        h1_start_step=h1_start_step/2
        x0wave = x0wave+h1_start_step
        y10wave = y_with_2_cherta[0]
        y20wave = y_with_2_cherta[1]
        y30wave = y_with_2_cherta[2]
        y40wave = y_with_2_cherta[3]
    if(norma_of_rn_tolerance_on_every_step>tol/(pow(2,p+1)) and norma_of_rn_tolerance_on_every_step<=tol):
        print("3")
        h1_start_step=h1_start_step
        x0wave = x0wave+h1_start_step
        y10wave = y_with_cherta[0]
        y20wave = y_with_cherta[1]
        y30wave = y_with_cherta[2]
        y40wave = y_with_cherta[3]
    if(norma_of_rn_tolerance_on_every_step<=tol/(pow(2,p+1))):
        print("4")
        h1_start_step=min(2*h1_start_step, h_max)
        x0wave = x0wave+h1_start_step/2
        y10wave = y_with_cherta[0]
        y20wave = y_with_cherta[1]
        y30wave = y_with_cherta[2]
        y40wave = y_with_cherta[3]