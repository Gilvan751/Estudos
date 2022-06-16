import turtle


# getting a Screen to work on
ws=turtle.Screen()

# Defining Turtle instance
t=turtle.Turtle()

# setting up turtle color to green
t.color("Green")

# Setting Up width to 2
t.width("2")

# Setting up speed to 2
t.speed(2)

# Loop for making outside square of
# length 300
for i in range(4):
	t.fd(300)
	t.lt(90)


# code for inner lines of the square
t.up()
t.goto(0,100)
t.pd()

t.fd(300)

t.up()
t.goto(0,200)
t.pd()

t.fd(300)

t.up()
t.goto(100,0)
t.pd()

t.lt(90)
t.fd(300)

t.up()
t.goto(200,0)
t.pd()


t.fd(300)
turtle.done()