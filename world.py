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
#sand
t.color("brown")
for i in range (75):
    x=random.randint(-800,750)
    y=random.randint(-600,-300)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot (5)
#pyramid
t.width(3)
t.setheading(0)
t.penup()
t.goto(-600,-300)
t.pendown()
for x in range (3):
    t.forward(200)
    t.left(120)
    
t.mainloop()