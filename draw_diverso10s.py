import turtle
colors = ["red", "blue", "green", "gray", "orange", "black"]
a = turtle.Turtle()
a.pensize(5)
a.speed(5)
for i in range(130):
     a.color(colors[i%6])
     if i%2==0:
         a.pendown()
         a.forward(i/10)
         a.hideturtle()
     else:
         a.penup()
         a.forward(5+i/10)
         a.showturtle()
         a.left(40 - i/1.5)
turtle.exitonclick()