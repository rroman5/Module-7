#Roberto Roman
#11-07-21

#Problem 5
#Importing module
import turtle
# draws square when making the first box
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("Blue")
size = 50
x = 0
y = 0
for i in range(5):
    drawSquare(alex, size)
#Size is increasing + 10 in order to grow
    size = size + 10
    x = x - 5
    y = y - 5
#after loop is done pen up is used to stop the loop
    alex.penup()
    alex.setposition(x, y)
#Pen down to start again the loop but with different coordinates
    alex.pendown()

wn.exitonclick()