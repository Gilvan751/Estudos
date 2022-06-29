import turtle
turtle.Screen()
bob = turtle.Turtle('turtle')

def square(bob):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)


square(bob)
alice = turtle.Turtle()
alice.up()
alice.goto(100,100)
alice.pd()
square(alice)


turtle.done()
