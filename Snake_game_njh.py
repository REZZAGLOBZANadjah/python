
# REZZAG LOBZA Nadjah 10/07/2019
#rezzaglobza7@gmail.com
# source   https://www.youtube.com/watch?v=Vi0AhyUCCkE&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ&index=7
import os
import random
import turtle
import time
#import keyboard 

delay = 0.1
# score
score = 0
high_score = 0


#set up the screen

wn = turtle.Screen()
wn.title("Snake Game @Nadjah")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)   # turns off the screen updates

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score :0  High score : 0 ", align="center", font=("Courier", 24, "normal"))


# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#keyboard bindings
# controle the game with  letters "u,d,l,r"
"""
wn.listen()
wn.onkeypress(go_up, "u")
wn.onkeypress(go_down, "d")
wn.onkeypress(go_left, "l")
wn.onkeypress(go_right, "r")
"""

# -----------------------------------------------------------

# contole the game with keys up down left right --> <--
wn.listen()
wn.onkey(lambda: go_right(), 'Right')
wn.onkey(lambda: go_left(), 'Left')
wn.onkey(lambda: go_up(), 'Up')
wn.onkey(lambda: go_down(), 'Down')
#move()
#done()
# -----------------------------------------------------------


# Main game loop
while True:
    wn.update()
    # check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segment list
        segments.clear()

        # reset the score
        score = 0
        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("score : {} High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # check for a collision with the food

    if head.distance(food) < 20:
        # move the food to random spot

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

        # Move the end segments first in revers order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move the segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collision with the border
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment list
            segments.clear()

            # reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("score : {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)
wn.mainloop()
#------------
