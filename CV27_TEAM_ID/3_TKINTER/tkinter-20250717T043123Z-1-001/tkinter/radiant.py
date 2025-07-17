# Importing tkinter module 
from tkinter import *
# Importing random module
import random

# Creating a tkinter window
root = Tk() 

# Initialize tkinter window with dimensions 300 x 250
root.geometry('300x250')

# Creating a Button
btn = Button(root, text = 'Click me !')
btn.pack()

# Defining method on click
def Clicked(event):
    x = random.randint(50,250)
    y = random.randint(50,200)
    btn.place(x=x, y=y)
    
    
# bind button
btn.bind("<Button-1>" ,Clicked)
btn.pack()

root.mainloop()