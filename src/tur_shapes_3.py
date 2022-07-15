

#התכנית מקבלת מספר.אם הוא כפולות 3 היא משרטטת מעגל סגול בקוטר של הקלט,
# אחרת היא משרטטת קו כחול באורך של הקלט
num = int(input("enter :  "))

if num % 3 == 0:
    import turtle 
    tw = turtle.Screen()
    tw.title("hello")
    moti = turtle.Turtle()
    moti.pensize(4)
    moti.speed(1)
    moti.shape("classic")   
    moti.color("purple")
    moti.circle(num)
    turtle.mainloop()
else:
    import turtle 
    tw = turtle.Screen()        
    moti = turtle.Turtle()                    
    moti.pensize(4) 
    moti.speed(1)
    moti.shape("classic") 
    moti.color("blue") 
    moti.fd(num)  
    turtle.mainloop()  
    