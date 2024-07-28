from turtle import *

#drowing a house
width(5)
speed(5)
#body
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
color("purple")
end_fill()


penup()
goto(200,200)
pendown()


#roof
color("blue")
begin_fill()
right(90)
right(45)
forward(141)
left(90)
forward(141)
end_fill()

penup()
goto(75,0)
pendown()
#door
color("green")
begin_fill()
right(135)
forward(75)
right(90)
forward(50)
right(90)
forward(75)
end_fill()

penup()
goto(20,180)
pendown()

#window1
color("yellow")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()  


penup()
goto(180,180)
pendown()


#window2
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()
    