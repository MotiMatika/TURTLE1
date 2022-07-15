import turtle               
tw = turtle.Screen()        
moti = turtle.Turtle()                    
moti.pensize(4) 
moti.speed(1)
moti.shape("classic")

#הריבוע
def num_1(size):
    moti.color("green")
    moti.begin_fill()
    moti.fd(size)
    moti.rt(90)
    moti.fd(size)
    moti.rt(90)
    moti.fd(size)
    moti.rt(90)
    moti.fd(size)
    moti.end_fill()
num_1(100)

def num_2(size):
    moti.color("red")
    moti.begin_fill()
    moti.fd(size)
    moti.rt(90)
    moti.fd(size)
    moti.rt(90)
    moti.fd(size)
    moti.rt(90)
    moti.fd(size)
    moti.end_fill()
num_2(100)

def num_3(size):
    moti.color("blue")
    moti.begin_fill()
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.end_fill()
num_3(100)

def num_4(size):
    moti.color("purple")
    moti.begin_fill()
    moti.rt(90)
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.end_fill()
num_4(100)

def num_5(size):
    moti.color("pink")
    moti.begin_fill()
    moti.rt(90)
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.end_fill()
num_5(100)




def main():
    import turtle               
    tw = turtle.Screen()        
    moti = turtle.Turtle()                    
    moti.pensize(4) 
    moti.speed(1)
    moti.shape("classic")
    size = 100

    
    num_1(size)
    num_2(size)
    num_3(size)
    num_4(size)
    num_5(size)
    

turtle.mainloop()            