import turtle

tela = turtle.Screen()
t = turtle.Turtle()

t.shape('turtle')
t.pensize(5)


def poligono(lados, tamanho, cor):
    for i in range(lados):
        t.color(cor)
        t.fd(tamanho)
        t.lt(360 / lados)


t.speed(0)
cores = ('green', 'purple', 'blue', 'yellow', 'orange', 'violet', 'red')


#for i in range(10):
#   print(f'{i} => {cores[i % len(cores)]}')
for i in range(3, 12):
    poligono(i, 100, cores[(i - 3) % len(cores)])


turtle.done()
