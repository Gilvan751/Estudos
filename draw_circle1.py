""" import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
t.pensize(5)
t.speed(0)
t.pencolor("yellow")
colors = ['red','yellow','blue','green']
for x in range(360):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.lt(90)
turtle.done() """

from turtle import*
import turtle

shape("circle")
wheel = 12
bgcolor("blue")
pensize(10)
pencolor("green")
colors = ['red', 'green', 'orange','yellow','violet']

for i in range(wheel):
        color(colors[i % 5])
        begin_fill();rt(90);fd(200);lt(120);fd(200);lt(120);fd(200);end_fill()
        fd(200)

turtle.done()