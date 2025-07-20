from tkinter import *

# create root window
root = Tk()
# create root window
root = Tk()

# frame inside root window
frame = Frame(root,bg='red', bd=3, cursor='hand2', height=100, 
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', width=200)

# geometry method
frame.pack()

# button inside frame which is
# inside root
button = Button(frame, text='gousiya')
button.pack()# frame inside root window
frame = Frame(root,bg='red', bd=3, cursor='hand2', height=100, 
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', width=200)

# geometry method
frame.pack()
# button inside frame which is
# inside root

button = Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

# Tkinter event loop
root.mainloop()

