import turtle               
tw = turtle.Screen() 
tw.title("Stairs")       
moti = turtle.Turtle()       
moti.pensize(4)
moti.shape("classic")
moti.speed()

moti.lt(90)
for x in range(4):

    moti.fd(70)
    moti.lt(90)
    moti.fd(70)
    moti.rt(90)
moti.up()
moti.setx(0)
moti.sety(0)
moti.pd()

moti.rt(90)
for x in range(4):

    moti.fd(70)
    moti.lt(90)
    moti.fd(70)
    moti.rt(90)
moti.fd(70)

moti.rt(90)
moti.fd(350)
moti.rt(90)
moti.fd(630)
moti.rt(90)
moti.fd(350)

moti.goto(0,0)
moti.rt(90)
moti.fd(70)
moti.lt(45)
moti.fd(395.98)

turtle.mainloop()       