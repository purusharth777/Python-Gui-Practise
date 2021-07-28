from tkinter import *
import tkinter.messagebox as tmg
root=Tk()
def getdollars():
    print(myslider2.get())
    tmg.showinfo("Amount credit",f"We have created {myslider2.get()}")
root.geometry("455x455")
root.title("Slider")
# myslider=Scale(root,from_=0,to=100)
# myslider.pack()
Label(text="How many dollars you want").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(7)

myslider2.pack()
Button(root,text="Get dollars",command=getdollars).pack()
root.mainloop()