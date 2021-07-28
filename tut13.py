from tkinter import *
root=Tk()
root.title("Puru canvas")
canvas_width=800
canvas_height=700
root.geometry(f"{canvas_width}x{canvas_height}")
canwi=Canvas(root,width=canvas_width,height=canvas_height)
canwi.pack()

# The line goes from the point x1,y1 to x2,y2
canwi.create_line(0,0,800,700,fill= "blue")
canwi.create_line(800,0,0,700,fill="magenta")

# The way to create rectangle to create a rectangle specify parameters in this order----Cordinates of top left and
# Cordinates of bottom right
# canwi.create_rectangle(3,5,700,300,fill='blue')
canwi.create_text(200,200,text="Purusharth")
canwi.create_oval(3,5,700,300) #we use four coordinates as rectangle
canwi.create_rectangle(100,100,400,400)

#

root.mainloop()
