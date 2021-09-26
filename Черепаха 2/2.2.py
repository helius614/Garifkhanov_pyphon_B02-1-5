import turtle as t
t.shape('turtle')

#Почтовый индекс
X=[0, 20, 30, 50, 60, 80, 90, 110, 120, 140, 150, 170]
Y=[0, -20, -40]
t.penup()
t.goto(X[0],Y[1])
t.pendown()
t.goto(X[1],Y[0])
t.goto(X[1],Y[2])

t.penup()
t.goto(X[2],Y[0])
t.pendown()
t.goto(X[2],Y[1])
t.goto(X[3],Y[1])
t.goto(X[3],Y[0])
t.goto(X[3],Y[2])

t.penup()
t.goto(X[4],Y[1])
t.pendown()
t.goto(X[5],Y[0])
t.goto(X[5],Y[2])

t.penup()
t.goto(X[6],Y[0])
t.pendown()
t.goto(X[7],Y[0])
t.goto(X[6],Y[1])
t.goto(X[6],Y[2])

t.penup()
t.goto(X[8],Y[0])
t.pendown()
t.goto(X[8],Y[2])
t.goto(X[9],Y[2])
t.goto(X[9],Y[0])
t.goto(X[8],Y[0])

t.penup()
t.goto(X[10],Y[0])
t.pendown()
t.goto(X[10],Y[2])
t.goto(X[11],Y[2])
t.goto(X[11],Y[0])
t.goto(X[10],Y[0])

t.done()
