from cmath import sqrt
import turtle
wn = turtle.Screen()
wn.bgcolor("#c2c2c2")

turtle.pensize(5)
turtle.color('white')
turtle.begin_fill()
turtle.up()
turtle.goto(-300,0)
turtle.pd()
for i in range(4):
    turtle.fd(200)
    turtle.lt(360/4)






turtle.end_fill()
turtle.up()

turtle.goto(200,0)
turtle.color('green')
turtle.begin_fill()
turtle.pd()
for i in range(3):
    turtle.fd(200)
    turtle.lt(360/3)
turtle.end_fill()

turtle.up()

turtle.goto(0,0)
turtle.color('red')
turtle.begin_fill()
turtle.pd()
for i in range(5):
    turtle.fd(150)
    turtle.lt(360/5)
turtle.end_fill()

turtle.up()

turtle.goto(0,-250)
turtle.color('blue')
turtle.begin_fill()
turtle.pd()
turtle.circle(100)
turtle.end_fill()
side = 30
turtle.up()

turtle.goto(250,-170)
turtle.color('violet')

turtle.pd()
for i in range(1,20):
        turtle.fd(side)
        turtle.lt(90)
        side +=7


        








turtle.done()

