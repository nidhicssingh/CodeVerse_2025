import tkinter as tk
from tkinter import simpledialog

def comment_window(root, post):
    comment = simpledialog.askstring("Comment", "Write your comment:")
    if comment:
        post["comments"].append({"user": "Nidhi", "text": comment})
