# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
from turtle import *
import time

tt = Turtle()

Screen().setup(1000, 800, 0, 0)
tt.speed(0)
tt.penup()
tt.seth(90)
tt.fd(340)
tt.seth(0)
tt.pendown()

tt.speed(5)
tt.begin_fill()
tt.fillcolor('red')
tt.circle(50, 30)

for i in range(10):
    tt.fd(1)
    tt.left(10)

tt.circle(40, 40)

for i in range(6):
    tt.fd(1)
    tt.left(3)

tt.circle(80, 40)

for i in range(20):
    tt.fd(0.5)
    tt.left(5)

tt.circle(80, 45)

for i in range(10):
    tt.fd(2)
    tt.left(1)

tt.circle(80, 25)

for i in range(20):
    tt.fd(1)
    tt.left(4)

tt.circle(50, 50)

time.sleep(0.1)

tt.circle(120, 55)

tt.speed(0)

tt.seth(-90)
tt.fd(70)

tt.right(150)
tt.fd(20)

tt.left(140)
tt.circle(140, 90)

tt.left(30)
tt.circle(160, 100)

tt.left(130)
tt.fd(25)

tt.penup()
tt.right(150)
tt.circle(40, 80)
tt.pendown()

tt.left(115)
tt.fd(60)

tt.penup()
tt.left(180)
tt.fd(60)
tt.pendown()

tt.end_fill()

tt.right(120)
tt.circle(-50, 50)
tt.circle(-20, 90)

tt.speed(1)
tt.fd(75)

tt.speed(0)
tt.circle(90, 110)

tt.penup()
tt.left(162)
tt.fd(185)
tt.left(170)
tt.pendown()
tt.circle(200, 10)
tt.circle(100, 40)
tt.circle(-52, 115)
tt.left(20)
tt.circle(100, 20)
tt.circle(300, 20)
tt.speed(1)
tt.fd(250)

tt.penup()
tt.speed(0)
tt.left(180)
tt.fd(250)
tt.circle(-300, 7)
tt.right(80)
tt.circle(200, 5)
tt.pendown()

tt.left(60)
tt.begin_fill()
tt.fillcolor('green')
tt.circle(-80, 100)
tt.right(90)
tt.fd(10)
tt.left(20)
tt.circle(-63, 127)
tt.end_fill()

tt.penup()
tt.left(50)
tt.fd(20)
tt.left(180)

tt.pendown()
tt.circle(200, 25)

tt.penup()
tt.right(150)

tt.fd(180)

tt.right(40)
tt.pendown()
tt.begin_fill()
tt.fillcolor('green')
tt.circle(-100, 80)
tt.right(150)
tt.fd(10)
tt.left(60)
tt.circle(-80, 98)
tt.end_fill()

tt.penup()
tt.left(60)
tt.fd(13)
tt.left(180)

tt.pendown()
tt.speed(1)
tt.circle(-200, 23)

Screen().exitonclick()
