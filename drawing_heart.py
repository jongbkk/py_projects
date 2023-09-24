import turtle


def draw_heart():
    turtle.speed(2)

    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    turtle.begin_fill()
    turtle.color('orange', 'red')

    turtle.left(140)
    turtle.forward(224)

    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)

    turtle.left(120)

    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)

    turtle.forward(224)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()


draw_heart()
