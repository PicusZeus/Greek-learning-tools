dir = 'pictures/'
from tkinter import *
win = Tk()
igm = PhotoImage(file = dir + 'alf.gif')
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=igm.width(), height= igm.height())
can.create_image(4, 4, image=igm, anchor=NW)
#Label(can, text='yo').pack()

win.mainloop()