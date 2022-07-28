import turtle               
tw = turtle.Screen() 
tw.title("Stairs")       
moti = turtle.Turtle()       
moti.pensize(4)
moti.shape("turtle")
moti.speed()

#עיגולים בשורה
# moti.circle(50)
# moti.rt(10)
# moti.circle(50)
# moti.rt(10)
# moti.circle(50)
# moti.rt(10)
# moti.circle(50)

#פרח
# for x in range(3):
#     moti.circle(50)
#     moti.rt(90)
   
# moti.circle(50)

#פרח מחליף צבעים
moti.color("red")
moti.circle(50)
moti.rt(90)
moti.color("blue")
moti.circle(50)
moti.rt(90)
moti.color("green")
moti.circle(50)
moti.rt(90)
moti.color("black")
moti.circle(50)
moti.rt(90)

turtle.mainloop()   