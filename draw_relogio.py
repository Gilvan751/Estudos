# import package
import turtle

# create a Screen Object
screen = turtle.Screen()

# Screen configuration
screen.setup(500, 500)

# Make turtle Object
t= turtle.Turtle()

# set a Turtle object color
t.color('blue')

# set a Turtle object width
t.width(4)


def draw_hour_hand():
	t.penup()
	t.home()
	t.rt(90)
	t.pd()
	t.fd(100)


# value for numbers in clock
val = 0

# loop for print clock numbers
for i in range(12):
	# increment value by 1
	val += 1

	# move turtle in air
	t.up()

	# for circular motion
	t.setheading(-30 * (i + 3) + 75)

	# move forward for space
	t.fd(22)

	# move turtle to surface
	t.pd()

	# move forward for dash line
	t.fd(15)

	# move turtle in air
	t.up()

	# move forward for space
	t.fd(20)

	# write clock integer
	t.write(str(val), align="center",
			font=("Arial",
					12, "normal"))

# colored centre by setting position
# sets position of turtle at given position
t.setpos(2, -112)
t.pd()
t.width(2)

# To fill color green
t.fillcolor('Green')

# start filling
t.begin_fill()

# make a circle of radius 5
t.circle(5)

# end filling
t.end_fill()

t.up()
draw_hour_hand()
t.setpos(-20, -64)
t.pd()
t.up()

# Write Clock by setting position
t.setpos(-30, -170)
t.pd()
t.write(' GfG Clock', font=("Arial", 14,
							"normal"))
t.hideturtle()
turtle.done()
