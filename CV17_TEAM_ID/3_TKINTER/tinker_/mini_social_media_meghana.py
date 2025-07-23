import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class MiniSocialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("S-VYASA Deemed to be University")
        self.root.geometry("550x700")
        self.root.config(bg="#fff")
        self.posts = []

        tk.Label(root, text="S-VYASA Deemed to be University",
                 font=("Arial", 18, "bold"), fg="darkblue", bg="#fff"
        ).pack(pady=10)

        # Name + Caption + Upload UI
        top = tk.Frame(root, bg="#fff")
        top.pack(fill="x", pady=5, padx=10)
        tk.Label(top, text="Name:", bg="#fff").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(top, width=20, font="Arial 12")
        self.name_entry.grid(row=0, column=1, padx=5)
        tk.Label(top, text="Caption:", bg="#fff").grid(row=1, column=0, sticky="w")
        self.caption_entry = tk.Entry(top, width=30, font="Arial 12")
        self.caption_entry.grid(row=1, column=1, padx=5)
        tk.Button(top, text="Upload Image", bg="#3897f0", fg="#fff",
                  command=self.upload_image).grid(row=2, column=0, columnspan=2, pady=5)

        # Scrollable feed area
        self.canvas = tk.Canvas(root, bg="#f5f5f5", width=520, height=500)
        scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.feed_frame = tk.Frame(self.canvas, bg="#f5f5f5")
        self.canvas.create_window((0,0), window=self.feed_frame, anchor="nw")
        self.feed_frame.bind("<Configure>",
                             lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def upload_image(self):
        name = self.name_entry.get().strip()
        caption = self.caption_entry.get().strip()
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg;*.jpeg")])
        if not (name and caption and path):
            messagebox.showwarning("Missing Info",
                                   "Please enter name, caption, and select an image.")
            return

        img = Image.open(path)
        img.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(img)
        self.posts.append((name, photo, caption))
        self.display_posts()
        self.caption_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)

    def display_posts(self):
        # clear
        for widget in self.feed_frame.winfo_children():
            widget.destroy()
        # show latest 5, newest first
        for name, photo, caption in self.posts[-5:][::-1]:
            fr = tk.Frame(self.feed_frame, bg="white", bd=2, relief="groove", padx=10, pady=5)
            fr.pack(fill="x", pady=10, padx=10)

            tk.Label(fr, text=f"{name}", font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
            lbl = tk.Label(fr, image=photo, bg="white")
            lbl.image = photo
            lbl.pack(pady=5)
            tk.Label(fr, text=caption, font=("Arial", 12), bg="white",
                     wraplength=400, justify="left").pack(anchor="w")

            # Action buttons
            act = tk.Frame(fr, bg="white")
            act.pack(anchor="w", pady=5)
            tk.Button(act, text="❤️ Like", bg="white", bd=0,
                      command=lambda b=act: self.like_action(b.winfo_children()[0])).pack(side="left", padx=5)
            tk.Button(act, text="💬 Comment", bg="white", bd=0,
                      command=lambda: messagebox.showinfo("Comment", "Comment section coming soon")).pack(side="left", padx=5)
            tk.Button(act, text="📤 Share", bg="white", bd=0,
                      command=lambda: messagebox.showinfo("Share", "Post shared!")).pack(side="left", padx=5)

    def like_action(self, btn):
        if btn["text"] == "❤️ Like":
            btn.config(text="❤️ Liked", fg="#e1306c")
        else:
            btn.config(text="❤️ Like", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniSocialApp(root)
    root.mainloop()
