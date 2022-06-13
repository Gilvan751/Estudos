import turtle

turtle.Screen()
t= turtle.Turtle()

t.speed(0)
t.pensize(2)

colors = ['red', 'green', 'orange', 'violet',
          'yellow', 'blue']
for i in range(180):
    t.color(colors[i % 6])
    t.fd(100)
    t.rt(30)
    t.fd(20)
    t.lt(60)
    t.fd(50)
    t.rt(30)
    
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.rt(2)
    
turtle.done()