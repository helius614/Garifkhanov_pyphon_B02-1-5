import turtle as t
t.shape('turtle')

#Броуновское движение
from random import *
for _ in range (10000):
    t.forward(randint(5, 10))
    x=randint(1, 2)
    if x==1:
        t.left(randint(0, 180))
    else:
        t.right(randint(0, 180))