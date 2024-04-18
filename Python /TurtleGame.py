import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Initialize score
score = 0

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, -250)

# Set the player's speed
player_speed = 15

# Create the enemy turtles
enemies = []

for _ in range(5):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

# Set the enemy speed
enemy_speed = 2

# Define the player's movement functions
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 290:
        x = 290
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Create the score display turtle
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Instructions display
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.color("black")
instructions.goto(0, 230)
instructions.write("Use the left and right arrow keys to move the turtle.", align="center", font=("Courier", 14, "normal"))

# Main game loop
while True:
    for enemy in enemies:
        y = enemy.ycor()
        y -= enemy_speed
        enemy.sety(y)

        # Check for collision with player
        if enemy.distance(player) < 20:
            player.hideturtle()
            enemy.hideturtle()
            screen.bgcolor("red")
            screen.update()
            break

        # Check if enemy is out of bounds
        if enemy.ycor() < -300:
            x = random.randint(-290, 290)
            y = random.randint(100, 250)
            enemy.goto(x, y)
            # Increase the score when an enemy passes the player
            score += 1
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    screen.update()
