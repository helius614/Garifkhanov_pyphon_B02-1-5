import turtle
turtle.shape('turtle')

#Звезда
l=200
n=5
def star(n, l):
    for _ in range (n):
        turtle.forward(l)
        turtle.right(180 - 180/n)

star(n,l)
turtle.penup()
turtle.goto(-1.5*l, 0)
n=11
turtle.pendown()
star(n, l)