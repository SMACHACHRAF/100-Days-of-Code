import turtle as t
import random
t.Turtle()

color_list = [
    (242, 235, 211), (236, 159, 68), (221, 72, 95), (41, 122, 185), (231, 89, 19), (94, 205, 153),
    (250, 226, 90), (205, 61, 24), (180, 73, 180), (126, 47, 99), (59, 45, 15), (22, 156, 232),
    (109, 213, 239), (45, 92, 52), (252, 144, 176), (38, 48, 98), (193, 146, 237), (72, 80, 220),
    (128, 216, 229), (253, 165, 23), (249, 59, 41), (87, 70, 221), (242, 198, 41), (20, 34, 76),
    (175, 35, 12), (63, 12, 64), (180, 103, 53)
]

random_color = (random.choice(color_list))
t.colormode(255)
t.penup()
t.speed("fastest")
t.hideturtle()


def left_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(0)


def right_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(180)


for _ in range(5):
    for _ in range(10):
        t.dot(20, (random.choice(color_list)))
        t.setheading(180)
        t.forward(50)
    left_up()
    for _ in range(10):
        t.forward(50)
        t.dot(20, (random.choice(color_list)))
    right_up()


screen = t.Screen()
screen.exitonclick()
