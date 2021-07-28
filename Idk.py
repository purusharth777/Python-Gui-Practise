from tkinter import *
import pandas as pd
root=Tk()


def party1adder():
    pass
def party1subtractor():
    pass
def amount():
    amount = Tk()
    amount.title("Add amount")
    amount.geometry("500x500")



    def part1():
        def getval():


            pro = amountval.get() *quatityval.get()
            print(pro)



           
        Label(amount, text="Enter the amount").grid(row=1, column=0)
        amountval = IntVar()
        amountEntry = Entry(amount, textvariable=amountval)
        amountEntry.grid(row=1, column=1)


        Label(amount, text="Enter the Quatiy").grid(row=2, column=0)
        quatityval = IntVar()
        quantityEntry = Entry(amount, textvariable=quatityval)
        quantityEntry.grid(row=2, column=1)




        a=Button(amount, text="Add", command=party1adder).grid(row=4, column=1)
        b=Button(amount, text="Subtract", command=party1subtractor).grid(row=4, column=2)
        Button(amount,text="Calulate",command=getval).grid(row=4,column=3)

















    Button(amount, text="Party1", command=part1).grid(row=3, column=0)
    Button(amount, text="Party2", command=part1).grid(row=3, column=1)
    Button(amount, text="Party3", command=part1).grid(row=3, column=2)
    Button(amount, text="Party4", command=part1).grid(row=3, column=3)

    amount.mainloop()

    pass
root.geometry("500x500")
Label(text="What do you want to do ").pack()
Button(text="Add amount", command=amount).pack()

Button(text="Add Stock").pack()
root.mainloop()