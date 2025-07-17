
#pip install pillow

from tkinter import *
from PIL import Image, ImageTk  # Import from Pillow

root = Tk()
root.title("JPG Image in Tkinter")

# Load JPG image using PIL
image = Image.open("a.jpg")
photo = ImageTk.PhotoImage(image)

# Display image using Label
label = Label(root, image=photo)
label.pack()

root.mainloop()
