import turtle

# Turtle works with the concept of a virtual pen.  You move the
# pen around the screen and draw where the pen is 'pointing'.
# Turtle can also draw circles and a few more shapes - but mostly
# you draw by moving the virtual pen around the screen.

# Just like a real pen, you can by putting the pen 'down'
# and moving it - and picking it 'up' when you don't want to draw.

# By default, Turtle will draw an arrow at the current position
# that points in the drawing direction.  You can also hide this
# arrow if you don't want to include it in your drawing.

# To create a pen and show it in the default position (centered), you'd
# just write.
pen = turtle.Pen()

# To see what you can do with some simple commands,
# try to visualize what this method does.



# Can you tell? Uncomment below to see.
#mystery_drawing_one(90)

# Imagine a slight change to the last - what if we change the angle
# by 91 deg. instead of 90.
#mystery_drawing_one(91)

# You can also set the pen color.
#pen.pencolor("red")
#mystery_drawing_one(91)

# Turtle has some built in named colors you would expect, like
# red, blue, green etc..
# You can also create your own colors using web style 'hex' colors
# or using RGB colors.

# RGB stands for Red, Green, Blue and its created by 'mixing' values
# for each of those 3 base colors where each base can be a
# number from 0.0 to 1.0.
red_color = (1.0, 0.0, 0.0)
black_color = (0.0, 0.0, 0.0)
blue_color = (0.0, 0.0, 1.0)
white_color = (1.0, 1.0, 1.0)
green_color = (0.0, 1.0, 0.0)

# Use like so:
#pen.pencolor(blue_color)
#mystery_drawing_one(91)

# Note that Turtle doesn't really have a 'color' object.  You would
# create and store colors as I did above - with a tuple of 3 integers
# or a hex string color. (See below for more on color).
#pen.pencolor(hex_color)



# Additional Turtle Info
#
# Specify a screen size and/or start positn
#turtle.setup(width=600, height=500)

# Moving the pen
turtle.bgcolor(black_color)
turtle.color('red')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(200,100)
turtle.color(white_color)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.color(blue_color)
turtle.goto(200,250)
turtle.pendown()
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.color(green_color)
turtle.goto(100,-250)
turtle.pendown()
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.color(blue_color)



# turtle.goto(10, 10)
# turtle.setpos(10, 10) # same as goto()

# Move the arrow/turtle back to the beginning (origin)
# turtle.home()

# Clear the screen and return to the origin
# turtle.reset()

# Hide/show the arrow (turtle) while printing
# turtle.hideturtle()
# turtle.showturtle()

# Set drawing (animation) speed; 0 means no animation
# turtle.setspeed(0)

# Get screen size info
# turtle.window_height()
# turtle.window_width()

# Set a title
turtle.title("Turtle Project")

turtle.exitonclick()


# 1) Use a different background color for the screen.  Try red, blue and black.
# 2) Draw a 2 squares and 2 rectangle.
# 2a) Make one of each filled and one 'empty' or not filled.
# 2b) Use different colors for the fill and border or lines


