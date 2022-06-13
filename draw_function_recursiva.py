import turtle
turtle.title('Função recursiva')

turtle.Screen()
t = turtle.Turtle('turtle')
t.penup()
t.goto(-300, 0)
t.pendown()
t.pensize(2)
t.speed(0)
n = 6
length = 4


def recursiva(n, length):
    if n == 0:
        t.fd(length)
    else:
        recursiva(n - 1, length)
        t.lt(60)
        recursiva(n - 1, length)
        t.lt(-120)
        recursiva(n - 1, length)
        t.lt(60)
        recursiva(n - 1, length)
        
        


recursiva(n, length)
turtle.done()
        