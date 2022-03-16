from decimal import Decimal as D
from decimal import getcontext
from turtle import *

def rectangle(width, height):
    for _ in range(2):
        forward(width)
        left(90)
        dot()
        forward(height)
        left(90)
        dot()

#rectangle(200, 100)

def triangle(side):
    for _ in range(3):
        forward(side)
        left(120)

#triangle(100)

def square(side):
    for _ in range(4):
        forward(side)
        left(90)
'''
for _ in range(3):
    square(100)
    left(20)'''

def four_squares(side):
    for _ in range(4):
        square(side)
        left(90)

'''four_squares(100)
right(45)
four_squares(100)'''

def hexagon(side):
    for _ in range(6):
        forward(side)
        left(60)

#hexagon(50)

'''for _ in range(6):
    hexagon(60)
    forward(60)
    left(60)
    forward(60)
    right(60)
    forward(60)
    left(60)'''

def rhombus(side, angle):
    for _ in range(2):
        forward(side)
        left(angle)
        forward(side)
        left(180 - angle)
        
'''l = 20
for _ in range(l):
    rhombus(100, 60)
    left(360 / l)'''


def five_star(size):
    for _ in range(5):
        forward(size)
        left(144)

'''setx(-300)
five_star(500)'''

'''
for i in range(20, 200, 10):
    for _ in range(4):
        left(90)
        forward(i)'''


'''for length in range(1, 200, 1):
    forward(length)
    right(69)'''

def DO_NOT_USE():    
    circle(30)
    pu()
    forward(60)
    pd()
    circle(30)
    left(90)
    pu()
    forward(60)
    pd()
    forward(100)
    right(90)
    forward(2.5)
    left(90)
    circle(35, 180)
    left(90)
    forward(2.5)
    right(90)
    forward(100)
'''
shape('turtle')
for _ in range(10):
    circle(80, 36)
    stamp()'''

'''shape()
def stroke():
    for _ in range(7):    
        forward(25)
        stamp()
        for _ in range(10):
            circle(80, 36)
            stamp()
stroke()'''


def star(n, length=100):
    for _ in range(n):
        forward(length)
        stamp()
        backward(length)
        left(360 / n)
#star(8)

def eurasian_star(length=100):
    for _ in range(4):
        Screen().bgcolor('black')
        pencolor('yellow')
        forward(length / 1.33)
        stamp()
        backward(length / 1.33)
        left(360 / 8)
        forward(length)
        stamp()
        backward(length)
        left(360 / 8)

#eurasian_star()

def turtle_circle(radius):
    pensize(2)
    shape('turtle')
    pu()
    stamp()
    for _ in range(12):
        forward(radius * 0.75)
        pd()
        forward(radius * 0.15)
        pu()
        forward(radius * 0.1)
        stamp()
        backward(radius)
        left(360 / 12)

#turtle_circle(200)
def turtle_ratio():
    pu()
    shape('turtle')
    i = 1

    while 0 <= abs(pos()[0]) <= screensize()[0] * 1.5 and 0 <= abs(pos()[1]) <= screensize()[1] * 1.5:
        stamp()
        forward(i)
        right(16.18)
        i += 1
#turtle_ratio()

def funny_spiral():
    colors = ['yellow', 'green', 'purple', 'orange', 'red', 'blue']
    for i in range(1, 40):
        pencolor(colors[i % len(colors)])
        pensize(i)
        forward(i * 5)
        left(45)

#funny_spiral()
getcontext().prec = 50
golden_ratio = (D(5).sqrt() + 1) / 2
print(golden_ratio)

screensize(1200, 800)
def golden_spiral(radius=1):
    while True:
        circle(radius, 90)
        radius *= float(golden_ratio)
#left(90)
#golden_spiral(1)

def iiiii_goiii(size):
    triangle(size)
    forward(size / 3)
    right(60)
    forward(size / 3)
    left(120)
    triangle(size)
#iiiii_goiii(200)

def xi(size):
    circle(size / 2)
    circle(size, 150)
    right(180)
    circle(size / 4)
    right(180)
    circle(size, 60)
    right(180)
    circle(size / 4)
    right(180)
    circle(size, 150)
    left(90)
    pu()
    forward(size * 0.15)
    pd()
    forward(size * 0.5)
    right(90)
    circle(size / 10)
    pu()
    pensize(10)
    forward(size * 0.5)
    left(90)
    forward(size / 3)
    dot()
    left(90)
    forward(size)
    dot()
    
'''xi(120)
hideturtle()'''

write('сукаа!')


Screen().exitonclick()