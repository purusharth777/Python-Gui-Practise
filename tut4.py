from tkinter import *
root=Tk()
root.geometry("777x400")       #Widhth X Height
root.minsize(200,100)          #Widhth , Height
root.maxsize(500,700)
label=Label(text="Hello Gui ")
label.pack()
root.mainloop()