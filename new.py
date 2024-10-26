from tkinter import *
from PIL import Image, ImageTk
import os

# Initialize Tkinter root
root = Tk()
root.geometry("1350x700+220+130")
root.title("Analysis History")
root.config(bg="#f0f1f8")
root.state('zoomed')





logo = PhotoImage(file="Images/First aid.png")
myimage = Label(root, image=logo, bg="#000")
myimage.pack(padx=0,pady=(1,0))  

call = Label(root, text="Call:911", bg="red",font="Arial 15")
call.place(relx=0.93, rely=0.23, anchor='w') 


instruct = PhotoImage(file="Images/Layer 2.png")
instruction = Label(root, image=instruct, bg="#f0f1f8")
instruction.place(relx=0.011, rely=0.58, anchor='w') 

instruct2 = PhotoImage(file="Images/Layer 3.png")
instruction2 = Label(root, image=instruct2, bg="#f0f1f8")
instruction2.place(relx=0.994, rely=0.58, anchor='e')  



root.mainloop()
