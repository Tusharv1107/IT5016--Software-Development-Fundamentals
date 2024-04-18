# Import required libraries
import turtle as t
import random

# Set up the screen
screen = t.Screen()
screen.bgcolor("black")
screen.setup(1200, 800)
screen.title("Circle-circle-circles")
screen.colormode(255)

# Create a turtle object
c = t.Turtle()

# Function to generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Function to draw a mandala
def drawMandala(gapsize):
    numOfCircles = 0
    while numOfCircles < (360/gapsize):
        # Draw an extra line after every 36 circles
        if numOfCircles % 36 == 0 and numOfCircles != 0:
            c.penup()
            c.forward(300)
            c.pendown()
        # Set turtle speed and color
        c.speed("fastest")
        c.color(random_color())
        # Draw two circles with a gap in between
        c.circle(100)
        c.setheading(c.heading() + gapsize)
        c.circle(100)
        numOfCircles += 1
        
# Call the function to draw the mandala
drawMandala(5)

# Keep the window open until clicked
screen.exitonclick()
