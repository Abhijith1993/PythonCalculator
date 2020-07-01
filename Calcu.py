import tkinter
from tkinter import *
import math

expression = ""
one_expression = " "
one_expression1 = " "


def input_number(number, equation, one):
    # accessing the global expression variable
    # accessing the global one_expression variable
    global expression
    global one_expression
    # concatenation of string
    expression = expression + str(number)
    equation.set(expression)
    # here to show one digit at a time in second display
    if str(number) == ("+"):
        one_expression = one.get()
        one_expression = " "
        one.set(one_expression)
    elif str(number) == ("-"):
        one_expression = one.get()
        one_expression = " "
        one.set(one_expression)
    elif str(number) == ("*"):
        one_expression = one.get()
        one_expression = " "
        one.set(one_expression)
    elif str(number) == ("/"):
        one_expression = one.get()
        one_expression = " "
        one.set(one_expression)
    elif str(number) == ("%"):
        one_expression = one.get()
        one_expression = " "
        one.set(one_expression)
    else:
        one_expression = one_expression + str(number)
        one.set(one_expression)


def clear1(number, equation):
    global expression
    length = len(expression)
    expression = expression[0: -1]
    equation.set(expression)


def root(equation):
    global expression
    root = int(expression) * int(expression)
    expression = str(root)
    equation.set(expression)


def evaluate(equation):
    global expression
    # trying to evaluate the expression
    try:
        result = str(eval(expression))
        # showing the result in the input field
        equation.set(result)
        # setting expression to empty string
        expression = ""
    except ZeroDivisionError:
        equation.set("Can't Divide By Zero")


# some error occured
# showing it to the user equation.set("Enter a valid expression")

# creating the GUI

class Calcu:

    def gui_structure(self):
        # ------------Window Gui----------------------
        screen = Tk()
        screen.title("My Calcu")
        screen.geometry('390x600')
        screen.config(bg='#423E3E')
        equation = StringVar()
        one = StringVar()

        # ------------Calcu Screen---------------------
        # here i used Text Field Reason is i will plan to input date from keyboard
        label1 = Label(screen, textvariable=equation, width=36, relief=FLAT, justify='right', bd=25,
                       font=('Arial', 11, 'bold'), bg='orange')
        label1.grid(column=0, row=0, padx=5, pady=0)
        # text1 is display full numbers you enter text2 only display current enter number
        txt2 = Entry(screen, textvariable=one, width=17, relief=FLAT, justify='right', bd=26,
                     font=('Arial', 26, 'bold'), bg='orange')
        txt2.grid(column=0, row=1, padx=5, pady=0)
        # -------------buttons--------------------------
        button7 = Button(screen, text='7', width=3, height=1,
                         command=lambda: input_number(7, equation, one), font="Verdana 19 bold")
        button7.place(x=15, y=290)

        button8 = Button(screen, text='8', width=3, height=1,
                         command=lambda: input_number(8, equation, one), font="Verdana 19 bold")
        button8.place(x=115, y=290)

        button9 = Button(screen, text='9', width=3, height=1,
                         command=lambda: input_number(9, equation, one), font="Verdana 19 bold")
        button9.place(x=215, y=290)

        button4 = Button(screen, text='4', width=3, height=1,
                         command=lambda: input_number(4, equation, one), font="Verdana 19 bold")
        button4.place(x=15, y=370)

        button5 = Button(screen, text='5', width=3, height=1,
                         command=lambda: input_number(5, equation, one), font="Verdana 19 bold")
        button5.place(x=115, y=370)

        button6 = Button(screen, text='6', width=3, height=1,
                         command=lambda: input_number(6, equation, one), font="Verdana 19 bold")
        button6.place(x=215, y=370)

        button1 = Button(screen, text='1', width=3, height=1,
                         command=lambda: input_number(1, equation, one), font="Verdana 19 bold")
        button1.place(x=15, y=450)

        button2 = Button(screen, text='2', width=3, height=1,
                         command=lambda: input_number(2, equation, one), font="Verdana 19 bold")
        button2.place(x=115, y=450)

        button3 = Button(screen, text='3', width=3, height=1,
                         command=lambda: input_number(3, equation, one), font="Verdana 19 bold")
        button3.place(x=215, y=450)

        button0 = Button(screen, text='0', width=9, height=1,
                         command=lambda: input_number(0, equation, one), font="Verdana 19 bold")
        button0.place(x=15, y=530)

        buttondot = Button(screen, text='.', width=3, height=1,
                           command=lambda: input_number(".", equation, one), font="Verdana 19 bold")
        buttondot.place(x=215, y=530)

        buttoneq = Button(screen, text='=', width=3, height=1,
                          command=lambda: evaluate(equation, ), font="Verdana 19 bold")
        buttoneq.place(x=315, y=530)

        buttonpl = Button(screen, text='+', width=3, height=1,
                          command=lambda: input_number("+", equation, one), font="Verdana 19 bold")
        buttonpl.place(x=315, y=290)

        buttonpl = Button(screen, text='-', width=3, height=1,
                          command=lambda: input_number("-", equation, one), font="Verdana 19 bold")
        buttonpl.place(x=315, y=370)

        buttonml = Button(screen, text='X', width=3, height=1,
                          command=lambda: input_number("*", equation, one), font="Verdana 19 bold")
        buttonml.place(x=315, y=210)

        buttondi = Button(screen, text='÷', width=3, height=1,
                          command=lambda: input_number("/", equation, one), font="Verdana 19 bold")
        buttondi.place(x=215, y=210)

        buttonro = Button(screen, text='x²', width=3, height=1,
                          command=lambda: ("√", root(equation)), font="Verdana 19 bold")
        buttonro.place(x=115, y=210)

        buttonmod = Button(screen, text='%', width=3, height=1,
                           command=lambda: input_number("%", equation, one), font="Verdana 19 bold")
        buttonmod.place(x=15, y=210)

        buttondel = Button(screen, text='C', width=3, height=1,
                           command=lambda: clear1(1, equation, one), font="Verdana 19 bold")
        buttondel.place(x=315, y=450)

        screen.mainloop()


cs = Calcu.gui_structure
cs(0)
