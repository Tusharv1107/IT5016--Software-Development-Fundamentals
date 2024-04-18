from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("Triangle")
timmy.color("")

tommy = Turtle()
tommy.shape("turtle")
tommy.color("")


def drawSquare(x):
    x.forward(400)
    x.left(90)
    x.forward(400)
    x.left(90)
    x.forward(400)
    x.left(90)
    x.forward(400)
    x.left(90)
    
def drawTriangle(x):
    x.left(120)
    x.forward(200)
    x.left(120)
    x.forward(200)
    x.right(120)
    x.forward(200)
    
drawSquare(timmy)
tommy.penup()
tommy.backward()