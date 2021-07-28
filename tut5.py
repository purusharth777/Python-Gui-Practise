from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("700x700")
# photo=PhotoImage(file="8.jpg")

# For jpg images
image=Image.open("8.jpg")
photo= ImageTk.PhotoImage(image)

abel=Label(image=photo)
abel.pack()
root.mainloop()