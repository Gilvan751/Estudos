# importing turtle
import turtle

# initialise the turtle instance
animation = turtle.Turtle()

#creating animation
# changes speed of turtle
animation.speed(0)

# hiding turtle
animation.hideturtle()

# changing background color
animation.getscreen().bgcolor("black")

# color of the animation color
colors = ['red', 'blue', 'green', 'violet']
animation.color(colors[3])


for i in range(100):
    
	
	# drawing circle using circle function
	# by passing radius i
	animation.circle(i)

	# changing turtle face by 5 degree from it's
	# previous position after drawing a circle
	animation._rotate(8)


turtle.done()