import turtle

class Box(turtle.Turtle):
    def __init__(self, x, y, w,h):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x, y) # posição inicial da raquete
        self.shapesize(w,h) #tamanho da raquetinha

    def up(self):
        self.sety(self.ycor() +(self.ycor() < 220) *  20)

    def dw(self):
        self.sety(self.ycor() - (self.ycor() > -220) * 20)


class Bol(Box):
    def __init__(self, x, y, w, h):
        Box.__init__(self, x, y, w, h)
        self.pcy = 0
        self.bx = 0
        self.by = 0
        self.vx = 1
        self.vy = 1

    def update(self):
        self.bx  += self.vx
        self.by  += self.vy
        bol.goto(self.bx, self.by)
        pc.goto(pc.xcor(), self.pcy)
        if self.bx >= pc.xcor() -30: 
            self.vx *= -1
        if self.bx <= hm.xcor() +30 and self.by < hm.ycor() + 100 and self.by > hm.ycor() -100:
            self.vx *= -1
        if self.bx < hm.xcor():
            self.vx *= -1
            self.bx = 0
        if self.by >= 280 or self.by <= -280:
            self.vy *= -1

        if self.bx > 20:
            if pc.ycor() < self.by and self.pcy < 220:
                self.pcy += 1
            if pc.ycor() > self.by and self.pcy > -220:
                self.pcy -= 1




hm = Box(-350, 0, 8, 1)
pc = Box(350, 1, 8, 1)
bol = Bol(0, 0, 2, 2)






win = turtle.Screen()
win.title('Pong')
wn = turtle.Turtle()
win.bgcolor('black')
win.setup(width=800, height= 600)
win.tracer(0)


win.listen()
win.onkeypress(hm.up,"Up")
win.onkeypress(hm.dw,"Down")


while True:
    win.update()
    bol.update()



