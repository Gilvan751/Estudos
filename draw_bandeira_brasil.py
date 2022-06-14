import turtle

turtle.title('Bandeira do Brasil')

turtle.Screen()
t = turtle.Turtle('turtle')
t.penup()

t.pendown()
t.pensize(2)
t.speed(1)

#retangulo
t.color('green')
t.begin_fill()
t.goto(150,0)
t.goto(150,100)
t.goto(-250,100)
t.goto(-250, -100)
t.goto(150, -100)
t.goto(150,0)
t.end_fill()
t.pu()
#losangulo
t.color('yellow')
t.begin_fill()
t.goto(100,0)

t.goto(-50,80)
t.goto(-200,0)
t.goto(-50,-80)
t.goto(100,0)

t.end_fill()
t.pu()
t.goto(-50,-50)

t.color('Blue')
t.begin_fill()
t.circle(50)
t.end_fill()
t.pu()
t.goto(250,0)

turtle.done()
