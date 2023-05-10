from turtle import *
import random
from PIL import Image

setup(600, 600)


def tiling(x,y,s,l, mode):
    # final level of recursion, draw line
    if l == 0:
        if mode == "straight":
            if random.random() < 0.5:
                # vertical line
                penup()
                goto(x,y-s)
                pendown()
                goto(x, y+s)

            else:
                # horizontal line
                penup()
                goto(x-s,y)
                pendown()
                goto(x+s,y)
        elif mode == "diagonal":
            if random.random() < 0.5:
                # NW to SE line
                penup()
                goto(x-s,y+s)
                pendown()
                goto(x+s, y-s)

            else:
                # SW to NE line
                penup()
                goto(x-s,y-s)
                pendown()
                goto(x+s,y+s)
    # split the screen and go to next level of recursion
    else:
        s /= 2
        l -= 1
        tiling(x-s,y+s,s,l,mode)
        tiling(x+s,y+s,s,l,mode)
        tiling(x-s,y-s,s,l,mode)
        tiling(x+s,y-s,s,l,mode)

width(3)
hideturtle()
tracer(False)
tiling(0,0,250,5,"diagonal")
tracer(True)

getscreen().getcanvas().postscript(file='myImage.ps')
psimage=Image.open('myImage.ps')
psimage.save('myImage.png')

exitonclick()