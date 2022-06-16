import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk=turtle.Turtle()
skk.pensize(5)
""" skk.color("blue") """
colors = ['red', 'green', 'orange', 'violet']

def sqrfunc(size):
	for i in range(4):
		skk.color(colors[i % 8])
		skk.fd(size)
		skk.lt(90)
		size = size -5

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)

turtle.done()