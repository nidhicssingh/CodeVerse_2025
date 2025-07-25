import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

uploaded_image = None  # To store uploaded image path

# Function to upload image
def upload_image():
    global uploaded_image
    uploaded_image = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if uploaded_image:
        messagebox.showinfo("Image Uploaded", f"Selected: {uploaded_image}")

# Function to delete a post
def delete_post(frame):
    frame.destroy()

# Function to post content
def post_content():
    global uploaded_image
    content = text_area.get("1.0", tk.END).strip()
    if content or uploaded_image:
        # Create a frame for each post
        post_frame = tk.Frame(timeline_frame, bg="#2c2c2c", bd=1, relief="solid", padx=8, pady=8)
        post_frame.pack(fill=tk.X, pady=8)

        # Username
        username_label = tk.Label(post_frame, text="TECH_TITANS", font=("Arial", 11, "bold"), fg="#1e90ff", bg="#2c2c2c")
        username_label.pack(anchor="w")

        # Post text
        if content:
            post_label = tk.Label(post_frame, text=content, font=("Arial", 12), bg="#2c2c2c", fg="white", justify="left", wraplength=500)
            post_label.pack(anchor="w", pady=5)

        # Post image
        if uploaded_image:
            img = Image.open(uploaded_image)
            img.thumbnail((400, 300))  # Resize for display
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(post_frame, image=img_tk, bg="#2c2c2c")
            img_label.image = img_tk  # Keep a reference
            img_label.pack(anchor="w", pady=5)

        # Delete button
        delete_btn = tk.Button(post_frame, text="Delete", font=("Arial", 10, "bold"), bg="#ff4d4d", fg="white",
                               relief="flat", command=lambda: delete_post(post_frame))
        delete_btn.pack(anchor="e", pady=5)

        # Clear inputs after posting
        text_area.delete("1.0", tk.END)
        uploaded_image = None

        # Auto-scroll to bottom
        canvas.yview_moveto(1.0)
    else:
        messagebox.showwarning("Empty Post", "Please write something or upload an image before posting.")

# Main window
root = tk.Tk()
root.title("CHIT-CHAT")
root.geometry("650x650")
root.configure(bg="#1a1a1a")  # Dark background

# Header
header = tk.Label(root, text="CHIT-CHAT", font=("Helvetica", 28, "bold"), bg="#0d0d0d", fg="#1e90ff", pady=15)
header.pack(fill=tk.X)

# Frame for post creation
frame = tk.Frame(root, bg="#2c2c2c", bd=2, relief="groove", padx=10, pady=10)
frame.pack(pady=10, padx=30, fill=tk.X)

# Create post label
create_label = tk.Label(frame, text="Create Post", font=("Arial", 13, "bold"), bg="#2c2c2c", fg="white")
create_label.pack(anchor="w")

# Text area
text_area = tk.Text(frame, height=5, font=("Arial", 12), wrap="word", bd=2, relief="solid", bg="#1a1a1a", fg="white", insertbackground="white")
text_area.pack(fill=tk.X, pady=10)

# Button frame
button_frame = tk.Frame(frame, bg="#2c2c2c")
button_frame.pack(fill=tk.X, pady=5)

# Upload image button
upload_btn = tk.Button(button_frame, text="Upload Image", font=("Arial", 11, "bold"), bg="#1e90ff", fg="white",
                       relief="flat", command=upload_image)
upload_btn.pack(side=tk.LEFT, padx=5)

# Post button
post_btn = tk.Button(button_frame, text="Post", font=("Arial", 11, "bold"), bg="#28a745", fg="white",
                     relief="flat", command=post_content)
post_btn.pack(side=tk.RIGHT, padx=5)

# --- Timeline Section ---
timeline_label = tk.Label(root, text="Timeline", font=("Arial", 15, "bold"), bg="#1a1a1a", fg="white")
timeline_label.pack(anchor="w", padx=30, pady=(10, 0))

# Canvas for scrollable timeline
canvas = tk.Canvas(root, bg="#1a1a1a", highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(30,0), pady=5)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5)

canvas.configure(yscrollcommand=scrollbar.set)

# Frame inside canvas
timeline_frame = tk.Frame(canvas, bg="#1a1a1a")
canvas.create_window((0,0), window=timeline_frame, anchor="nw")

# Update scroll region dynamically
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

timeline_frame.bind("<Configure>", on_frame_configure)

root.mainloop()


