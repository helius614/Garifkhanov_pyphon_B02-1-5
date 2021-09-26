import turtle
turtle.shape('turtle')

#Цветок
n=6
for _ in range (n//2):
    turtle.circle(50)
    turtle.circle(-50)
    turtle.right(360/n)
#или, чтобы можно было рисовать сколько угодно окружностей:
#n=6
#for _ in range (n/2):
#    turtle.circle(50)
#    turtle.right(360/n)