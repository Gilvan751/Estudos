import turtle
wn = turtle.Screen()
wn.bgcolor("light green")

myPen = turtle.Turtle()
myPen.speed(0)
myPen.pensize(5)

side=50
myPen.penup()
myPen.goto(0,0) #position cursor at the bootom right of the screen
myPen.pendown()
colors = ['blue', 'violet', 'red', 'yellow']

for i in range (1,50):
  myPen.color(colors[i % 4])
  myPen.forward(side)
  myPen.left(92)
  side=side+7


myPen.penup()
myPen.goto(500,500)

#Start Spiral
#for i in range (1,20):
#  for j in range (0,4):
#      myPen.forward(side)
#      myPen.left(90)
#  myPen.left(20)
#  side=side+5
turtle.done()