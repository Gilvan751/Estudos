import turtle
t=turtle.Turtle()
t.screen.bgcolor('black')
colors =['blue', 'purple', 'red','yellow','orange','cyan']
t.speed(5)
t.screen.tracer(0,0)
for x in range(300):
    t.color(colors[x%6])
    t.fd(x)
    t.lt(59)


t.screen.exitonclick()
t.screen.mainloop()