from tkinter import *

window = None
displayLabel = None
equation = None
expression = ""

def guiMain():
    setupGUI()
    window.mainloop()

def nothing():
    pass

def setupGUI():
    global window
    global displayLabel
    global equation

    window = Tk()
    window.title('Caculator')
    equation = StringVar()
    equation.set('0')
    displayLabel = Label(window, textvariable = equation, justify = RIGHT,
                         relief=RAISED, width=15, font="Futura 20")
    displayLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    setupButtons()

def setupButtons():
    button1 = Button(window, text="1", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(1))
    button1.grid(row=1, column=0)
    button2 = Button(window, text="2", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(2))
    button2.grid(row=1, column=1)
    button3 = Button(window, text="3", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(3))
    button3.grid(row=1, column=2)

    button4 = Button(window, text="4", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(4))
    button4.grid(row=2, column=0)
    button5 = Button(window, text="5", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(5))
    button5.grid(row=2, column=1)
    button6 = Button(window, text="6", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(6))
    button6.grid(row=2, column=2)
    button7 = Button(window, text="7", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(7))
    button7.grid(row=3, column=0)
    button8 = Button(window, text="8", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(8))
    button8.grid(row=3, column=1)
    button9 = Button(window, text="9", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(9))
    button9.grid(row=3, column=2)
    button0 = Button(window, text="0", relief=RAISED, width=5, height=2, font="Futura 20", command=lambda: press(0))
    button0.grid(row=4, column=1)
    setupCalculatingButtons()

def setupCalculatingButtons():
    # c 버튼, =버튼
    clearButton = Button(window, text="C", relief=RAISED, width=5, height=2, font="Futura 15", command=clearDisplay)
    clearButton.grid(row=4, column=0)

    resultButton = Button(window, text="=", relief=RAISED, width=5, height=2, font="Futura 15", command=equalPress)
    resultButton.grid(row=4, column=2)

    addButton = Button(window, text="+", relief=RAISED, width=5, height=2, font="Futura 15", command=lambda:press("+"))
    addButton.grid(row=1, column=3)
    subButton = Button(window, text="-", relief=RAISED, width=5, height=2, font="Futura 15", command=lambda:press("-"))
    subButton.grid(row=2, column=3)
    mulButton = Button(window, text="x", relief=RAISED, width=5, height=2, font="Futura 15", command=lambda:press("*"))
    mulButton.grid(row=3, column=3)
    divButton = Button(window, text="/", relief=RAISED, width=5, height=2, font="Futura 15", command=lambda:press("/"))
    divButton.grid(row=4, column=3)


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clearDisplay():
    global expression
    expression = ""
    equation.set("0")

def equalPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

guiMain()