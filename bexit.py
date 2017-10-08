from user_preferences import bcolor, bfont, bsize
from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Wyjście', command= self.quit)
#        widget.config()
        widget.pack()

    def quit(self):
        ans = askokcancel('Potwierdź wyjście', 'Naprawdę wyjść?')
        if ans: Frame.quit(self)


