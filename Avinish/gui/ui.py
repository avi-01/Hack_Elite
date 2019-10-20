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

class loggedIn:
	def __init__(self):
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

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("400x200")
        self.label_email = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_email = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_email.grid(row=0, sticky=E,pady=(70,0))
        self.label_password.grid(row=1, sticky=E,pady=(10,0))
        self.entry_email.grid(row=0, column=1,pady=(70,0))
        self.entry_password.grid(row=1, column=1,pady=(10,0))

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2,pady=(30,0))

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        email = self.entry_email.get()
        password = self.entry_password.get()

        # print(email, password)

        url = "http://localhost:3001/users/login"
        # dic = '{"email":"'+email+'", "password":"'+password+'"}'
        dic = '{"email":"avnishmay@gmail.com", "password":"test1234"}'

        data = json.loads(dic)
        print(data)
        res = requests.post(url = url , json = data) 
        
        resJSON = json.loads(res.text) 
        if resJSON == {}:
            tm.showerror("Login error", "Incorrect email")
        else:
            print(resJSON['token']) 
        # if email == "john" and password == "password":
        #     tm.showinfo("Login info", "Welcome John")
        # else:
        #     tm.showerror("Login error", "Incorrect email")


class SignupFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("400x250")
        self.label_name = Label(self, text="Name")
        self.label_email = Label(self, text="Email")
        self.label_password = Label(self, text="Password")

        self.entry_name = Entry(self)
        self.entry_email = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_name.grid(row=0, sticky=E,pady=(70,0))
        self.label_email.grid(row=1, sticky=E,pady=(10,0))
        self.label_password.grid(row=2, sticky=E,pady=(10,0))
        self.entry_name.grid(row=0, column=1,pady=(70,0))
        self.entry_email.grid(row=1, column=1,pady=(10,0))
        self.entry_password.grid(row=2, column=1,pady=(10,0))

        self.signbtn = Button(self, text="Signup", command=self._signup_btn_clicked)
        self.signbtn.grid(columnspan=2,pady=(30,0))
        self.loginbtn = Button(self, text="Login", command=self._login_open)
        self.loginbtn.grid(row=3,column=2,pady=(30,0))

        self.pack()

    def _signup_btn_clicked(self):
        # print("Clicked")
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        # print(email, password)

        url = "http://localhost:3001/users"
        # dic = '{"name":"'+name+'","email":"'+email+'", "password":"'+password+'"}'
        dic = '{"name":"Avinish Kumar", "email":"avnish31may@gmail.com", "password":"test1234"}'

        data = json.loads(dic)
        print(data)
        res = requests.post(url = url , json = data) 
        
        resJSON = json.loads(res.text) 
        if resJSON == {}:
            tm.showerror("Signup error", "Incorrect data")
        else:
            print(resJSON['token']) 
        # if email == "john" and password == "password":
        #     tm.showinfo("Login info", "Welcome John")
        # else:
        #     tm.showerror("Login error", "Incorrect email")

    def _login_open(self):
        
        self.destroy
        lf = LoginFrame(root)

class log():
    def __init__(self):
        root = Tk()
        sf = SignupFrame(root)
        root.mainloop()