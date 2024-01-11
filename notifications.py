```python
import tkinter as tk
from tkinter import messagebox

def new_message_notification(message):
    messagebox.showinfo("New Message", message)

def new_voice_chat_notification():
    messagebox.showinfo("Voice Chat", "You have a new voice chat.")

def file_shared_notification(filename):
    messagebox.showinfo("File Shared", f"{filename} has been shared.")

def show_notification(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()
```