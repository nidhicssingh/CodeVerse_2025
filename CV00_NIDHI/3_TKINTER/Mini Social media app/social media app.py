# main.py
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
from modules import send_post, like_post, comment_post, profile_system

# Initialize Main App
app = tk.Tk()
app.title("PySocial Media")
app.geometry("800x600")
app.configure(bg="#f0f2f5")

# Style
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#4CAF50", font=("Arial", 12))

# Frames
frame_top = tk.Frame(app, bg="#3b5998", height=50)
frame_top.pack(fill=tk.X)

frame_content = tk.Frame(app, bg="white")
frame_content.pack(fill=tk.BOTH, expand=True)

# Title
title = tk.Label(frame_top, text="PySocial", fg="white", bg="#3b5998", font=("Helvetica", 20, "bold"))
title.pack(pady=5)

# Post Frame
post_frame = tk.LabelFrame(frame_content, text="Create Post", padx=10, pady=10, bg="white")
post_frame.pack(pady=10)

post_text = tk.Text(post_frame, height=4, width=60, font=("Arial", 12))
post_text.pack()

image_path = None
def upload_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        messagebox.showinfo("Image Selected", f"Selected: {image_path}")

def post():
    content = post_text.get("1.0", tk.END).strip()
    if content:
        send_post.create_post(content, image_path)
        messagebox.showinfo("Posted", "Your post has been published.")
        render_feed()
        post_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Empty", "Please write something before posting.")

tk.Button(post_frame, text="Upload Image", command=upload_image).pack(side=tk.LEFT, padx=5)
tk.Button(post_frame, text="Post", command=post).pack(side=tk.RIGHT, padx=5)

# Feed Frame
feed_frame = tk.Frame(frame_content, bg="white")
feed_frame.pack(fill=tk.BOTH, expand=True)

post_widgets = []

def render_feed():
    for widget in post_widgets:
        widget.destroy()
    post_widgets.clear()
    for post in send_post.posts[::-1]:
        frame = tk.Frame(feed_frame, bg="#e9ebee", padx=10, pady=10)
        frame.pack(pady=5, fill=tk.X)

        tk.Label(frame, text=f"{post['user']}", font=("Arial", 10, "bold"), bg="#e9ebee").pack(anchor='w')
        tk.Label(frame, text=post['content'], wraplength=700, bg="#e9ebee", justify="left").pack(anchor='w')
        if post['image']:
            try:
                img = Image.open(post['image'])
                img = img.resize((200, 200))
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="#e9ebee")
                img_label.image = photo
                img_label.pack(anchor='w')
            except Exception as e:
                tk.Label(frame, text=f"[Error loading image: {e}]", fg="red", bg="#e9ebee").pack(anchor='w')

        tk.Button(frame, text=f"❤️ {post['likes']}", command=lambda p=post: [like_post.like(p), render_feed()]).pack(side=tk.LEFT)
        tk.Button(frame, text="Comment", command=lambda p=post: comment_post.comment_window(app, p)).pack(side=tk.LEFT, padx=5)

        if post["comments"]:
            tk.Label(frame, text="Comments:", font=("Arial", 10, "italic"), bg="#e9ebee").pack(anchor='w')
            for c in post["comments"]:
                tk.Label(frame, text=f"- {c['user']}: {c['text']}", bg="#e9ebee", wraplength=700, justify="left").pack(anchor='w')

        post_widgets.append(frame)

# Profile View
def view_profile():
    window = tk.Toplevel(app)
    window.title("Profile: Nidhi")
    window.geometry("500x600")
    window.configure(bg="white")

    def edit_profile():
        edit_window = tk.Toplevel(window)
        edit_window.title("Edit Profile")
        edit_window.geometry("300x200")

        tk.Label(edit_window, text="Name:").pack(pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, "Nidhi")
        name_entry.pack()

        tk.Label(edit_window, text="Bio:").pack(pady=5)
        bio_entry = tk.Entry(edit_window)
        bio_entry.insert(0, "Passionate developer.")
        bio_entry.pack()

        def save_profile():
            new_name = name_entry.get()
            new_bio = bio_entry.get()
            messagebox.showinfo("Profile Updated", f"Name: {new_name}\nBio: {new_bio}")
            edit_window.destroy()

        tk.Button(edit_window, text="Save", command=save_profile).pack(pady=10)

    tk.Label(window, text="👤 Nidhi's Profile", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
    tk.Button(window, text="✏️ Edit Profile", command=edit_profile, bg="#4CAF50", fg="white").pack(pady=5)

    posts = [p for p in send_post.posts if p["user"] == "Nidhi"]

    for post in posts[::-1]:
        frame = tk.Frame(window, bg="#f5f6fa", padx=10, pady=10)
        frame.pack(pady=5, fill=tk.X)

        tk.Label(frame, text=post['content'], wraplength=450, justify="left", bg="#f5f6fa").pack(anchor="w")

        if post["image"]:
            try:
                img = Image.open(post["image"])
                img = img.resize((200, 200))
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="#f5f6fa")
                img_label.image = photo
                img_label.pack(anchor='w')
            except Exception as e:
                tk.Label(frame, text=f"[Error loading image: {e}]", fg="red", bg="#f5f6fa").pack(anchor='w')

        tk.Label(frame, text=f"❤️ {post['likes']} Likes | 💬 {len(post['comments'])} Comments", fg="gray", bg="#f5f6fa").pack(anchor="w")

        if post["comments"]:
            tk.Label(frame, text="All Comments:", font=("Arial", 10, "italic"), bg="#f5f6fa").pack(anchor='w')
            for c in post["comments"]:
                tk.Label(frame, text=f"- {c['user']}: {c['text']}", bg="#f5f6fa", wraplength=450, justify="left").pack(anchor='w')

menu = tk.Menu(app)
app.config(menu=menu)
menu.add_command(label="View Profile", command=view_profile)

render_feed()
app.mainloop()
