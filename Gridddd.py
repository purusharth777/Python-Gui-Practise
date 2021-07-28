from tkinter import *
root=Tk()

def getvall():
    print(f"The value of user is ={userentry.get()}")
    print(f"The value of password is {passentry.get()}")


root.geometry("600x333")
user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid()
password.grid(row=1)
uservale=StringVar()
passvale=StringVar()
userentry=Entry(root,textvariable=uservale)
passentry=Entry(root,textvariable=passvale)

userentry.grid(row=0,column=2)
passentry.grid(row=1,column=2)
Button(text="Click me",command=getvall).grid(row=3,column=3)





root.mainloop()
"""
Variable classes in tkinter
BooleanVar,DoubleVar,IntVar,StringVar
"""
"""
Grid is layout 

Entry is use to take entry
get() use to simplyfy the entry
"""