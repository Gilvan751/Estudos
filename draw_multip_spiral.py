import turtle
turtle.Screen()
turtle.speed(0)
turtle.pensize(2)
ts = turtle.getscreen()
ts.setup(width = 1.0, height = 1.0 )

length = 250
min_length = 32
angles = [89,73,90,120,122,145]
steps = [1,1,4,4,4,4]
x_pos = [-720,-190,518,-730,25,455]
y_pos = [160,232,115,-160, -362,-120]

colors = ['red', 'green', 'orange', 'violet',
          'yellow', 'blue', 'magenta', 'cyan']
def Spiral(length, angle, step, min_length):
    while(length > min_length):
        turtle.color(colors[length % 8])
        turtle.fd(length)
        turtle.lt(angle)
        length = length - step

for i in range(6):
    turtle.penup()
    turtle.goto(x_pos[i], y_pos[i])
    turtle.pendown()
    angle = angles[i]
    step = steps[i]
    Spiral(length, angle, step, min_length)
    
turtle.done()