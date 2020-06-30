import tkinter
from tkinter import *
import math


class Calcu:
    def gui_structure(self):
        # ------------Window Gui----------------------
        screen = Tk()
        screen.title("My Calcu")
        screen.geometry('500x600')
        screen.config(bg='#423E3E')

        # ------------Calcu Screen---------------------
        # here i used Text Field Reason is i will plan to input date from keyboard
        label1 = Label(screen,width=42, relief=FLAT, justify='right', bd=25,font=('Arial',12,'bold'), bg='orange')
        label1.grid(column=0, row=0, padx=15, pady=0)
        #text1 is display full nubers you enter text2 only display current enter number
        txt2 = Entry(screen, width=22, relief=FLAT, justify='right', bd=26, font=('Arial', 26, 'bold'), bg='orange')
        txt2.grid(column=0, row=1, padx=15, pady=0)
        # -------------buttons--------------------------
        button7 = Button(screen, text='7', width=5, height=5)
        button7.grid(column=0, row=3, padx=0, pady=0)

        screen.mainloop()


cs = Calcu.gui_structure
cs(0)
