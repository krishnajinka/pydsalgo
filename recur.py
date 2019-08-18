from turtle import Turtle

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def listSum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listSum(numlist[1:])

def tostr(n, base):
    convertStr = "0123456789ABCDEF"
    if n<base:
        return convertStr[n]
    else:
        return tostr(n // base, base) + convertStr[n%base]

def drawspiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawspiral(myTurtle, lineLen-5)

#1. 
lst=[3,5,7,9]
print(listSum(lst))

#2. 
print(tostr(769, 10))

drawspiral(myTurtle, 100)
myWin.exitonclick()