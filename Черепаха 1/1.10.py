import turtle
turtle.shape('turtle')

#Пружина
turtle.left(90)
R=20
r=5
n=10
for _ in range (n):
    turtle.circle(-R, 180)
    turtle.circle(-r, 180)