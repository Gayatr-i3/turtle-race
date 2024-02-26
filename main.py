from turtle import Turtle, Screen
import random

is_race_on=False
s=Screen()
s.setup(width=600, height=500)
user_bet = s.textinput(title="make your bet", prompt="which turtle will win?")
colors = ["orange", "blue", "yellow", "red", "purple", "green"]
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-280, y=y[i])
    all_turtles.append(t)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
         if turtle.xcor() > 280:
             is_race_on = False
             winning_turtle = turtle.pencolor()
             if winning_turtle == user_bet:
                 print(f"you have won!")
             else:
                 print(f"you have lost")
         rand_distance=random.randint(0, 10)
         turtle.forward(rand_distance)


s.exitonclick()