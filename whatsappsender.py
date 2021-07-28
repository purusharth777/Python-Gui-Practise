from tkinter import *
import pywhatkit as kit
root=Tk()
root.title("WhatsApp Sender ")



def setter():

    l=timeval.get().split(":")

    x=list(map(int,l))
    # print(l)
    kit.sendwhatmsg(f"+91{phoneval.get()}",f"{whatsppval.get()}",x[0],x[1])


    # print(type(x[0]))

root.geometry("700x700")
Label(text="Enter Whatsapp message").grid()
whatsppval=StringVar()
whatsEn=Entry(root,textvariable=whatsppval).grid()
Label(text="Enter the time").grid()
timeval=StringVar()
timeEn=Entry(root,textvariable=timeval).grid()
Label(text="Phone no.").grid()
phoneval=StringVar()
phoneEn=Entry(root,textvariable=phoneval).grid()

button=Button(text="Submit",command=setter)
button.grid()
root.mainloop()