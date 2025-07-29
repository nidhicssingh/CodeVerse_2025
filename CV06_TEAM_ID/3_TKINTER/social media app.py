import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
from modules import send_post, like_post, comment_post, profile_system

# Initialize Main App
app = tk.Tk()
app.title("NITHYA'S SOCIAL HUB")
app.geometry("900x700")
app.configure(bg="#f8f9fa")  # Set main window background color

# Style Configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=8, relief="flat", font=("Segoe UI", 12, "bold"), background="#007bff", foreground="white")
style.map("TButton", background=[("active", "#0056b3")])
style.configure("TLabel", font=("Segoe UI", 12), background="white")
style.configure("TFrame", background="white")

# Custom Fonts
TITLE_FONT = ("Segoe UI", 24, "bold")
SUBTITLE_FONT = ("Segoe UI", 14, "bold")
BODY_FONT = ("Segoe UI", 12)

# Frames
frame_top = tk.Frame(app, bg="#343a40", height=60)
frame_top.pack(fill=tk.X)

frame_content = tk.Frame(app, bg="#f8f9fa")  # Match main window background
frame_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Title
title = tk.Label(frame_top, text="NITHYA'S SOCIAL HUB", fg="white", bg="#343a40", font=TITLE_FONT)
title.pack(pady=10)

# Post Frame
post_frame = tk.LabelFrame(frame_content, text="Share Your Thoughts", font=SUBTITLE_FONT, padx=15, pady=15, bg="white", bd=2, relief="flat")
post_frame.pack(pady=10, padx=10, fill=tk.X)

post_text = tk.Text(post_frame, height=5, width=70, font=BODY_FONT, bd=1, relief="solid", wrap="word")
post_text.pack(pady=10)

image_path = None
def upload_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        messagebox.showinfo("Image Selected", f"Selected: {os.path.basename(image_path)}")

def post():
    content = post_text.get("1.0", tk.END).strip()
    if content:
        send_post.create_post(content, image_path)
        messagebox.showinfo("Success", "Your post has been shared!")
        render_feed()
        post_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Empty Post", "Please write something before posting.")

# Buttons with hover effect
def on_enter(e, btn): btn.config(bg="#a71d2a" if btn["text"].startswith(("❤️", "💬")) else "#0056b3")
def on_leave(e, btn): btn.config(bg="#dc3545" if btn["text"].startswith(("❤️", "💬")) else "#007bff")

upload_btn = tk.Button(post_frame, text="📷 Upload Image", command=upload_image, bg="#007bff", fg="white", font=BODY_FONT, relief="flat", cursor="hand2")
upload_btn.pack(side=tk.LEFT, padx=10)
upload_btn.bind("<Enter>", lambda e: on_enter(e, upload_btn))
upload_btn.bind("<Leave>", lambda e: on_leave(e, upload_btn))

post_btn = tk.Button(post_frame, text="Post", command=post, bg="#007bff", fg="white", font=BODY_FONT, relief="flat", cursor="hand2")
post_btn.pack(side=tk.RIGHT, padx=10)
post_btn.bind("<Enter>", lambda e: on_enter(e, post_btn))
post_btn.bind("<Leave>", lambda e: on_leave(e, post_btn))

# Feed Frame
feed_frame = tk.Frame(frame_content, bg="#f8f9fa")  # Match main window background
feed_frame.pack(fill=tk.BOTH, expand=True, padx=10)

post_widgets = []

def render_feed():
    for widget in post_widgets:
        widget.destroy()
    post_widgets.clear()
    for post in send_post.posts[::-1]:
        frame = tk.Frame(feed_frame, bg="white", padx=15, pady=15, bd=1, relief="solid")
        frame.pack(pady=10, fill=tk.X)

        user_label = tk.Label(frame, text=f"{post['user']}", font=("Segoe UI", 14, "bold"), bg="white", fg="#343a40")
        user_label.pack(anchor='w')
        content_label = tk.Label(frame, text=post['content'], font=BODY_FONT, wraplength=800, bg="white", fg="#212529", justify="left")
        content_label.pack(anchor='w', pady=5)

        if post['image']:
            try:
                img = Image.open(post['image'])
                img = img.resize((250, 250), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="white")
                img_label.image = photo
                img_label.pack(anchor='w', pady=5)
            except Exception as e:
                tk.Label(frame, text=f"[Error loading image: {e}]", fg="red", bg="white").pack(anchor='w')

        button_frame = tk.Frame(frame, bg="white")
        button_frame.pack(anchor='w', pady=5)
        like_btn = tk.Button(button_frame, text=f"❤️ {post['likes']}", font=BODY_FONT, command=lambda p=post: [like_post.like(p), render_feed()], bg="#dc3545", fg="white", relief="flat", cursor="hand2", padx=10, pady=5)
        like_btn.pack(side=tk.LEFT, padx=5)
        like_btn.bind("<Enter>", lambda e: on_enter(e, like_btn))
        like_btn.bind("<Leave>", lambda e: on_leave(e, like_btn))

        comment_btn = tk.Button(button_frame, text="💬 Comment", font=BODY_FONT, command=lambda p=post: comment_post.comment_window(app, p), bg="#dc3545", fg="white", relief="flat", cursor="hand2", padx=10, pady=5)
        comment_btn.pack(side=tk.LEFT, padx=5)
        comment_btn.bind("<Enter>", lambda e: on_enter(e, comment_btn))
        comment_btn.bind("<Leave>", lambda e: on_leave(e, comment_btn))

        if post["comments"]:
            tk.Label(frame, text="Comments:", font=("Segoe UI", 10, "italic"), bg="white", fg="#6c757d").pack(anchor='w', pady=5)
            for c in post["comments"]:
                tk.Label(frame, text=f"• {c['user']}: {c['text']}", font=BODY_FONT, bg="white", fg="#495057", wraplength=800, justify="left").pack(anchor='w', padx=10)

        post_widgets.append(frame)

# Profile View
def view_profile():
    window = tk.Toplevel(app)
    window.title("Profile: Nithya")
    window.geometry("600x700")
    window.configure(bg="#f8f9fa")  # Match main window background

    def edit_profile():
        edit_window = tk.Toplevel(window)
        edit_window.title("Edit Profile")
        edit_window.geometry("350x250")
        edit_window.configure(bg="white")

        tk.Label(edit_window, text="Name:", font=SUBTITLE_FONT, bg="white").pack(pady=10)
        name_entry = tk.Entry(edit_window, font=BODY_FONT, width=30)
        name_entry.insert(0, "Nithya")
        name_entry.pack()

        tk.Label(edit_window, text="Bio:", font=SUBTITLE_FONT, bg="white").pack(pady=10)
        bio_entry = tk.Entry(edit_window, font=BODY_FONT, width=30)
        bio_entry.insert(0, "Passionate developer.")
        bio_entry.pack()

        def save_profile():
            new_name = name_entry.get()
            new_bio = bio_entry.get()
            messagebox.showinfo("Profile Updated", f"Name: {new_name}\nBio: {new_bio}")
            edit_window.destroy()

        save_btn = tk.Button(edit_window, text="Save", command=save_profile, bg="#007bff", fg="white", font=BODY_FONT, relief="flat", cursor="hand2", padx=10, pady=5)
        save_btn.pack(pady=20)
        save_btn.bind("<Enter>", lambda e: on_enter(e, save_btn))
        save_btn.bind("<Leave>", lambda e: on_leave(e, save_btn))

    profile_header = tk.Frame(window, bg="#007bff")
    profile_header.pack(fill=tk.X)
    tk.Label(profile_header, text="👤 Nithya's Profile", font=TITLE_FONT, bg="#007bff", fg="white").pack(pady=15)

    tk.Button(window, text="✏️ Edit Profile", command=edit_profile, bg="#007bff", fg="white", font=BODY_FONT, relief="flat", cursor="hand2", padx=10, pady=5).pack(pady=10)

    posts = [p for p in send_post.posts if p["user"] == "Nithya"]

    for post in posts[::-1]:
        frame = tk.Frame(window, bg="white", padx=15, pady=15, bd=1, relief="solid")
        frame.pack(pady=10, fill=tk.X)

        tk.Label(frame, text=post['content'], font=BODY_FONT, wraplength=500, justify="left", bg="white", fg="#212529").pack(anchor="w", pady=5)

        if post['image']:
            try:
                img = Image.open(post['image'])
                img = img.resize((250, 250), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="white")
                img_label.image = photo
                img_label.pack(anchor='w', pady=5)
            except Exception as e:
                tk.Label(frame, text=f"[Error loading image: {e}]", fg="red", bg="white").pack(anchor='w')

        tk.Label(frame, text=f"❤️ {post['likes']} Likes | 💬 {len(post['comments'])} Comments", font=BODY_FONT, fg="#6c757d", bg="white").pack(anchor="w", pady=5)

        if post["comments"]:
            tk.Label(frame, text="All Comments:", font=("Segoe UI", 10, "italic"), bg="white", fg="#6c757d").pack(anchor='w', pady=5)
            for c in post["comments"]:
                tk.Label(frame, text=f"• {c['user']}: {c['text']}", font=BODY_FONT, bg="white", fg="#495057", wraplength=500, justify="left").pack(anchor='w', padx=10)

# Menu
menu = tk.Menu(app, font=BODY_FONT)
app.config(menu=menu)
menu.add_command(label="View Profile", command=view_profile)

render_feed()
app.mainloop()
