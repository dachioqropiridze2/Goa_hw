from turtle import*

#we want to paint a house

#step 1: draw a square

speed(30)



width(7)
color("purple")
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
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()

goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill( )

color("purple")
penup()

goto(200, 120)
pendown()

left(30)
forward(30)


color("blue")
right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)
right(90)

penup()
goto(200, 120)
pendown()


forward(60)

penup()
goto(120, 200)

left(40)
forward(160)
left(50)
forward(5)
pendown()

color("blue")
left (90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)


left(90)
forward(30)
left(90)
forward(60)
left(180)
forward(30)
left(90)
forward(30)
left(180)
forward(60)


penup()
left(180)
goto(200, 200)
right(90)
forward(53)
right(90)
forward(30)
left(90)
pendown()


forward(60)












exitonclick()