import turtle
    #(1) Draws a Sqaure
def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)
draw_square()
    #(2) Draws a Circle
def draw_circle():
    circ =turtle.Turtle()
    circ.shape("arrow")
    circ.color("red")
    circ.circle(100)
draw_circle()
    #(3) Draws a Triangle
def draw_triangle():
    triang = turtle.Turtle()
    triang.shape("triangle")
    triang.color("black")

    for i in range(0,4):
        triang.backward(120)
        triang.left(120)
       
draw_triangle()
   
