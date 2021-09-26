import turtle
turtle.shape('turtle')

#Бабочка
turtle.left(90)
n=10
r=20
k=1
for _ in range (n):
    turtle.circle(r)
    turtle.circle(-r)
    r=r+n*k