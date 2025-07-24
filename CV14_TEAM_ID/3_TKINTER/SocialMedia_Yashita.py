import tkinter as tk

class Post:
    def __init__(self, content):
        self.content = content
        self.likes = 0

class SocialMediaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Social Media")
        self.root.geometry("400x500")

        self.posts = []

        self.entry = tk.Entry(root, font="Arial 14")
        self.entry.pack(pady=10, fill="x", padx=10)

        self.post_btn = tk.Button(root, text="Post", font="Arial 12", command=self.create_post)
        self.post_btn.pack(pady=5)

        self.feed_frame = tk.Frame(root)
        self.feed_frame.pack(fill="both", expand=True)

        self.refresh_feed()

    def create_post(self):
        content = self.entry.get().strip()
        if content:
            self.posts.insert(0, Post(content))  # Newest post at top
            self.entry.delete(0, tk.END)
            self.refresh_feed()

    def refresh_feed(self):
        for widget in self.feed_frame.winfo_children():
            widget.destroy()

        for post in self.posts:
            frame = tk.Frame(self.feed_frame, bd=2, relief=tk.RIDGE, padx=10, pady=5)
            frame.pack(fill="x", pady=5, padx=10)

            content_label = tk.Label(frame, text=post.content, font="Arial 12", wraplength=300, justify="left")
            content_label.pack(anchor="w")

            like_btn = tk.Button(frame, text=f"❤️ {post.likes}", command=lambda p=post: self.like_post(p))
            like_btn.pack(anchor="e")

    def like_post(self, post):
        post.likes += 1
        self.refresh_feed()

root = tk.Tk()
app = SocialMediaApp(root)
root.mainloop()
