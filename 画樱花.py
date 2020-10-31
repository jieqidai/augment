# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:22:36 2019

@author: Administrator
"""

import turtle as T
import random
import time

# 画樱花的躯干(60,t)
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')  # wheat小麦
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的躯干
Tree(60, t)
# 掉落的花瓣
Petal(200, t)
w.exitonclick()

#%%
import turtle as T
import random
import time

# 画樱花的躯干(60,t)
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')  # wheat小麦
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的躯干
Tree(60, t)
# 掉落的花瓣
Petal(200, t)
w.exitonclick()

#%%
from turtle import *
from random import *
from math import *

def tree(n,l):
    pd()#下笔
    #阴影效果
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)#画树枝

    if n>0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        right(b)
        tree(n-1,d)
        #左转一定角度，画左分支
        left(b+c)
        tree(n-1,d)
        #转回来
        right(c)
    else:
        #画叶子
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n*0.8,n*0.8)
        circle(3)
        left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            pu()
            #飘落
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #画叶子
            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            circle(2)
            left(90)
            pu()
            #返回
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)#退回

bgcolor(0.5,0.5,0.5)#背景色
ht()#隐藏turtle
speed(0)#速度 1-10渐进，0 最快
tracer(0,0)
pu()#抬笔
backward(100)
left(90)#左转90度
pu()#抬笔
backward(300)#后退300
tree(12,100)#递归7层
done()
#%%
from turtle import *
from random import *
from math import *

def tree(n,l):
    pd()#下笔
    #阴影效果
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)#画树枝

    if n>0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        right(b)
        tree(n-1,d)
        #左转一定角度，画左分支
        left(b+c)
        tree(n-1,d)
        #转回来
        right(c)
    else:
        #画叶子
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n*0.8,n*0.8)
        circle(3)
        left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            pu()
            #飘落
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #画叶子
            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            circle(2)
            left(90)
            pu()
            #返回
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)#退回

bgcolor(0.5,0.5,0.5)#背景色
ht()#隐藏turtle
speed(0)#速度 1-10渐进，0 最快
tracer(0,0)
pu()#抬笔
backward(100)
left(90)#左转90度
pu()#抬笔
backward(300)#后退300
tree(12,100)#递归7层
done()
#%%
from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)
bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
tracer(0, 0)
left(90)
pu()
backward(300)
tree(13, 100)
done()
#%%


from turtle import *
import time

setup(1000,800,0,0)
speed(0)
penup()
seth(90)
fd(340)
seth(0)
pendown()

speed(5)
begin_fill()
fillcolor('red')
circle(50,30)

for i in range(10):
    fd(1)
    left(10)

circle(40,40)

for i in range(6):
    fd(1)
    left(3)

circle(80,40)

for i in range(20):
    fd(0.5)
    left(5)

circle(80,45)

for i in range(10):
    fd(2)
    left(1)

circle(80,25)

for i in range(20):
    fd(1)
    left(4)

circle(50,50)

time.sleep(0.1)

circle(120,55)

speed(0)

seth(-90)
fd(70)

right(150)
fd(20)

left(140)
circle(140,90)

left(30)
circle(160,100)

left(130)
fd(25)

penup()
right(150)
circle(40,80)
pendown()

left(115)
fd(60)

penup()
left(180)
fd(60)
pendown()

end_fill()

right(120)
circle(-50,50)
circle(-20,90)

speed(1)
fd(75)

speed(0)
circle(90,110)

penup()
left(162)
fd(185)
left(170)
pendown()
circle(200,10)
circle(100,40)
circle(-52,115)
left(20)
circle(100,20)
circle(300,20)
speed(1)
fd(250)

penup()
speed(0)
left(180)
fd(250)
circle(-300,7)
right(80)
circle(200,5)
pendown()

left(60)
begin_fill()
fillcolor('green')
circle(-80,100)
right(90)
fd(10)
left(20)
circle(-63,127)
end_fill()

penup()
left(50)
fd(20)
left(180)

pendown()
circle(200,25)

penup()
right(150)

fd(180)

right(40)
pendown()
begin_fill()
fillcolor('green')
circle(-100,80)
right(150)
fd(10)
left(60)
circle(-80,98)
end_fill()

penup()
left(60)
fd(13)
left(180)

pendown()
speed(1)
circle(-200,23)



exitonclick()

