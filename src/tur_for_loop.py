
import turtle               
tw = turtle.Screen()        
moti = turtle.Turtle()       
moti.pensize(4)
moti.shape("turtle")
moti.speed()
    

# #שרטוט צורות משוכללות ברצף באופן יעיל עם לולאת פור
# #משולש שוה צלעות
# for num in range(3):
#     moti.fd(100)
#     moti.rt(120)
# #ריבוע
# for num in range(4):
#     moti.fd(100)
#     moti.rt(90)
# #מחומש
# for num in range(5):
#     moti.fd(100)
#     moti.rt(72)
# #משושה
# for num in range(6):
#     moti.fd(100)
#     moti.rt(60)    

# turtle.mainloop()


#שרטוט צורות משוכללות ברצף צבועות באופן יעיל עם לולאת פור
# משולש שוה צלעות מלא
moti.begin_fill()
moti.color("green")
for num in range(3):
    moti.fd(100)
    moti.rt(120)
moti.end_fill()    

# #ריבוע
moti.begin_fill()
moti.color("red")
for num in range(4):
    moti.fd(100)
    moti.rt(90)
moti.end_fill()
#מחומש

moti.begin_fill()
moti.color("blue")
for num in range(5):
    moti.fd(100)
    moti.rt(72)
moti.end_fill()
#משושה

moti.begin_fill()
moti.color("pink")
for num in range(6):
    moti.fd(100)
    moti.rt(60)    
moti.end_fill()
turtle.mainloop()