from graphics import *

#Window UI
win = GraphWin("My Circle", 800, 800)

enter = Rectangle(Point(400, 90), Point(480, 110))
enter.setFill("grey")
text = Text(Point(420, 100), "Enter")

inputBox1 = Entry(Point(200, 100), 10)
inputBox1.setText("0")
inputBox2 = Entry(Point(300, 100), 10)
inputBox2.setText("0")
outputBox = Entry(Point(600, 100), 10)

# Draw Method
enter.draw(win)
text.draw(win)

outputBox.draw(win)
inputBox1.draw(win)
inputBox2.draw(win)

def mult(v1,v2,ev1,ev2):
    if v1 != 0 or v2 != 0:
        ms = v1 * v2
        sd = (ms)*((ev1/v1)+(ev2/v2))
        return sd
    else:
        return 0

while True:
    ponto = win.getMouse()
    x = ponto.getX()
    y = ponto.getY()
    if x >= 400 and x <= 480 and y >= 90 and y <= 110:
        print("enter")
        # Getting content
        inputStr1 = inputBox1.getText()
        inputStr2 = inputBox2.getText()
        outputStr1 = outputBox.getText()
        # Content Updates
        ans = mult(float(inputStr1), float(inputStr2), 0, 0)
        outputBox.setTextColor("black")
        outputBox.setText(ans)
#Closing condition
while True:
    if win.checkKey() == "q":
        win.close()
