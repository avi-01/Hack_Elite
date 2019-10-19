
import tkinter as tk
from tkinter import *

back = '#454647'
titleBack = '#343b80'
startClick = 0


def onOFF():
    global startClick 
    startClick+=1
    if(startClick%2==1):
        start()
    else:
        stop()
    

def start():
    onOFFButton.configure(text='Stop')
    
def stop():
    onOFFButton.configure(text='Start')



r = tk.Tk() 
r.title('Destello')
r.configure(background=back)
r.geometry("800x600")

titleFrame = Frame(r,bg=titleBack)
titleFrame.pack(side=TOP, fill=X,ipady=2)

title = Label(titleFrame,text="Destello",bg=titleBack,fg="white",font=('Woodcut', 18,'italic'),height=2)
title.pack(fill=X)


bottomFrame = Frame(r,bg=back,padx=20,pady=30)
onOFFButton = Button(bottomFrame,text='Start',width=20,height=2,bg=titleBack,fg='white',font=(None,11,'bold'),border=0,command=onOFF)
onOFFButton.pack(side=RIGHT)
bottomFrame.pack(side=BOTTOM,fill=X)

r.mainloop() 
