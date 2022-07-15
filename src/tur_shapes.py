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


def num_6(size):
    moti.color("pink")
    moti.begin_fill()
    moti.rt(90)
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.lt(90)
    moti.fd(size)
    moti.end_fill()
num_6(100)

def main():
    import turtle               
    tw = turtle.Screen()        
    moti = turtle.Turtle()                    
    moti.pensize(4) 
    moti.speed(1)
    moti.shape("classic")

    
    num_1()
    num_2()
    num_3()
    num_4()
    num_5()
    num_6()

turtle.mainloop()            