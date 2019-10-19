import tkinter as tk
from tkinter import *

back = '#454647'
titleBack = '#343b80'
startClick = 0

r =tk.Tk()
contentFrame = Frame(r, bg=back)
class eyeDetails :
	def __init__(self) :
		global contentFrame
		contentFrame.destroy()
		contentFrame = Frame(r, bg=back)
		title = Label(contentFrame, text = "Eye Details")
		title.pack(side = TOP)
		contentFrame.pack(side = TOP, fill=BOTH, expand=True)
		contentFrame.tkraise()


class history :
	def __init__(self) :
		global contentFrame
		contentFrame.destroy()
		contentFrame = Frame(r, bg=back)
		title = Label(contentFrame, text = "History")
		title.pack(side = TOP)
		contentFrame.pack(side = TOP,fill=BOTH,expand=True)

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

r.title('Destello')
r.configure(background=back)
r.geometry("800x600")

titleFrame = Frame(r,bg=titleBack)
titleFrame.pack(side=TOP, fill=X,ipady=2)

title = Label(titleFrame,text="Destello",bg=titleBack,fg="white",font=('Woodcut', 18,'italic'))
title.pack(fill=X)

topdown = Frame(r,height=10)
eyeHealthButton = Button(topdown, text = 'Eye Health',width=20,height=2,bg="green",relief=SUNKEN,fg='white',font=(None,11,'bold'),border=0, command=eyeDetails) # add command to execute
eyeHealthButton.pack(side=LEFT, padx = 8, pady = 10, fill=X)

seperator = Label(topdown, text = ' History ',width=20,height=2,bg="green",relief=SUNKEN,fg='white',font=(None,11,'bold'),border=0)
seperator.pack(side = LEFT, padx = 8, pady = 10)

historyOptions = StringVar(r)
historyOptions.set("Select") # default value

def on_field_change(*args):
	print("value changed to " + historyOptions.get())
	history()
historyOptions.trace('w', on_field_change)

historyDropdown = OptionMenu(topdown, historyOptions, "Past 24 hrs", "Past 30 days ") # add command to execute
historyDropdown.pack(side = LEFT, padx = 8, pady = 10)
addExceptionAppButton = Button(topdown, text = "Add exception app") # add command to execute
addExceptionAppButton.pack(side=LEFT, padx = 8, pady = 3)

logoutButton = Button(topdown, text = "Logout") # add command to execute
logoutButton.pack(side=LEFT, padx = 8, pady = 3, fill=X)

topdown.pack(side=TOP, fill=X)




bottomFrame = Frame(r,bg=back,padx=20,pady=30)
onOFFButton = Button(bottomFrame,text='Start',width=20,height=2,bg=titleBack,fg='white',font=(None,11,'bold'),border=0,command=onOFF)
onOFFButton.pack(side=RIGHT)
bottomFrame.pack(side=BOTTOM,fill=X)

r.mainloop()