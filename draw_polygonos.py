import turtle
t = turtle.Turtle()
turtle.Screen()
t.speed(10)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(t, 8, 70)

turtle.done()
