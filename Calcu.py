import tkinter
from tkinter import *


class Calcu:
    def gui_structure(self):
        # ------------Window Gui----------------------
        screen = Tk()
        screen.title("My Calcu")
        screen.geometry('500x600')
        screen.config(bg='#423E3E')

        # ------------Calcu Screen---------------------
        # here i used Text Field Reason is i will plan to input date from keyboard
        txt1 = Text(screen, width=60,height=10 )
        txt1.grid(column=5, row=1 ,padx=8, pady=15)

        screen.mainloop()


cs = Calcu.gui_structure
cs(0)
