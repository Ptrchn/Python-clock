from tkinter import *
from tkinter.ttk import *

from time import strftime

box = Tk()
box.title('clock')

def time():
    string = strftime('%H : %M : %S : %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(box, font=('ds-digital', 80),background = 'yellow' , foreground =  'red')
label.pack(anchor='center')
time()

mainloop()


