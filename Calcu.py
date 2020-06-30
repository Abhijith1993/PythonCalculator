import tkinter
from tkinter import *
import math


class Calcu:
    def gui_structure(self):
        # ------------Window Gui----------------------
        screen = Tk()
        screen.title("My Calcu")
        screen.geometry('390x600')
        screen.config(bg='#423E3E')

        # ------------Calcu Screen---------------------
        # here i used Text Field Reason is i will plan to input date from keyboard
        label1 = Label(screen, width=36, relief=FLAT, justify='right', bd=25, font=('Arial', 11, 'bold'), bg='orange')
        label1.grid(column=0, row=0, padx=5, pady=0)
        # text1 is display full nubers you enter text2 only display current enter number
        txt2 = Entry(screen, width=17, relief=FLAT, justify='right', bd=26, font=('Arial', 26, 'bold'), bg='orange')
        txt2.grid(column=0, row=1, padx=5, pady=0)
        # -------------buttons--------------------------
        button7 = Button(screen, text='7', width=8, height=3, )
        button7.place(x=15, y=290)

        button8 = Button(screen, text='8', width=8, height=3, )
        button8.place(x=115, y=290)

        button9 = Button(screen, text='9', width=8, height=3, )
        button9.place(x=215, y=290)

        button4 = Button(screen, text='4', width=8, height=3, )
        button4.place(x=15, y=370)

        button5 = Button(screen, text='5', width=8, height=3, )
        button5.place(x=115, y=370)

        button6 = Button(screen, text='6', width=8, height=3, )
        button6.place(x=215, y=370)

        button1 = Button(screen, text='1', width=8, height=3, )
        button1.place(x=15, y=450)

        button2 = Button(screen, text='2', width=8, height=3, )
        button2.place(x=115, y=450)

        button3 = Button(screen, text='3', width=8, height=3, )
        button3.place(x=215, y=450)

        button0 = Button(screen, text='0', width=22, height=3, )
        button0.place(x=15, y=530)

        buttondot = Button(screen, text='.', width=8, height=3, )
        buttondot.place(x=215, y=530)

        buttoneq = Button(screen, text='=', width=8, height=8, )
        buttoneq.place(x=315, y=455)

        buttonpl = Button(screen, text='+', width=8, height=9, )
        buttonpl.place(x=315, y=290)

        buttonml = Button(screen, text='X', width=8, height=3, )
        buttonml.place(x=315, y=210)

        buttondi = Button(screen, text='÷', width=8, height=3, )
        buttondi.place(x=215, y=210)

        buttonro = Button(screen, text='√', width=8, height=3, )
        buttonro.place(x=115, y=210)

        buttonmod = Button(screen, text='%', width=8, height=3, )
        buttonmod.place(x=15, y=210)

        screen.mainloop()


cs = Calcu.gui_structure
cs(0)
