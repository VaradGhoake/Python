import turtle as t

t.title("Colors")

a = t.Turtle()

a.speed(1)

a.pencolor("red")
for i in range(50):
    a.forward(50)
    a.left(123)

a.forward(35)
a.pencolor("blue")
for i in range(50):
    a.forward(100)
    a.left(123)

a.forward(60)
a.pencolor("green")
for i in range(50):
    a.forward(150)
    a.left(123)

a.right(180)
a.forward(20)
a.pencolor("black")
for i in range(75):
    a.forward(250)
    a.left(123)

t.done()
