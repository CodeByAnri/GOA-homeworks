from turtle import *


#we want to paint a house

#step 1: draw a squeare

begin_fill()
speed(30)

color("Orange")
forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
end_fill()

# -- --

#step 2: draw a door

begin_fill()
forward(70)
color("Brown")
left(90)
forward(120) #Door Height
right(90)
forward(60)
right(90)
forward(120)
end_fill()

# -- --

#step 3: draw a roof

penup()
goto(200, 200)
pendown()


begin_fill()
color("Maroon")
right(150)
forward(200)

left(120)
forward(200)
end_fill()

# -- --

#step 4: draw 2 windows

# 1st Window
width(4)

penup()
goto(15, 135)
pendown()

color("Gray")
left(120)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

# 2nd Window

penup()
goto(135, 135)
pendown()

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

# -- --

# 1st Glass

width(1)

begin_fill()
penup()
goto(16, 137)
pendown()

color("Cyan")
left(90)
forward(47)

left(90)
forward(47)

left(90)
forward(47)

left(90)
forward(47)
end_fill()

# 2nd Glass

begin_fill()
penup()
goto(136, 137)
pendown()

left(90)
forward(47)

left(90)
forward(47)

left(90)
forward(47)

left(90)
forward(47)
end_fill()

# -- --

# 1st Frame

width(3)
penup()
goto(40, 185)
pendown()

color("Gray")
forward(50)

penup()
goto(15, 160)
pendown()

left(90)
forward(50)

# 2nd Frame

penup()
goto(160, 185)
pendown()

right(90)
forward(50)

penup()
goto(135, 160)
pendown()

left(90)
forward(50)

# -- --

# Grass


penup()
goto(-10000, -10000)
pendown()


color("Green")
begin_fill()
forward(20000)

left(90)
forward(10000)

left(90)
forward(20000)

left(90)
forward(10000)
end_fill()

# -- --

# Sky

width(1)
penup()
goto(10000, 0)
pendown()

color("Blue")

left(180)
forward(10000)

left(90)
forward(20000)

left(90)
forward(10000)

left(90)
forward(10000)

left(90)
forward(200)

begin_fill()
right(30)
forward(200)

right(120)
forward(200)

right(30)
forward(200)

left(90)
forward(9800)

left(90)
forward(10000)

left(90)
forward(20000)

left(90)
forward(10000)

left(90)
forward(10000)

end_fill()

# -- --

# Stars

begin_fill()

width(7)
color("Yellow")
penup()
goto(-200, 300)
pendown()


left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

penup()
goto(-100, 280)
pendown()


left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

penup()
goto(-350, 250)
pendown()


left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

penup()
goto(-380, 350)
pendown()


left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

penup()
goto(-225, 175)
pendown()


left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

penup()
goto(-400, 120)
pendown()


left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

penup()
goto(-100, 110)
pendown()


left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

left(90)
forward(5)

# -- --

# Sun

begin_fill()
penup()
goto(400, 270)
pendown()


left(90)
forward(100)

left(90)
forward(100)

left(90)
forward(100)

left(90)
forward(100)
end_fill()

exitonclick()