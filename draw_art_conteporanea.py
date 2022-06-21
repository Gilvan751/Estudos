import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
t.pencolor('#ffffff')
s.bgcolor('#000000')
time.sleep(0)
total = 5
repeticao = 50
t.fd(total)
colors = ['green', 'yellow','violet','blue']
for i in range(repeticao):
    t.color(colors[i % 4])
    t.fd(total)
    t.lt(91)
    total +=10


turtle.done()