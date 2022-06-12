import turtle
turtle.Screen().clear()
turtle.speed(0)
turtle.pensize(2)
  # função da espiral
  
colors = ['red', 'green', 'orange', 'violet', 'yellow', 'blue', 'magenta', 'cyan']
def Spiral (length, angle, step, min_length):
    while(length > min_length ):
        turtle.color(colors[length % 8])
        turtle.fd(length)
        turtle.lt(angle)
        length = length - step
        
Spiral(length= 250, angle=89, step=1, min_length= 32)
 
turtle.done()
