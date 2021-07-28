from tkinter import *
root=Tk()
root.geometry("455x455")
root.title("Title of my GUI")
root.wm_iconbitmap("9.ico")
root.config(background="Red")
width=root.winfo_screenmmwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="Close",command=root.destroy).pack()

root.mainloop()