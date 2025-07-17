from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Transparent Layout Over Background")
root.geometry("800x600")

# Set background image
bg_image = Image.open("a.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# Use label as background
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 1. Label
label = Label(root, text="Welcome to Tkinter UI", font=("Arial", 16), bg='#ed2e2e')
label.place(x=250, y=20)

# 2. Entry
entry = Entry(root, width=40)
entry.place(x=250, y=60)

# 3. Button
button = Button(root, text="Submit", command=lambda: print("Submitted"))
button.place(x=300, y=100)

# 4. Checkbutton
check_var = IntVar()
checkbutton = Checkbutton(root, text="Accept Terms", variable=check_var, bg='white')
checkbutton.place(x=250, y=140)

# 5. Radiobuttons
radio_var = StringVar(value="A")
radio1 = Radiobutton(root, text="Option A", variable=radio_var, value="A", bg='white')
radio2 = Radiobutton(root, text="Option B", variable=radio_var, value="B", bg='white')
radio1.place(x=250, y=180)
radio2.place(x=350, y=180)

# 6. Scale
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, bg='white')
scale.place(x=250, y=220)

# 7. Listbox
listbox = Listbox(root, height=4)
for item in ["Python", "Java", "C++", "JavaScript"]:
    listbox.insert(END, item)
listbox.place(x=250, y=280)

# 8. Text
text = Text(root, height=3, width=30)
text.insert(END, "Type something here...")
text.place(x=250, y=340)

# 9. Spinbox
spinbox = Spinbox(root, from_=1, to=10)
spinbox.place(x=250, y=410)

# 10. Label (Result)
result_label = Label(root, text="Result appears here", font=("Arial", 12), bg='white')
result_label.place(x=250, y=450)

root.mainloop()
