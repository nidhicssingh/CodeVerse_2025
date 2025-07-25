import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
import os

class SocialMediaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🌐 PySocial - Connect & Share")
        self.master.geometry("640x720")
        self.master.configure(bg="#f0f2f5")

        self.posts = {}
        self.post_id = 1
        self.images = {}
        self.image_path = None

        # Header banner
        header = tk.Canvas(master, width=640, height=60, bg="#3b5998", highlightthickness=0)
        header.pack(fill="x")
        header.create_text(320, 30, text="🐍 PySocial Network", fill="white", font=("Helvetica", 22, "bold"))

        # Input section
        form_frame = tk.Frame(master, bg="#f0f2f5")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="👤 Username:", bg="#f0f2f5", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5)
        self.user_entry = tk.Entry(form_frame, width=30, font=("Arial", 11))
        self.user_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="💬 What's on your mind?", bg="#f0f2f5", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5)
        self.post_entry = tk.Entry(form_frame, width=50, font=("Arial", 11))
        self.post_entry.grid(row=1, column=1, pady=5)

        # Action buttons
        button_frame = tk.Frame(master, bg="#f0f2f5")
        button_frame.pack(pady=5)

        self.attach_btn = tk.Button(button_frame, text="📎 Attach Image", bg="#4CAF50", fg="white", font=("Arial", 10), command=self.select_image)
        self.attach_btn.pack(side="left", padx=8)
        self.post_btn = tk.Button(button_frame, text="🚀 Post", bg="#1877F2", fg="white", font=("Arial", 10), command=self.create_post)
        self.post_btn.pack(side="left")

        # Scrollable feed
        self.canvas = tk.Canvas(master, bg="#e9ebee", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#e9ebee")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.load_data()

    def select_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
        if path:
            self.image_path = path
            messagebox.showinfo("✅ Image Attached", os.path.basename(path))

    def create_post(self):
        user = self.user_entry.get().strip()
        content = self.post_entry.get().strip()
        if not user or not content:
            messagebox.showwarning("⚠️ Input Missing", "Please enter your name and a post.")
            return

        self.posts[self.post_id] = {
            "user": user,
            "content": content,
            "likes": 0,
            "comments": [],
            "image": self.image_path
        }

        self.post_id += 1
        self.image_path = None
        self.user_entry.delete(0, tk.END)
        self.post_entry.delete(0, tk.END)
        self.refresh_posts()
        self.save_data()

    def refresh_posts(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        for pid in sorted(self.posts.keys(), reverse=True):
            self.display_post(pid)

    def display_post(self, post_id):
        post = self.posts[post_id]
        card = tk.Frame(self.scrollable_frame, bg="white", bd=2, relief="groove", padx=10, pady=10)
        card.pack(padx=15, pady=10, fill="x")

        tk.Label(card, text=f"👤 {post['user']}", bg="white", font=("Arial", 11, "bold")).pack(anchor="w")
        tk.Label(card, text=post['content'], bg="white", wraplength=500, font=("Arial", 10)).pack(anchor="w", pady=2)

        if post.get("image") and os.path.exists(post["image"]):
            try:
                img = Image.open(post["image"])
                img.thumbnail((260, 260))
                tk_img = ImageTk.PhotoImage(img)
                self.images[post_id] = tk_img
                tk.Label(card, image=tk_img, bg="white").pack(anchor="w", pady=5)
            except Exception as e:
                print("Image Load Error:", e)

        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(anchor='w', pady=4)

        tk.Button(btn_frame, text=f"👍 Like ({post['likes']})", bg="#1877F2", fg="white",
                  command=lambda pid=post_id: self.like_post(pid)).pack(side="left", padx=3)
        tk.Button(btn_frame, text="✏️ Edit", bg="#ff9800", command=lambda pid=post_id: self.edit_post(pid)).pack(side="left", padx=3)
        tk.Button(btn_frame, text="🗑️ Delete", bg="#f44336", fg="white", command=lambda pid=post_id: self.delete_post(pid)).pack(side="left", padx=3)

        for cmt in post["comments"]:
            tk.Label(card, text=f"💬 {cmt}", bg="white", fg="gray", font=("Arial", 9)).pack(anchor="w", padx=10)

        comment_entry = tk.Entry(card, width=40, font=("Arial", 10))
        comment_entry.insert(0, "Add a comment...")
        comment_entry.bind("<FocusIn>", lambda e, entry=comment_entry: entry.delete(0, tk.END))
        comment_entry.pack(anchor="w", pady=5)

        tk.Button(card, text="💬 Comment", bg="#34A853", fg="white",
                  command=lambda pid=post_id, entry=comment_entry: self.add_comment(pid, entry)).pack(anchor="w")

    def like_post(self, post_id):
        self.posts[post_id]["likes"] += 1
        self.refresh_posts()
        self.save_data()

    def edit_post(self, post_id):
        current = self.posts[post_id]["content"]

        def save():
            updated = edit_entry.get().strip()
            if updated:
                self.posts[post_id]["content"] = updated
                self.refresh_posts()
                self.save_data()
                popup.destroy()

        popup = tk.Toplevel(self.master)
        popup.title("Edit Post")
        edit_entry = tk.Entry(popup, width=50)
        edit_entry.insert(0, current)
        edit_entry.pack(padx=10, pady=10)
        tk.Button(popup, text="Save", command=save).pack(pady=5)

    def delete_post(self, post_id):
        if messagebox.askyesno("Confirm", "Delete this post?"):
            del self.posts[post_id]
            self.refresh_posts()
            self.save_data()

    def add_comment(self, post_id, entry):
        comment = entry.get().strip()
        if comment:
            self.posts[post_id]["comments"].append(comment)
            self.refresh_posts()
            self.save_data()

    def save_data(self):
        with open("posts.json", "w") as f:
            json.dump(self.posts, f)

    def load_data(self):
        if os.path.exists("posts.json"):
            with open("posts.json", "r") as f:
                data = json.load(f)
            self.posts = {int(k): v for k, v in data.items()}
            self.post_id = max(self.posts.keys(), default=0) + 1
            self.refresh_posts()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaApp(root)
    root.mainloop()
