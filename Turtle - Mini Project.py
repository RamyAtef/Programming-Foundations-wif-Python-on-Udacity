        #Draw Flower
import turtle
    
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():    
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    #Create the turtle Brad - Draws a Sqaure
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(20)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
        #to draw last line it down
    brad.right(90)
    brad.forward(350)
    
draw_art()
