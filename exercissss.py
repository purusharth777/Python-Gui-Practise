from tkinter import *
root=Tk()
def wrie():
    with open("Ans.txt","a") as f:
        f.write(f"ans is {myslider.get()}")

root.geometry("455x455")
Label(root,text="rate experience ").pack()
myslider=Scale(root,from_=0,to=7,orient=HORIZONTAL)
myslider.pack()
Button(text="Click me ", command=wrie).pack()
root.mainloop()