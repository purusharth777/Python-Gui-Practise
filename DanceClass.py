from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry('500x500')
p=Image.open('8.jpg')
new_p=p.resize((400,400))
phot=ImageTk.PhotoImage(new_p)
label=Label(image=phot).pack()
nameval=StringVar()
ageval=StringVar()
contactval=StringVar()
nameentry=Entry(root,textvariable=nameval)
angentry=Entry(root,textvariable=ageval)
contactentry=Entry(root,textvariable=contactval)
Label(text="Name",font="Arial 17 bold").pack(anchor="w")
nameentry.pack(anchor='w')
Label(text="Age",font="Arial 17 bold").pack(anchor="w")
angentry.pack(anchor='w')
Label(text="Contact Number",font="Arial 17 bold").pack(anchor="w")
contactentry.pack(anchor='w')
Button(text="Submit",)



root.mainloop()