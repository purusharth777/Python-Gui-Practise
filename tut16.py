from tkinter import *
root=Tk()
def geo():
    root.geometry(f"{heightval.get()}x{brethval.get()}")
Label(text="Height").grid()
Label(text="Breath").grid()
Button(text="Apply",command=geo).grid()
heightval=StringVar()
brethval=StringVar()
heightEntry=Entry(root,textvariable=heightval)
breathEntry=Entry(root,textvariable=brethval)
heightEntry.grid(row=0,column=1)
breathEntry.grid(row=1,column=1)
root.mainloop()