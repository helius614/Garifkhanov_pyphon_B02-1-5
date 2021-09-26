import turtle
turtle.shape('turtle')

#Правильные многоугольники
import math
def drnang(n, d):
    for _ in range(n):
        turtle.forward(d)
        turtle.left(360/n)
turtle.left(150)
r=20
n=3
d=2*r*math.sin(math.pi/n)
for n in range (3, 11, 1):
    drnang(n, d)
    turtle.penup()
    turtle.right(90+180/n)
    turtle.forward(10)
    turtle.left(90+180/(n+1))
    turtle.pendown()
    r=r+10
    d = 2 * r * math.sin(math.pi / n)