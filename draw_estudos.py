import turtle
turtle.Screen()
bob = turtle.Turtle('turtle')
bob.speed(10)


def square(bob):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)


square(bob)
alice = turtle.Turtle()
alice.speed(10)
alice.up()
alice.goto(100,100)
alice.pd()
square(alice)

def squares(t, length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)

squares(bob, 90)


def polygon(t, n, length):
     angle = 360 / n
     for i in range(n):
         t.fd(length)
         t.lt(angle)

polygon(bob, 7, 70)



turtle.done()
