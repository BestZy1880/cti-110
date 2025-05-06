# Zykria Best
# 04/05/25
# P4LAB1b (Turtle draws my initials) 

import turtle

# Setup
win = turtle.Screen()
win.bgcolor("white")
t = turtle.Turtle()

# Style
t.pensize(5)
t.pencolor("blue")
t.shape("turtle")
t.speed(2)

# ---------- Draw "Z" ----------
t.penup()
t.goto(-150, 100)
t.setheading(0)
t.pendown()
t.forward(100)

t.right(135)
t.forward(140)

t.left(135)
t.forward(100)

# ---------- Draw "B" ----------
# Spine
t.penup()
t.goto(55, 100)
t.setheading(270)
t.pendown()
t.forward(100)

# Top bump
t.penup()
t.goto(55, 100)
t.setheading(40)
t.pendown()
t.circle(-33, 260)  # Arc left to right

# Bottom bump
t.penup()
t.goto(50, 45)
t.setheading(50)
t.pendown()
t.circle(-37, 270)

# Finish
t.hideturtle()
win.mainloop()
