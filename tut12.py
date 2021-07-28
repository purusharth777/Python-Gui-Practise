from tkinter import *
root= Tk()

root.geometry('644x344')
def getvals():
    print("Submitting form")
    with open("records.txt","a") as f:
        f.write(f"Name={nameval.get()}\n"
                f"Phone={phoneval.get()}\n"
                f"Gender={genderval.get()}\n"
                f"Emergency={emergencyval.get()}\n"
                f"PaymentMod={paymodval.get()} \n")
        if(foodserviceval.get()==1):
            f.write("Khana Mang rahe hai bhukhe \n\n\n\n\n\n\n\n")
        else:
            f.write("Khana nhi dena kutte ko\n\n\n\n\n\n\n\n")



#----------------------------------------> HEADING <-------------------------

Label(root,text="Welcome to Puru industry",font="Arial 13 bold",pady=17).grid(row=0,column=3)

#----------------------------------------> TEXT FOR MY FORM<-------------------

name=Label(root ,text="Name")
phone=Label(root ,text="phone")
gender=Label(root ,text="gender")
emergency=Label(root ,text="emergency")
paymode=Label(root ,text="Payment Mode")

#--------------------------------------->PACK IN THE GRID FORM<-------------------------

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymode.grid(row=5,column=2)

# -------------------------->VARIABLES TO TAKE ENTRY<--------------------------------------

nameval=StringVar()
phoneval=StringVar()
genderval=StringVar()
emergencyval=StringVar()
paymodval=StringVar()
foodserviceval=IntVar()

# --------------------------->ENTRY FOR MY FORM <----------------------------------------

nameentry=Entry(root,textvariable=nameval)
phoneentry=Entry(root,textvariable=phoneval)
genderentry=Entry(root,textvariable=genderval)
emergencyentry=Entry(root,textvariable=emergencyval)
paymodentry=Entry(root,textvariable=paymodval)

# ------------------------------------------------>PACKING ENTRIES<-----------------------------

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2 ,column=3)
genderentry.grid(row=3 ,column=3)
emergencyentry.grid(row=4 ,column=3)
paymodentry.grid(row=5 ,column=3)

#-------------------------------->CHECKBOX<------------------
foodservice=Checkbutton(text="Want to prebook your meal",variable=foodserviceval)
foodservice.grid(row=6,column=3)

# ----------------------------------->BUTTON AND ASSIGNING IT A COMMAND<-----------------------
Button(text="Done",font="Arial 17 bold",bg="CYAN",fg="YELLOW",command=getvals).grid(row=7,column=3)



root.mainloop()