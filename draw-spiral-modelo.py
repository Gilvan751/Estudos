import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")
myPen.pensize(5)

side=400
myPen.penup()
myPen.goto(-200,-200) #position cursor at the bootom right of the screen
myPen.pendown()
colors = ['red', 'violet', 'blue', 'yellow']

#Start Spiral
for i in range (1,100):
   myPen.color(colors[i % 4])
   myPen.forward(side)
   myPen.left(90)
   side=side-4

turtle.done()