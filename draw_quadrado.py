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
    turtle.lt(90)






turtle.end_fill()
turtle.up()

turtle.goto(200,0)
turtle.color('green')
turtle.begin_fill()
turtle.pd()
for i in range(3):
    turtle.fd(200)
    turtle.lt(120)
turtle.end_fill()


turtle.done()

