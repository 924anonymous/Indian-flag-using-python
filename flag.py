import turtle
tr=turtle.Turtle()
tr.speed(5)
for i in range(24):
    tr.forward(50)
    tr.penup()
    tr.setposition(0,0)
    tr.right(15)
    tr.pendown()

tr.setposition(0,-50)
tr.circle(50)
tr.penup()

tr.setposition(-500,130)
tr.pendown()
tr.fillcolor("orange")
tr.begin_fill()
tr.forward(1000)
tr.left(90)
tr.forward(300)
tr.left(90)
tr.forward(1000)
tr.left(90)
tr.forward(300)
tr.end_fill()
tr.penup()


tr.setposition(-500,-130)
tr.pendown()
tr.fillcolor("green")
tr.begin_fill()
tr.right(270)
tr.forward(1000)
tr.right(90)
tr.forward(300)
tr.right(90)
tr.forward(1000)
tr.right(90)
tr.forward(300)
tr.end_fill()
tr.penup()
    
      
turtle.done()


    
