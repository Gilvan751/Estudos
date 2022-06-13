import turtle

turtle.Screen()
turtle.bgcolor('black')
turtle.pencolor('white')
colors = ['red', 'green', 'blue', 'yellow']

turtle.speed(0)
turtle.pensize(2)
for i in range(200):
    turtle.color(colors[ i %4])
    turtle.circle(i)
    turtle.lt(91)



turtle.done()