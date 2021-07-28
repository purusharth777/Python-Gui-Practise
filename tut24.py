from tkinter import *
root=Tk()
def update():
    statusvar.set("Done")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")
root.geometry("455x455")
root.title("Seekbar ")

statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Update",command=update).pack()

root.mainloop()