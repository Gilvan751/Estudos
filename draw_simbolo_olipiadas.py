import turtle

# object tr for turtle
tr = turtle.Turtle()

# set thickness for each ring
tr.pensize(5)

tr.color("blue")
tr.up()
tr.goto(-110, -25)
tr.pd()
tr.circle(45)

tr.color("black")
tr.up()
tr.goto(0, -25)
tr.pd()
tr.circle(45)

tr.color("red")
tr.up()
tr.goto(110, -25)
tr.pd()
tr.circle(45)

tr.color("yellow")
tr.up()
tr.goto(-55, -75)
tr.pd()
tr.circle(45)

tr.color("green")
tr.up()
tr.goto(55, -75)
tr.pd()
tr.circle(45)
turtle.done()
