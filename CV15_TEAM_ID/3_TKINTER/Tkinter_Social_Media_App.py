import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
import os

class SocialMediaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Social Media App")
        self.posts = {}
        self.post_id = 1
        self.images = {}  # Store references to images
        self.image_path = None

        # User input section
        tk.Label(master, text="Username:").pack()
        self.user_entry = tk.Entry(master)
        self.user_entry.pack()

        tk.Label(master, text="What's on your mind?").pack()
        self.post_entry = tk.Entry(master, width=50)
        self.post_entry.pack()

        self.attach_btn = tk.Button(master, text="Attach Image", command=self.select_image)
        self.attach_btn.pack()

        self.post_btn = tk.Button(master, text="Post", command=self.create_post)
        self.post_btn.pack(pady=5)

        # Scrollable canvas for posts
        self.canvas = tk.Canvas(master)
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.load_data()

    def select_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
        )
        if path:
            self.image_path = path
            messagebox.showinfo("Image Selected", os.path.basename(path))

    def create_post(self):
        user = self.user_entry.get().strip()
        content = self.post_entry.get().strip()

        if not user or not content:
            messagebox.showwarning("Error", "Please enter username and content.")
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
        for pid in sorted(self.posts.keys()):
            self.display_post(pid)

    def display_post(self, post_id):
        post = self.posts[post_id]
        frame = tk.Frame(self.scrollable_frame, bd=2, relief="solid", padx=10, pady=5)
        frame.pack(pady=5, fill='x')

        tk.Label(frame, text=f"{post['user']} posted:", font=("Arial", 10, "bold")).pack(anchor='w')
        content_label = tk.Label(frame, text=post['content'], wraplength=400)
        content_label.pack(anchor='w')

        # Display image if available
        if post.get("image") and os.path.exists(post["image"]):
            try:
                img = Image.open(post["image"])
                img.thumbnail((200, 200))
                tk_img = ImageTk.PhotoImage(img)
                self.images[post_id] = tk_img  # Keep reference
                tk.Label(frame, image=tk_img).pack(anchor='w')
            except Exception as e:
                print("Image error:", e)

        # Buttons (Like, Edit, Delete)
        btn_frame = tk.Frame(frame)
        btn_frame.pack(anchor='e')

        like_btn = tk.Button(btn_frame, text=f"Like ({post['likes']})",
                             command=lambda pid=post_id: self.like_post(pid))
        like_btn.pack(side="left", padx=3)

        edit_btn = tk.Button(btn_frame, text="Edit",
                             command=lambda pid=post_id: self.edit_post(pid))
        edit_btn.pack(side="left", padx=3)

        delete_btn = tk.Button(btn_frame, text="Delete",
                               command=lambda pid=post_id: self.delete_post(pid))
        delete_btn.pack(side="left", padx=3)

        # Comments section
        for cmt in post["comments"]:
            tk.Label(frame, text=f"- {cmt}", fg="gray").pack(anchor='w')

        comment_entry = tk.Entry(frame, width=40)
        comment_entry.pack(anchor='w')
        tk.Button(frame, text="Add Comment",
                  command=lambda pid=post_id, entry=comment_entry: self.add_comment(pid, entry)).pack(anchor='w')

    def like_post(self, post_id):
        self.posts[post_id]['likes'] += 1
        self.refresh_posts()
        self.save_data()

    def edit_post(self, post_id):
        current_text = self.posts[post_id]["content"]

        def save_edit():
            new_text = edit_entry.get().strip()
            if new_text:
                self.posts[post_id]["content"] = new_text
                self.refresh_posts()
                self.save_data()
                edit_window.destroy()

        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Post")
        edit_entry = tk.Entry(edit_window, width=50)
        edit_entry.insert(0, current_text)
        edit_entry.pack(padx=10, pady=10)
        tk.Button(edit_window, text="Save", command=save_edit).pack(pady=5)

    def delete_post(self, post_id):
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this post?")
        if confirm:
            del self.posts[post_id]
            self.refresh_posts()
            self.save_data()

    def add_comment(self, post_id, entry):
        comment = entry.get().strip()
        if comment:
            self.posts[post_id]["comments"].append(comment)
            entry.delete(0, tk.END)
            self.refresh_posts()
            self.save_data()

    def save_data(self):
        with open("posts.json", "w") as f:
            json.dump(self.posts, f)

    def load_data(self):
        if os.path.exists("posts.json"):
            with open("posts.json", "r") as f:
                data = json.load(f)
            # Convert string keys to int for consistency
            self.posts = {int(k): v for k, v in data.items()}
            self.post_id = max(self.posts.keys(), default=0) + 1
            self.refresh_posts()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaApp(root)
    root.mainloop()
