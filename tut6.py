from tkinter import *
root=Tk()
root.geometry("444x233")
root.title("My gui with harry")
# Important Label Options
# text -adds the text
# bd-background
# fd=foreground
# font-sets font
# font=("comicsansms",19,"bold")
# font="comicsansms 19 bold"
# padx-x padding
# pady-y padding
# relief- border styling - SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text="""Son Goku[nb 1] is a fictional character and 
\n main protagonist of the Dragon Ball manga series created by Akira Toriyama. 
\n He is based on Sun Wukong (known as Son Goku in Japan and Monkey King in the West),
 \n a main character in the classic Chinese novel Journey to the West (16th century), 
 \n combined with influences from the Hong Kong martial arts films of Jackie Chan 
 \n and Bruce Lee. Goku first made his debut in the first Dragon Ball chapter, 
 \n Bulma and Son Goku,[nb 2][nb 3] originally published in Japan's Weekly 
 \n Shōnen Jump magazine on December 3, 1984.[2] Born Kakarot,[nb 4][nb 5] 
 \n Goku is introduced as an eccentric, monkey-tailed boy who practices martial 
 \n arts and possesses superhuman strength. He meets Bulma and joins her on a 
 \n journey to find the magical seven Dragon Balls that can grant the user one wish. 
 \n Along the way, he finds new friends who follow him on his journey to become a stronger 
 \n fighter. As Goku grows up, he becomes the Earth's mightiest warrior and battles a wide 
\n  variety of villains with the help of his friends and family, while also gaining new allies in the process.\n 

As the protagonist of Dragon Ball, """,bg="yellow",fg="blue",padx=7,pady=7,font="GokuFont 19 bold",borderwidth=7,
                  relief=SUNKEN)

#Import Pack options
# anchor =nw
# side =top,bottom,left,right
# fill
# padx
# pady
"""
If i have to use south anchor==se,sw etc
i have to use side=BOTTOM  
"""
# title_label.pack(side=BOTTOM,anchor="sw",fill=X)
title_label.pack(side=LEFT,anchor="sw",fill=Y,padx=34,pady=55)





root.mainloop()

