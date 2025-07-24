import tkinter as tk
from tkinter import ttk

# List to hold posts
posts = []

def post_message():
    name = name_entry.get().strip()
    message = message_text.get("1.0", tk.END).strip()
    
    if name and message:
        full_post = f"{name} says:\n{message}\n" + "-"*40 + "\n"
        posts.append(full_post)
        update_feed()
        name_entry.delete(0, tk.END)
        message_text.delete("1.0", tk.END)

def update_feed():
    feed_text.config(state=tk.NORMAL)
    feed_text.delete("1.0", tk.END)
    for post in reversed(posts):
        feed_text.insert(tk.END, post)
    feed_text.config(state=tk.DISABLED)

# Main window
root = tk.Tk()
root.title("Mini Social Media App")
root.geometry("600x600")
root.configure(bg="#e6f2ff")

# Heading
heading = tk.Label(root, text="Welcome to Mini Social", font=("Arial", 20, "bold"), bg="#e6f2ff", fg="#003366")
heading.pack(pady=10)

# Frame for input
input_frame = tk.Frame(root, bg="#cce6ff", padx=20, pady=20, bd=2, relief=tk.RIDGE)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Your Name:", font=("Arial", 12), bg="#cce6ff").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Your Post:", font=("Arial", 12), bg="#cce6ff").grid(row=1, column=0, sticky="nw", pady=5)
message_text = tk.Text(input_frame, width=40, height=4, font=("Arial", 12))
message_text.grid(row=1, column=1, pady=5)

post_button = tk.Button(input_frame, text="Post", command=post_message, font=("Arial", 12, "bold"), bg="#007acc", fg="white", padx=10)
post_button.grid(row=2, column=1, pady=10, sticky="e")

# Frame for feed
feed_frame = tk.LabelFrame(root, text="📢 Feed", font=("Arial", 14, "bold"), bg="#e6f2ff", padx=10, pady=10)
feed_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Scrollbar and Text widget
scrollbar = tk.Scrollbar(feed_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

feed_text = tk.Text(feed_frame, wrap=tk.WORD, font=("Arial", 12), yscrollcommand=scrollbar.set, bg="#f7fbff", state=tk.DISABLED)
feed_text.pack(fill="both", expand=True)

scrollbar.config(command=feed_text.yview)

root.mainloop()
