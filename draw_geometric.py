import turtle
colors = ['green', 'purple', 'blue', 'yellow', 'orange', 'violet', 'red']
t = turtle.Pen()
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x//100 + 1)
    t.fd(x)
    t.lt(59)
turtle.done()