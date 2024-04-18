## Spiral Pattern with Turtle
This Python script uses the Turtle module to draw a spiral pattern. It creates a turtle object, sets the pen size and speed, and then draws a spiral pattern by repeating a set of movements.

## Usage
To run the script, ensure you have Python installed on your system. Then, follow these steps:
- Open a terminal or command prompt.
- Navigate to the directory containing the script.
- Run the script by executing the command: python your_script_name.py

## Dependencies
This script requires the Turtle module, which is a part of the Python standard library and should be available by default in most Python installations.

## Programming principle 
Discuss some programming principles and concepts involved:
•	Turtle Graphics Module: The code utilizes the turtle module, which provides a simple way to create graphics and drawings using a turtle metaphor. A turtle can move around the screen and draw lines as it moves.
•	Object-Oriented Programming (OOP): The code uses object-oriented principles. It creates a Turtle object named my_turtle using the turtle.Turtle() constructor. This object represents the drawing turtle and provides methods to control its movement and drawing.
•	Loops: Two nested for loops are used. The outer loop (for i in range(36)) repeats 36 times, controlling the number of iterations for the spiral pattern. The inner loop (for _ in range(4)) repeats four times, controlling the number of sides for each polygon drawn in the spiral.
•	Turtle Movement: Inside the nested loops, my_turtle.forward(100) moves the turtle forward by 100 units, and my_turtle.right(80) turns the turtle right by 80 degrees. This combination of movement and rotation creates the spiral pattern.
•	Code Comments: Comments (#) are used to provide explanations for different parts of the code. This is a good practice for enhancing code readability and understanding.
•	Function Calls: my_turtle.pensize(2) sets the width of the turtle's pen to 2 units, and my_turtle.speed(0) sets the drawing speed to the maximum value (0 means fastest). These function calls demonstrate how to configure the turtle's appearance and behavior.
•	Code Organization: The code is organized into logical sections, with each section responsible for a specific aspect of the program, such as initializing the turtle, setting parameters, and drawing the pattern.
