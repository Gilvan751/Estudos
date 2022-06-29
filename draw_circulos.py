import turtle
import math
t = turtle.Turtle()
turtle.Screen()
t.speed(10)

def polygon(t, n = 7, length = 70):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t,r):
    circunference = 2 * math.pi * r
    n = int(circunference / 3) +1
    length = circunference / n
    polygon(t,n,length)

circle(t, 100)

turtle.done()