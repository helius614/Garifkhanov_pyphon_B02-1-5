import turtle
turtle.shape('turtle')

#Спираль
for n in range(10000):
    turtle.forward(n/1000)
    turtle.left(1)