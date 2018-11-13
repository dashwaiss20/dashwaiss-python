import turtle
turtle.title('YEET')
pen = turtle.Pen()
black_color = (0.0, 0.0, 0.0)
white_color = (1.0, 1.0, 1.0)
red_color = (1.0, 0.0, 0.0)
green_color = (0.0, 1.0, 0.0)
blue_color = (0.0, 0.0, 1.0)
hex_color = "#ffe063"
turtle.bgcolor(black_color)
pen.goto(-50,0)
pen.color('red')
pen.forward(100)
pen.up()

pen.goto(-100,-100)
pen.color(hex_color)
pen.down()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)

pen.up()
pen.goto(-300,0)
pen.down()
pen.color(white_color)
pen.circle(300)
pen.up()

pen.color(green_color)
pen.goto(-200,-135)
pen.down()
pen.right(270)
pen.forward(400)
pen.left(120)
pen.forward(400)
pen.left(120)
pen.forward(400)

turtle.exitonclick()



