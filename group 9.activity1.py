import turtle

# Function to set position without leaving a trace
def setPos(turtle, x, y):
    turtle.goto(x, y)
    

# Function to draw a hexagon
def hexagon(turtle,x,y, hexa_color, border_color):
    setPos(turtle,x,y)
    turtle.penup
    turtle.color(border_color, hexa_color)
    turtle.goto(50,-50)
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)
    turtle.end_fill()


# Function to draw a square
def square(turtle,x,y, square_color, border_color):
    setPos(turtle,x,y)
    turtle.penup
    turtle.color(border_color, square_color)
    turtle.goto(110,-140)
    turtle.begin_fill()
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.end_fill()

# Function to draw a circle
def circle(turtle, x, y, circle_color, border_color):
    turtle.up()
    turtle.color(border_color, circle_color)
    turtle.begin_fill()
    turtle.circle(45)
    turtle.end_fill()


# Function to draw the pattern
def pattern(turtle,x,y, hexa_color, circle_color, square_color, border_color):
    hexagon(turtle, x,y,hexa_color, border_color)
    setPos(turtle, 0, -60)
    circle(turtle,x,y, circle_color, border_color)
    setPos(turtle, 0, -180)
    square(turtle, x,y, square_color, border_color)

# Main function to draw the diagram
def main():
    turtle_obj = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=400, height=400)
    turtle_obj.speed(0)  
    pattern(turtle_obj, 0,0 , "yellow", "green", "red", "black")

    turtle.done()

main()