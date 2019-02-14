import turtle
import time

# Input colors
coloro1="#FF0800"
colori1="#D0FF14"
coloro2="#D0FF14"
colori2="#FF0800"
coloro3="#FF0800"
colori3="#D0FF14"
coloro4="#D0FF14"
colori4="#FF0800"

def draw_square():
    # draw a square
    window = turtle.Screen()
    window.bgcolor("black")


def draw_romboid(some_turtle,some_angle,some_length,color_outside,color_inside):
    some_turtle.color(color_inside)
    some_turtle.forward(some_length)
    some_turtle.color(color_outside)
    some_turtle.right(some_angle)
    some_turtle.forward(some_length)
    some_turtle.right(180-some_angle)
    some_turtle.forward(some_length)
    some_turtle.right(some_angle)
    some_turtle.color(color_inside)
    some_turtle.forward(some_length)
    some_turtle.right(180-some_angle)

def draw_First_flower():
    # FIRST FLOWER
    march.speed(200)
    march.shape("turtle")
    angle = 40
    length = 50
    for x in range(1, 37):
        # march.START_ORIENTATION
        march.right(10)
        draw_romboid(march, angle, length, coloro1, colori1)
    march.right(90)
    march.forward(200)
    march.pu()

def draw_Other_flower():
    # SECOND FLOWER

    april = turtle.Turtle()
    april.pu()
    april.setpos(150, 180)

    april.speed(200)
    april.shape("triangle")
    angle = 30
    length = 30
    april.pd()
    for x in range(1, 37):
        # march.START_ORIENTATION
        april.right(10)
        draw_romboid(april, angle, length, coloro3, colori3)
    april.right(90)
    april.forward(200)
    april.pu()

if __name__ == '__main__':
    march = turtle.Turtle()
    draw_square()
    draw_First_flower()
    draw_Other_flower()
    #march.onclick()
    time.sleep(5)
