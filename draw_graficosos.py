import turtle
t = turtle.Turtle()
t.screen.bgcolor('black')
colors = ['blue', 'purple','red','yellow']
t.screen.tracer(0,0)
t.speed(3)
for x in range(300):
    t.color(colors[x%4])
    t.fd(x)
    t.lt(90)

t.screen.exitonclick()
t.screen.mainloop()