from tkinter import *

window = None
displayLabel = None
equation = None
expression = ''


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




guiMain()