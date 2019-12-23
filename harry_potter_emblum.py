from turtle import *
t = Turtle()
t.speed(80)
t.pensize(5)

# Move turtle to begin glasses
t.penup()
t.setpos(-30,-50)
t.left(90)

# Draw Harry Potter Glasses
t.pendown()
t.circle(57)
t.right(45)
t.circle(-50,90)
t.right(45)
t.circle(57)

# Move turtle to begin scar
t.penup()
t.setpos(-70,50)
t.left(200)

# Draw scar
t.pensize(2)
t.color("gold")
t.begin_fill()
t.pendown()
t.forward(60)
t.right(120)
t.forward(35)
t.left(120)
t.forward(90)
t.left(170)
t.forward(70)
t.right(110)
t.forward(35)
t.left(128)
t.forward(90)
t.end_fill()
t.penup()
t.setpos(-30,-400)

