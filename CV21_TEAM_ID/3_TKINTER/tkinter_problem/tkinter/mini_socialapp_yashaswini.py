import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
class InstaClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Codeverse_2025 - Mini Social App")
        self.root.geometry("550x700")
        self.root.config(bg="#fff")

        self.posts = []

        header = tk.Label(root, text="📸 Codeverse_2025", font=("Arial", 22, "bold"), bg="#fff", fg="#e1306c")
        header.pack(pady=10)

        # Upload + Caption area
        upload_frame = tk.Frame(root, bg="#fff")
        upload_frame.pack(pady=10)

        tk.Label(upload_frame, text="Caption:", font=("Arial", 12), bg="#fff").grid(row=0, column=0, sticky="w")
        self.caption_entry = tk.Entry(upload_frame, width=40)
        self.caption_entry.grid(row=0, column=1, padx=10)

        self.upload_btn = tk.Button(upload_frame, text="Upload Image", command=self.upload_image, bg="#3897f0", fg="white", font=("Arial", 10, "bold"))
        self.upload_btn.grid(row=1, column=0, columnspan=2, pady=10)

        # Feed area (scrollable)
        self.canvas = tk.Canvas(root, bg="#f5f5f5", width=520, height=500)
        self.frame = tk.Frame(self.canvas, bg="#f5f5f5")
        self.scroll = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)

        self.scroll.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if not file_path:
            return

        caption = self.caption_entry.get()
        if not caption:
            messagebox.showwarning("Missing Caption", "Please enter a caption before posting.")
            return

        image = Image.open(file_path)
        image.thumbnail((400, 400))
        img = ImageTk.PhotoImage(image)

        self.display_post(img, caption)
        self.caption_entry.delete(0, 'end')

    def display_post(self, img, caption):
        post_frame = tk.Frame(self.frame, bg="white", bd=2, relief="groove", padx=10, pady=5)
        post_frame.pack(padx=10, pady=10, fill="x")

        image_label = tk.Label(post_frame, image=img, bg="white")
        image_label.image = img
        image_label.pack()

        tk.Label(post_frame, text=caption, font=("Arial", 12), bg="white", wraplength=400, anchor="w", justify="left").pack(anchor="w", pady=5)

        action_frame = tk.Frame(post_frame, bg="white")
        action_frame.pack(anchor="w", pady=5)

        like_btn = tk.Button(action_frame, text="❤️ Like", command=lambda:self.like_action(like_btn), bg="#fff", border=0)
        like_btn.pack(side="left", padx=5)

        comment_btn = tk.Button(action_frame, text="💬 Comment", command=self.comment_action, bg="#fff", border=0)
        comment_btn.pack(side="left", padx=5)

        share_btn = tk.Button(action_frame, text="📤 Share", command=self.share_action, bg="#fff", border=0)
        share_btn.pack(side="left", padx=5)

    def like_action(self, button):
        if button["text"] == "❤️ Like":
            button.config(text="❤️ Liked", fg="#e1306c")
        else:
            button.config(text="❤️ Like", fg="black")

    def comment_action(self):
        messagebox.showinfo("Comment", "This would open a comment section!")

    def share_action(self):
        messagebox.showinfo("Share", "Post shared successfully!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = InstaClone(root)
    root.mainloop()