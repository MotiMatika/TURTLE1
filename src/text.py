
import turtle               
tw = turtle.Screen() 
tw.title("Text")       
moti = turtle.Turtle()       
moti.pensize(4)
moti.shape("turtle")
moti.speed(1)
tw.bgcolor("gold")

moti.write("hi",move=False,font=("ariel",50,"normal"))
moti.up()
#moti.fd(25)
moti.rt(45)
moti.backward (25)
moti.pendown()
moti.circle(70)
turtle.mainloop()       