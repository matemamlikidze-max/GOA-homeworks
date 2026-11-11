from turtle import *

#we want to paint a house

#step 1:   draw a square
speed(30)
width(8)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(75)
color("purple")
left(90)
forward (122)    #height of the door
right(90)
forward(60)
right(90)
forward(122)
end_fill()
penup()
goto(200, 200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

begin_fill()
color("brown")
left(30)
forward(40)
right(269)
forward(50)
left(-90)
forward(45)
left(-90)
forward(50)
end_fill()
penup()
goto(200, 200)
pendown()

begin_fill()
left(90)
forward(35)
left(269)
forward(50)
left(90)
forward(45)
right(-90)
forward(50)
end_fill()


exitonclick()