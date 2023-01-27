from graphics import *

AM = 0
#Window UI
win = GraphWin("My Circle", 800, 800)

modesel = Rectangle(Point(170, 90), Point(190, 110))
modesel.setFill("grey")
text1 = Text(Point(180, 100), "*")

enter = Rectangle(Point(360, 90), Point(380, 110))
enter.setFill("grey")
text2 = Text(Point(370, 100), "=")

inputBox1 = Entry(Point(80, 100), 10)
inputBox1.setText("0")
inputBox2 = Entry(Point(280, 100), 10)
inputBox2.setText("0")
outputBox = Entry(Point(600, 100), 35)

# Draw Method
modesel.draw(win)
enter.draw(win)
text1.draw(win)
text2.draw(win)

outputBox.draw(win)
inputBox1.draw(win)
inputBox2.draw(win)

def calc(v1,v2,ev1,ev2,mode):
    if v1 != 0 or v2 != 0:
        if mode == 0:
            ms = v1 * v2
        else:
            ms = v1 / v2
        sd = (ms) * ((ev1/v1)+(ev2/v2))
        return ms, "±" , sd
    else:
        return 0

while True:
    ponto = win.getMouse()
    x = ponto.getX()
    y = ponto.getY()
    if x >= 170 and x <= 190 and y >= 90 and y <= 110:
        if AM == 0:
            AM = 1
            text1.undraw()
            text1 = Text(Point(180, 100), "/")
            text1.draw(win)
        else:
            AM = 0
            text1.undraw()
            text1 = Text(Point(180, 100), "*")
            text1.draw(win)
    if x >= 360 and x <= 380 and y >= 90 and y <= 110:
        print("enter")
        # Getting content
        inputStr1 = inputBox1.getText().split("±")
        print(inputStr1[0].replace(',', '.'))
        print(inputStr1[1].replace(',', '.'))
        inputStr2 = inputBox2.getText().split("±")
        print(inputStr2[0].replace(',', '.'))
        print(inputStr2[1].replace(',', '.'))
        outputStr1 = outputBox.getText()
        # Content Updates
        ans = calc(float(inputStr1[0].replace(',', '.')), float(inputStr2[0].replace(',', '.')),float(inputStr1[1].replace(',', '.')),float(inputStr2[1].replace(',', '.')),AM)
        outputBox.setTextColor("black")
        outputBox.setText(ans)
#Closing condition
while True:
    if win.checkKey() == "q":
        win.close()
