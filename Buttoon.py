from tkinter import *
root=Tk()

root.geometry("655x333")
x=7
y=5

f=Frame(root,borderwidth=6,bg="RED",relief=SUNKEN)
f.pack(side=LEFT,anchor="nw")
button=Button(f,text="Click here ",bg="BLUE",font="GokuFont 77 bold",command=lambda x=7,y=7:print(x+y))

button.pack(side=LEFT,padx=55)


root.mainloop()