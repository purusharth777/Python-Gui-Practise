from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}") # It will be add item from top
    # lbx.insert(END,"iTEM") # It will add item from buttom
    i+=1
i=0
root=Tk()
root.geometry("455x455")
root.title("ListBox")

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"1ST item of  our listbox ")

Button(root,text="Add Item",command=add).pack()





root.mainloop()