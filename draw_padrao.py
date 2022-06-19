import turtle             
my_wn = turtle.Screen()
turtle.speed(0)
turtle.pensize(2)
colors = ['red', 'blue', 'green', 'violet']
for i in range(30):
   turtle.color(colors[i % 4])
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
turtle.exitonclick()