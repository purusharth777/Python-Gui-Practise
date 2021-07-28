from tkinter import *
def puru(event):
    print(f"You clicked on the button at {event.x},{event.y}")# It tells the where button is clicked
root=Tk()
root.title("Events in Tkinter")
root.geometry("644x334")
widget=Button(root,text="Click me please")
widget.pack()
widget.bind("<Button-1>",puru)# Button clicked once
widget.bind("<Double-1>",quit)# Button clicked twice ## Quit automatically close the widget
root.mainloop()