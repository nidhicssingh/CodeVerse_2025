import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

# --- Main Window Setup ---
root = tk.Tk()
root.title("Enhanced Mini Social Media - Teja")
root.geometry("550x700")
root.configure(bg="#E8F0FE")

posts = []

# --- Functions ---

def post_message():
    name = name_entry.get().strip()
    message = post_text.get("1.0", tk.END).strip()
    emoji = emoji_var.get()

    if name and message:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        posts.append({"name": name, "message": message, "likes": 0, "emoji": emoji, "time": timestamp})
        name_entry.delete(0, tk.END)
        post_text.delete("1.0", tk.END)
        char_count_var.set("0/200")
        display_posts()
    else:
        messagebox.showwarning("Empty Fields", "Please enter both name and message.")

def like_post(index):
    if 0 <= index < len(posts):
        posts[index]['likes'] += 1
        display_posts()

def delete_post(index):
    if 0 <= index < len(posts):
        confirm = messagebox.askyesno("Delete Post", "Are you sure you want to delete this post?")
        if confirm:
            posts.pop(index)
            display_posts()

def update_char_count(event=None):
    current_len = len(post_text.get("1.0", tk.END).strip())
    char_count_var.set(f"{current_len}/200")
    if current_len > 200:
        char_count_label.config(fg="red")
    else:
        char_count_label.config(fg="#1A5276")

def display_posts():
    for widget in posts_frame.winfo_children():
        widget.destroy()

    for idx, post in enumerate(reversed(posts)):
        original_idx = len(posts) - 1 - idx
        post_frame = tk.Frame(posts_frame, bg="#FFFFFF", padx=10, pady=8, bd=1, relief="solid")
        post_frame.pack(fill="x", pady=8, padx=5)

        title = f"{post['emoji']} {post['name']} says:"
        name_label = tk.Label(post_frame, text=title, font=("Arial", 11, "bold"), bg="#FFFFFF", fg="#1A5276")
        name_label.pack(anchor="w")

        time_label = tk.Label(post_frame, text=post['time'], font=("Arial", 8), bg="#FFFFFF", fg="#888888")
        time_label.pack(anchor="w")

        message_label = tk.Label(post_frame, text=post['message'], font=("Arial", 10), bg="#FFFFFF",
                                 fg="#333333", wraplength=450, justify="left")
        message_label.pack(anchor="w", pady=(5, 5))

        button_frame = tk.Frame(post_frame, bg="#FFFFFF")
        button_frame.pack(anchor="e", fill="x")

        like_btn = tk.Button(button_frame, text=f"❤ {post['likes']}", font=("Arial", 9, "bold"),
                             bg="#FFB6C1", fg="#C70039", activebackground="#FF4C4C", relief="raised",
                             command=lambda i=original_idx: like_post(i))
        like_btn.pack(side="right", padx=(0, 5))

        del_btn = tk.Button(button_frame, text="🗑", font=("Arial", 9), bg="#FFDDDD", fg="black",
                            command=lambda i=original_idx: delete_post(i))
        del_btn.pack(side="right", padx=5)

# --- Widgets ---

tk.Label(root, text="Your Name:", font=("Arial", 12, "bold"), bg="#E8F0FE", fg="#1A5276").pack(pady=(15, 0))
name_entry = tk.Entry(root, font=("Arial", 12), width=40, bd=2, relief="groove")
name_entry.pack(pady=5)

tk.Label(root, text="Choose Emoji:", font=("Arial", 12, "bold"), bg="#E8F0FE", fg="#1A5276").pack()
emoji_var = tk.StringVar(value="🙂")
emoji_menu = tk.OptionMenu(root, emoji_var, "🙂", "😎", "🤩", "😂", "😡", "😭", "😍", "🤔")
emoji_menu.config(font=("Arial", 10), bg="#FFFFFF", fg="#333333")
emoji_menu.pack(pady=5)

tk.Label(root, text="Write a Post:", font=("Arial", 12, "bold"), bg="#E8F0FE", fg="#1A5276").pack(pady=(10, 0))
post_text = scrolledtext.ScrolledText(root, width=55, height=5, font=("Arial", 11), wrap="word")
post_text.pack(pady=5)
post_text.bind("<KeyRelease>", update_char_count)

# Character Counter
char_count_var = tk.StringVar(value="0/200")
char_count_label = tk.Label(root, textvariable=char_count_var, font=("Arial", 9), bg="#E8F0FE", fg="#1A5276")
char_count_label.pack()

post_button = tk.Button(
    root,
    text="Share Post",
    font=("Arial", 13, "bold"),
    bg="#34A853",
    fg="white",
    activebackground="#2B8E44",
    relief="raised",
    bd=3,
    cursor="hand2",
    command=post_message
)
post_button.pack(pady=15, ipadx=20, ipady=5)

posts_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief="sunken")
posts_frame.pack(fill="both", expand=True, padx=15, pady=10)

display_posts()
root.mainloop()
