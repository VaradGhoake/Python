import turtle as t

a = t.Turtle()
a.pencolor("white")
a.setposition(-300,0)
a.pencolor("blue")

b = t.Turtle()
b.pencolor("white")
b.setposition(-300, 0)
b.pencolor("red")

a.left(45)
b.right(45)
length = 5

a.speed(7)
b.speed(9)

def left(x, length):
    x.forward(length)
    x.right(90)
    x.forward(length)

def right(x, length):
    x.forward(length)
    x.left(90)
    x.forward(length)

for i in range(1, 15):
    if(i%2!=0):
        left(a, length)
        right(b, length)
        length = length + 5
    else:
        right(a, length)
        left(b, length)
        length = length = length + 5

t.done()
