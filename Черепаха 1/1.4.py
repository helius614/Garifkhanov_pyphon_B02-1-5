import turtle
turtle.shape('turtle')

#Павук
turtle.forward(100)
turtle.left(180)
turtle.forward(100)
turtle.left(180)
n=10
for _ in range (1, n, 1):
    turtle.left(360/n)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180)