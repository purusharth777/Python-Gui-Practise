from tkinter import *
import tkinter.messagebox as tmg
root=Tk()
def order():
    tmg.showinfo("Order Recieved",f"We have recieved your {var.get()}")

root.geometry("455x455")
root.title("Radio Button ")
var=IntVar()
# var.set(1)

Label(root,text="What would like to have?? ",font="lucida 19 bold",justify=LEFT,padx=14).pack()

radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack()
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value=2).pack()
radio=Radiobutton(root,text="idly",padx=14,variable=var,value=3).pack()
radio=Radiobutton(root,text="Parantha",padx=14,variable=var,value=4).pack()

Button(text="Order now",command=order).pack()



root.mainloop()
