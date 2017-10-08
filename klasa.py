from tkinter import *

class Rama(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()
        self.data = 3

    def make_widgets(self):

        widget = Button(self, text='Hello greek', command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data += 1
        print('yo %s' % self.data)

