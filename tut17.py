from tkinter import *
root=Tk()
root.geometry("733x566")
root.title("Pycharm")
def myfunc():
    print("Mai ek function")
# Use these to create non dropdown menu
# my_menu=Menu(root)
# my_menu.add_command(label="file",command=myfunc)
# my_menu.add_command(label="Exit",command=quit)
# root.config(menu=my_menu)
yourmenubar=Menu(root)

m1=Menu(yourmenubar,tearoff=0)

m1.add_command(label="New Project",command=myfunc)
m1.add_separator()
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
m2=Menu(yourmenubar)
m2.add_command(label="New Project",command=myfunc)
m2.add_command(label="Save",command=myfunc)
m2.add_command(label="Save as",command=myfunc)
m2.add_command(label="Print",command=myfunc)
yourmenubar.add_cascade(label="File",menu=m1)
yourmenubar.add_cascade(label="Edit",menu=m2)
yourmenubar.add_command(label="exit",command=quit)
root.config(menu=yourmenubar)

root.mainloop()