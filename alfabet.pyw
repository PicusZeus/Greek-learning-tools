

import os
from tkinter import *
from tkinter.messagebox import askyesno, showinfo
from tkinter.colorchooser import askcolor
import random

from slownik import podstawowy, przydechy, dyftongi, transwords



imgfolder = './pictures/'

tkroot = Tk()
tkroot.title('Grecki Alfabet, ćwiczenia')

def startprogram():
    global tkroot
    tkroot = Tk()
    tkroot.title('Grecki Alfabet, ćwiczenia')
    Alfabet(tkroot)
    tkroot.mainloop()

class Alfabet(Frame):

    def __init__(self, parent=tkroot, **options):
        Frame.__init__(self, parent, **options)

        self.pack()
        self.letter = ''
        self.make_widgets()
        self.bind('<Double-1>', self.onDoubleLeftClick)
        self.slownik = podstawowy
        self.numtry = 10
        self.tries = 0 # number of times a user tried
        self.score = 0
        self.totalscore = 0
        self.prob = 0



    def onDoubleLeftClick(self):
        pass



    def make_widgets(self):

        self.canAlfabet()
        self.opcje()
        self.mainframe = Frame()
        self.mainframe.pack(fill=BOTH)

        self.Start()
        self.exitBut()



    # widgets
    def canAlfabet(self):

        # a canvas with a picture of the Greek alphabet
        imageobj = PhotoImage(file=imgfolder + 'alf.gif')
        self.imageobj = imageobj



        can = Canvas()
        can.pack(fill=BOTH)
        print(self.imageobj.width())
        can.config(height= self.imageobj.height(), width= self.imageobj.width(), bg='white')
        can.create_image(2, 2, image= self.imageobj, anchor=NW)
    
    
    def opcje(self):
        # options, everything on one frame, that will be forgot after starting of the quiz
        var1 = StringVar()
        fropt = Frame()
        fropt.pack(fill=BOTH, expand=YES)
        self.fropt = fropt
        fr1 = Frame(fropt)
        fr1.config(bd=2, relief=GROOVE, bg='yellow')
        fr1.pack(side=LEFT, fill=Y)
        Radiobutton(fr1, text='Litery', command=self.onLitery, variable=var1, value='Litery', bg='yellow').pack(anchor=NW, fill=BOTH, expand=YES)
        Radiobutton(fr1, text='Słowa', command=self.onSlowa, variable=var1, value='Słowa', bg='yellow').pack(anchor=NW, fill=BOTH, expand=YES)
        Radiobutton(fr1, text='Zdania', command=self.onZdania, variable=var1, value='Zdania', bg='yellow').pack(anchor=NW, fill=BOTH, expand=YES)
        self.var1 = var1
        self.var1.set('Litery')
        self.opts=[]

        self.pytanie1 = 'Ile liter chcesz przećwiczyć?'
        self.what='literę'

        Scal = Frame(fropt)
        Scal.pack(side=TOP, fill=BOTH, expand=YES)
        self.labPyt = Label(Scal, text=self.pytanie1, bg='green', font = ('arial', 14, 'normal'))
        self.labPyt.pack(fill=BOTH, expand=YES)
        self.num = IntVar()
        Scale(Scal, command=self.onNumber,
              variable=self.num, from_=0, to=20, length=800, tickinterval=5,
              showvalue=YES, orient='horizontal', bg = 'white', bd=2, relief=SUNKEN).pack(expand=YES, fill = BOTH)
        self.num.set(10)


        fr2 = Frame(fropt)
        fr2.config(bd=2, relief=GROOVE)
        fr2.pack(side=LEFT, fill=BOTH, expand=YES)
        for opcja in ['Przydechy', 'Dyftongi', 'Wymowa_erazmiańska', 'Wymowa_nowogrecka']:
            var = IntVar()
            com = "self." + 'on' + opcja
            com = eval(com)
            Checkbutton(fr2,
                        text=opcja,
                        variable=var,
                        command=com, bg='salmon').pack(side=LEFT, expand=YES, fill=X)
            self.opts.append(var)

    # callbacks from options

    def onSlowa(self):
        self.pytanie1 = 'Ile słów chcesz przećwiczyć?'
        self.labPyt.config(text=self.pytanie1)
        self.what= 'słowo'
        self.slownik = transwords


    def onZdania(self):
        self.pytanie1 = 'Ile zdań chcesz przećwiczyć?'
        self.labPyt.config(text=self.pytanie1)
        self.what = 'zdanię'
    def onLitery(self):
        self.pytanie1 = 'Ile liter chcesz przećwiczyć?'
        self.labPyt.config(text=self.pytanie1)
        self.slownik = podstawowy
        self.what = 'literę'
        self.onPrzydechy()
        self.onDyftongi()
    def onPrzydechy(self):
        if self.var1.get() == 'Litery':
            if self.opts[0].get() == 1:
#                print(self.opts[0].get())
                self.slownik = {**self.slownik, **przydechy}
            else:
               self.slownik = {k: v for k, v in self.slownik.items() if k not in przydechy}
#           print(self.slownik)

    def onDyftongi(self):
        print('sprawdzam')
        if self.var1.get() == 'Litery':
            if self.opts[1].get() == 1:
                self.slownik = {**self.slownik, **dyftongi}
                print(self.slownik)
            else:
                self.slownik = {k: v for k, v in self.slownik.items() if k not in dyftongi}
#            print(self.slownik)

    def onNumber(self, number):

        self.numtry = self.num.get()
        self.allnumtry = self.num.get()

    def onWymowa_erazmiańska(self):
        if self.opts[2].get():
            self.opts[3].set(0)
        else:
            self.opts[3].set(1)

    def onWymowa_nowogrecka(self):
        if self.opts[3].get():
            self.opts[2].set(0)
        else:
            self.opts[2].set(1)


# Start Button

    def Start(self):
        #creates a button that upon pressing creates main part of the program
        startbutton = Button(text='Zaczynam', command=self.onStart, font=('arial', 18, 'normal'), bg= 'gold', fg='deep sky blue', relief=SUNKEN, bd=8)
        startbutton.pack(fill=BOTH, expand=YES)
        self.startbutton = startbutton

# onStart

    def onStart(self):
        # callback from start button
        self.letter= random.choice(list(self.slownik.keys()))
        # create widgets
        self.plakat()
        self.entrytext()
        # say bay bay to options
        self.startbutton.pack_forget()
        self.fropt.pack_forget()


# widgets used for quiz

    def plakat(self):

        Rama1 = Frame(self.mainframe)
        Rama1.pack(fill=X, expand=YES)
        Rama1.config(bg='gainsboro')
        self.Rama1 = Rama1
        Label(Rama1, text='Przetranskrybuj \n %s:' %(self.what), font=('Helvetica', 34, 'bold'),
              bg='AntiqueWhite2' ).pack(side=LEFT, fill=Y)
        plak = Label(Rama1, text = self.letter)
        plak.config(bg='AntiqueWhite2', font=('arial', 50, 'normal'))
        plak.pack(side=LEFT, expand=YES, fill=BOTH)

        self.plak = plak

# entry widget, where user gives his/her answer


    def entrytext(self):
        Rama2 = Frame(self.mainframe)
        Rama2.pack(fill=X, expand=YES)

        ent = Entry(Rama2)
        ent.config(font=('arial', 26, 'italic'))
        ent.pack(fill=X, expand=YES)
        ent.insert(0, 'Pisz tutaj')
        ent.focus()
        ent.bind('<Return>', (lambda event: self.onfetch()))

        btn = Button(Rama2, text='Zatwierdź', command=self.onfetch, bg='orange', fg='azure', font=('Times', 16, 'bold'))
        btn.pack(fill=X, expand=YES)

        Rama2 = Frame(self.mainframe)
        Rama2.pack(fill = X, expand=YES)
        self.prob = 0
        info = Label(Rama2, bg='AntiqueWhite2', height= 2, text='Do dzieła!', font=('arial', 25, 'bold'))
        info.pack(fill= X, expand=YES)
        self.info = info
        scoring = Label(Rama2, text='Udało mi się 0 razy na %s prób.' %(self.prob), font=('Times', 20, 'italic'), bg='cyan2')
        scoring.pack(fill=X, expand=YES)
        self.scoring = scoring
        self.ent = ent


    def onfetch(self):
        self.prob = self.prob + 1

        if self.numtry > 0:
            inp = self.ent.get().lower()
            orig = self.letter

            if inp in self.slownik[orig] and inp != '':
                print('ok')
                self.score += 1
                print(self.prob)
                self.scoring.config(text='Udało mi się %s razy na %s prób.' %(self.score, self.prob))
                self.info.config(text='Brawo!!!\n %s = %s' %(inp, orig))

            else:
                print('no')
                self.info.config(text='Niestety, poprawna odpowiedź to\n: %s = %s' %(orig, str(self.slownik[orig])))
                self.scoring.config(text='Udało mi się %s razy na %s prób.' % (self.score, self.prob))


            if self.numtry > 1:
                self.letter = random.choice(list(self.slownik.keys()))
                self.plak.config(text=self.letter)
                self.numtry = self.numtry - 1
                self.ent.delete(0, END)
            else:
                win = Toplevel()
                you =''
                
                if self.score / self.allnumtry >= 0.9:
                    you = 'sowa.gif'
                else:
                    
                    you = 'osiol.gif'
                
                endimg = PhotoImage(file=imgfolder + you)
                
                self.endimg=endimg
                self.mainframe.pack_forget()
                can = Canvas(win)
                can.pack(fill=BOTH)
                
                can.config(height= self.endimg.height(), width= self.endimg.width())
                
                can.create_image(2, 2, image= self.endimg, anchor=NW)
                
                Label(win, text='Twoj wynik to %s na %s' %(self.score, self.allnumtry)).pack()
                
                Button(win, text='Koniec', command=self.quit).pack()
                Button(win, text='Chcę spróbować jeszcze raz', command=self.onRestart).pack()




    def onRestart(self):

        
        
        
        os.popen('alfabet.exe')

        self.quit()



    def exitBut(self):

        bt = Button(text = 'Wyjście', padx=10, pady=10)
        bt.pack(padx=20, pady=20)
        bt.config(cursor='gumby', bd =8, relief= RAISED, bg='dark green', fg='white')
        bt.config(font = ('helvetica', 20, 'underline italic'))
        bt.config(command=self.excallback)

    def excallback(self):
        if askyesno('Potwierdź', 'Czy na pewno chcesz wyjść?'):
            self.quit()
        else:
            showinfo('Nie', 'Uczę się dalej')



    def Oncolor(self):
        (triple, hexstr) = askcolor()
        return hexstr




Alfabet(tkroot).mainloop()

