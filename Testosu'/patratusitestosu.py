
import turtle

##def drawSquareCircleTriangle():
##
##    #creare window si culoare fundal
##    
##    window = turtle.Screen()
##    window.bgcolor("red")
##
##    #patratosu e o instanta a clasei Turtle din turtle file
##    patratosu= turtle.Turtle()
##
##    #patratosu devine galben si de viteza 2
##    
##    patratosu.color("yellow")
##    patratosu.speed(2)
##
##    #folosim while loop pt a il deplasa
##
##    squareSides=0
##    
##    while(squareSides<=4):
##        patratosu.forward(100)
##        patratosu.right(90)
##        squareSides+=1

    
##    cercosu=turtle.Turtle()
##    cercosu.color("blue")
##    cercosu.circle(100)
##
##    triungosu=turtle.Turtle()
##    triungosu.color("black")
##
##    #triangleSides=0
##
##    #while(triangleSides<=3):
##    triungosu.forward(100)
##    triungosu.left(120)
##    triungosu.forward(100)
##    triungosu.left(120)
##    triungosu.forward(100)
##        #triangleSides+=1
        
##    window.exitonclick()

##drawSquareCircleTriangle()

def drawSquare(turtleHolder):
    for i in range(1,5):
        turtleHolder.forward(100)
        turtleHolder.right(90)
        
def drawArt():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37):
        drawSquare(brad)
        brad.right(10)
    

drawArt()
    
    
