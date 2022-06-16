import turtle
import math

wn = turtle.Screen()
wn.bgcolor("#4C3A51")

myPen = turtle.Turtle()
myPen.speed(0)
myPen.pensize(5)
size=200
colors = ['#035397', '#E8630A', 'red', '#FCD900']
myPen.setheading(90) #Point the top
for i in range(0,6):
  myPen.color(colors[i % 4])
  myPen.fd(size)
  myPen.up()
  myPen.fd(-size)
  myPen.lt(60)
  myPen.pd()

myPen.setheading(90) #Point the top
myPen.fd(size)
myPen.setheading(215) #Point the left
newSize=size
newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(65))
for i in range(0,30):  
   myPen.forward(newSize)
   myPen.left(60)
   newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))

turtle.done()