from tkinter import *
class GUI(Tk):
    def __init__(self):             #Here root is self
        super().__init__()
        self.geometry("455x455")
    def newwind(self):
        Label(text="Hi").pack()

    def createButton(self,imptext):
        Button(text=imptext,command=self.newwind).pack()
if __name__ == '__main__':
    window=GUI()                    # Window is the object of the GUI class
    window.createButton("Hi")
    window.mainloop()
