from graphics import *

#Window UI
win = GraphWin("My Circle", 800, 800)
inputBox = Entry(Point(200, 100), 10)
outputBox = Entry(Point(600, 100), 10)

while True:
    # Draw Method
    outputBox.undraw()
    inputBox.undraw()

    #Content Updates
    inputStr = inputBox.getText()
    outputBox.setText(str(inputStr))

    #Draw Method
    outputBox.draw(win)
    inputBox.draw(win)

    #Closing condition
    if win.getMouse():
        win.close()
