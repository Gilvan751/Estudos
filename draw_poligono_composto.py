# draw Square in Python Turtle
import turtle

t = turtle.Turtle()

s = int(input("Enter the length of the side of square: "))
t.color('red')

t.begin_fill()


for _ in range(4):
    t.forward(s) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
t.end_fill()

turtle.done()
