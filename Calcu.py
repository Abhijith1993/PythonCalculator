import tkinter
from tkinter import *
import math

expression = ""

def input_number(number, equation):
   # accessing the global expression variable
   global expression
   # concatenation of string
   expression = expression + str(number)
   equation.set(expression)

class Calcu:

    def gui_structure(self):
        # ------------Window Gui----------------------
        screen = Tk()
        screen.title("My Calcu")
        screen.geometry('390x600')
        screen.config(bg='#423E3E')
        equation = StringVar()


        # ------------Calcu Screen---------------------
        # here i used Text Field Reason is i will plan to input date from keyboard
        label1 = Label(screen, width=36, relief=FLAT, justify='right', bd=25, font=('Arial', 11, 'bold'), bg='orange')
        label1.grid(column=0, row=0, padx=5, pady=0)
        # text1 is display full nubers you enter text2 only display current enter number
        txt2 = Entry(screen,textvariable=equation, width=17, relief=FLAT, justify='right', bd=26, font=('Arial', 26, 'bold'), bg='orange')
        txt2.grid(column=0, row=1, padx=5, pady=0)
        # -------------buttons--------------------------
        button7 = Button(screen, text='7', width=8, height=3,command=lambda: input_number(7, equation))
        button7.place(x=15, y=290)

        button8 = Button(screen, text='8', width=8, height=3,command=lambda: input_number(8, equation) )
        button8.place(x=115, y=290)

        button9 = Button(screen, text='9', width=8, height=3,command=lambda: input_number(9, equation) )
        button9.place(x=215, y=290)

        button4 = Button(screen, text='4', width=8, height=3,command=lambda: input_number(4, equation) )
        button4.place(x=15, y=370)

        button5 = Button(screen, text='5', width=8, height=3,command=lambda: input_number(5, equation) )
        button5.place(x=115, y=370)

        button6 = Button(screen, text='6', width=8, height=3,command=lambda: input_number(6, equation) )
        button6.place(x=215, y=370)

        button1 = Button(screen, text='1', width=8, height=3,command=lambda: input_number(1, equation) )
        button1.place(x=15, y=450)

        button2 = Button(screen, text='2', width=8, height=3,command=lambda: input_number(2, equation) )
        button2.place(x=115, y=450)

        button3 = Button(screen, text='3', width=8, height=3,command=lambda: input_number(3, equation) )
        button3.place(x=215, y=450)

        button0 = Button(screen, text='0', width=22, height=3,command=lambda: input_number(0, equation) )
        button0.place(x=15, y=530)

        buttondot = Button(screen, text='.', width=8, height=3,command=lambda: input_number(".", equation) )
        buttondot.place(x=215, y=530)

        buttoneq = Button(screen, text='=', width=8, height=3, )
        buttoneq.place(x=315, y=450)

        buttonpl = Button(screen, text='+', width=8, height=8,command=lambda: input_number("+", equation) )
        buttonpl.place(x=315, y=290)

        buttonml = Button(screen, text='X', width=8, height=3,command=lambda: input_number("X", equation) )
        buttonml.place(x=315, y=210)

        buttondi = Button(screen, text='÷', width=8, height=3,command=lambda: input_number("/", equation) )
        buttondi.place(x=215, y=210)

        buttonro = Button(screen, text='√', width=8, height=3,command=lambda: input_number("√", equation) )
        buttonro.place(x=115, y=210)

        buttonmod = Button(screen, text='%', width=8, height=3,command=lambda: input_number("%", equation) )
        buttonmod.place(x=15, y=210)

        buttondel = Button(screen, text='DEL', width=8, height=3,)
        buttondel.place(x=315, y=530)

        screen.mainloop()


cs = Calcu.gui_structure
cs(0)
