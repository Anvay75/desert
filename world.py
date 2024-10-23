import turtle as t 
import random
t.speed(100)
t.bgcolor("light blue")
#ground
t.color("yellow")
t.begin_fill()
t.penup()
t.goto (-800,-300)
t.pendown()
t.forward(1550)
t.right(90)
t.forward(300)
t.right(90)
t.forward(1550)
t.right(90)
t.forward(300)
t.end_fill()
"""
#sand
t.color("brown")
for i in range (75):
    x=random.randint(-800,750)
    y=random.randint(-600,-300)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot (5)
"""
#pyramid
t.width(3)
t.color("brown","yellow")
t.begin_fill()
t.setheading(0)
t.penup()
t.goto(-600,-300)
t.pendown()
for x in range (3):
    t.forward(200)
    t.left(120)
t.end_fill()





#pyramid strips
t.penup()
t.goto(-550,-220)
t.pendown()
t.setheading(0)
t.forward(100)

# cactus 
t.penup()
t.goto(-60,-202)
t.pendown()
t.color("brown","green")
t.begin_fill()
t.setheading(90)
t.forward(100)
t.setheading(0)
t.circle(50,180)
t.setheading(90)
t.forward(45)
t.circle(50,180)
t.setheading(270)
t.forward(265)
t.end_fill()

#sand dune 
t.penup()
t.goto(0,-300)
t.pendown()
t.setheading(90)
t.color("brown","yellow")
t.begin_fill()
t.circle(100,180)
t.end_fill()

# sun
t.penup()
t.goto(-260,400)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range (36):
    t.forward(100)
    t.right(100)
t.end_fill()





t.mainloop()