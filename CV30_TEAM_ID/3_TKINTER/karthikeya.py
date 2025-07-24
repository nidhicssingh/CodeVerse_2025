import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# --- Main Window Setup ---
root = tk.Tk()
root.title("Mini Social Media - Karthikeya")
root.geometry("500x650") # Slightly increased height for better spacing
root.configure(bg="#E8F0FE") # Very light blue background, slightly more vibrant

# List to store posts
posts = []

# --- Functions ---

def post_message():
    """Handles posting a new message to the feed."""
    name = name_entry.get().strip()
    message = post_text.get("1.0", tk.END).strip()

    if name and message:
        posts.append({"name": name, "message": message, "likes": 0})
        name_entry.delete(0, tk.END)
        post_text.delete("1.0", tk.END)
        display_posts() # Refresh the displayed posts
    else:
        # Using tkinter.messagebox for simplicity as custom Toplevel is more complex.
        messagebox.showwarning("Empty Fields", "Please enter both name and message.")

def like_post(index, like_btn_widget):
    """
    Increments the like count for a post and provides a brief visual animation.
    Args:
        index (int): The index of the post in the 'posts' list.
        like_btn_widget (tk.Button): The specific like button widget that was clicked.
    """
    if 0 <= index < len(posts):
        posts[index]['likes'] += 1

        # Animation: Briefly change button color
        original_bg = like_btn_widget.cget("bg")
        original_fg = like_btn_widget.cget("fg")
        like_btn_widget.config(bg="#FF4C4C", fg="white") # More intense red flash
        
        # After a short delay, revert color and then refresh posts
        root.after(150, lambda: like_btn_widget.config(bg=original_bg, fg=original_fg))
        root.after(300, display_posts) # Refresh posts after animation completes

def display_posts():
    """Clears and re-displays all posts in the posts_frame."""
    # Clear existing widgets in the posts_frame
    for widget in posts_frame.winfo_children():
        widget.destroy()
    
    # Display posts in reverse order (newest first)
    for idx, post in enumerate(reversed(posts)):
        # Calculate the original index in the 'posts' list for liking
        original_idx = len(posts) - 1 - idx

        post_frame = tk.Frame(posts_frame, bg="#F8FCFF", padx=15, pady=10, bd=1, relief="solid", highlightbackground="#A7D9F7", highlightthickness=1)
        post_frame.pack(fill="x", pady=8, padx=5) # Add some padding around each post frame

        # Name Label
        name_label = tk.Label(post_frame, text=f"{post['name']} says:", font=("Arial", 11, "bold"), bg="#F8FCFF", fg="#1A5276") # Darker blue
        name_label.pack(anchor="w", pady=(0, 2))

        # Message Label
        message_label = tk.Label(post_frame, text=post['message'], font=("Arial", 10), bg="#F8FCFF", fg="#333333", wraplength=400, justify="left")
        message_label.pack(anchor="w", pady=(0, 5))

        # Like Button
        like_btn = tk.Button(
            post_frame,
            text=f"❤ Like ({post['likes']})",
            font=("Arial", 9, "bold"),
            bg="#FFB6C1", # Lighter pink
            fg="#C70039", # Deeper red for heart
            activebackground="#FF4C4C", # Active state for button
            activeforeground="white",
            relief="raised",
            bd=1,
            cursor="hand2"
        )
        # Pass the button widget itself to the like_post function for animation
        like_btn.config(command=lambda btn=like_btn, i=original_idx: like_post(i, btn))
        like_btn.pack(anchor="e", pady=(5, 0))

# --- Widgets ---

# Name Input
tk.Label(root, text="Your Name:", font=("Arial", 12, "bold"), bg="#E8F0FE", fg="#1A5276").pack(pady=(15, 0)) # Darker blue
name_entry = tk.Entry(root, font=("Arial", 12), width=40, bd=2, relief="groove", bg="#FFFFFF", fg="#333333", insertbackground="#333333")
name_entry.pack(pady=5)

# Post Text Area
tk.Label(root, text="Write a Post:", font=("Arial", 12, "bold"), bg="#E8F0FE", fg="#1A5276").pack(pady=(10, 0)) # Darker blue
post_text = scrolledtext.ScrolledText(root, width=50, height=5, font=("Arial", 12), bd=2, relief="groove", bg="#FFFFFF", fg="#333333", insertbackground="#333333")
post_text.pack(pady=5)

# Post Button
post_button = tk.Button(
    root,
    text="Share Post",
    font=("Arial", 13, "bold"),
    bg="#34A853", # Google Green shade
    fg="white",
    activebackground="#2B8E44", # Darker green on active
    activeforeground="white",
    relief="raised",
    bd=3,
    cursor="hand2",
    command=post_message
)
post_button.pack(pady=15, ipadx=20, ipady=5) # Added internal padding

# Frame to hold posts
posts_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief="sunken", highlightbackground="#D3D3D3", highlightthickness=1)
posts_frame.pack(fill="both", expand=True, padx=15, pady=10) # Added external padding

# Initial display of posts (will be empty initially)
display_posts()

# Start the Tkinter event loop
root.mainloop()