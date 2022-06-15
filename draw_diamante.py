import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape("square")
t.speed(2)
 
# Nível fácil - apenas o contorno do diamante (passos 1 a 3)

#contorno
t.pensize(6)
t.goto(100, 100)
t.goto(60, 130)
t.goto(-60, 130)
t.goto(-100, 100)
t.goto(0, 0)

# Nível Médio - contorno + arestas principais + detalhes (passos 4 a 6)

#arestas principais
t.pensize(4)
t.goto(100, 100)
t.goto(-100, 100)
t.goto(50, 100)
t.home()
t.goto(-50, 100)
t.home()

#detalhes
t.pensize(3)
t.goto(-50, 100)
t.goto(-30, 120)
t.goto(0, 130)
t.goto(30, 120)
t.goto(50, 100)

#Nível Difícil - contorno + arestas principais + detalhes + detalhes finos em diante (passos 7 a 12)
 
#detalhes finos
t.pensize(2)
 
##lateral direito
t.penup()
t.home()
t.pendown()
t.goto(20, 40)
t.goto(70, 100)
t.goto(10, 10)
t.goto(80, 100)
 
##lateral esquerdo
t.penup()
t.home()
t.pendown()
t.goto(-20, 40)
t.goto(-70, 100)
t.goto(-10, 10)
t.goto(-80, 100)
 
##superior esquerdo
t.goto(-72, 121)
t.goto(-70, 100)
t.goto(-30, 120)
t.goto(-50, 130)
 
##superior direito
t.penup()
t.goto(80, 100)
t.pendown()
t.goto(72, 121)
t.goto(70, 100)
t.goto(30, 120)
t.goto(50, 130)
 
##central
t.penup()
t.goto(20, 40)
t.pendown()
t.goto(0, 100)
t.goto(-20, 40)
 
##superior central
t.goto(0, 100)
t.goto(30, 120)
t.goto(0, 100)
t.goto(-30, 120)
 
 
t.hideturtle()
turtle.done()