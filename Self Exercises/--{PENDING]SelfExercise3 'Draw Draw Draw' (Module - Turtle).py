"""
Module 2 - TURTLE

“Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw all over it!
We can use functions like turtle.forward(…) and turtle.right(…) which can move the turtle around.

Method	      Parameter	     Description
Turtle()	  None	         Creates and returns a new turtle object
forward()	  amount	     Moves the turtle forward by the specified amount
backward()	  amount	     Moves the turtle backward by the specified amount
right()	      angle	         Turns the turtle clockwise
left()	      angle	         Turns the turtle counterclockwise
penup()	      None	         Picks up the turtle’s Pen
pendown()	  None	         Puts down the turtle’s Pen
up()	      None	         Picks up the turtle’s Pen
down()	      None	         Puts down the turtle’s Pen
color()	      Color name	 Changes the color of the turtle’s pen
fillcolor()   Color name	 Changes the color of the turtle will use to fill a polygon
heading()	  None	         Returns the current heading
position()	  None	         Returns the current position
goto()	      x, y	         Move the turtle to position x,y
begin_fill()  None	         Remember the starting point for a filled polygon
end_fill()	  None	         Close the polygon and fill with the current fill color
dot()	      None	         Leave the dot at the current position
stamp()   	  None	         Leaves an impression of a turtle shape at the current location
shape()	      shapename	     Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’

"""

import turtle
# window = turtle.Screen()
# tur = turtle.Turtle()

# window.title("Draw Draw Draw")
# window.bgcolor("black")
# tur.color("cyan")

#SQUARE
# for i in range(4):
#     tur.forward(100)
#     tur.right(90)
# turtle.done()


#RECTANGLE
# for i in range(2):
#     tur.forward(100)
#     tur.right(90)
#     tur.forward(40)
#     tur.right(90)
# turtle.done()


#STAR
# for i in range(5):
#     tur.forward(100)
#     tur.right(144)
# turtle.done()



# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)


