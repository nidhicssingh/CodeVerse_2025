import tkinter as tk
from modules import send_post # type: ignore

def view_profile(root):
    window = tk.Toplevel(root)
    window.title("Profile: Nishith")
    window.geometry("400x400")

    tk.Label(window, text="👤 Nishith's Profile", font=("Arial", 16, "bold")).pack(pady=10)

    posts = [p for p in send_post.posts if p["user"] == "Nishith"]

    for post in posts:
        frame = tk.Frame(window, bg="#f5f6fa", padx=5, pady=5)
        frame.pack(pady=5, fill=tk.X)
        tk.Label(frame, text=post['content'], wraplength=300, justify="left").pack(anchor="w")
        tk.Label(frame, text=f"❤️ {post['likes']} Likes | 💬 {len(post['comments'])} Comments", fg="gray").pack(anchor="w")
