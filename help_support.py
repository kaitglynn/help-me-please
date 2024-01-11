```python
import tkinter as tk
from tkinter import messagebox

def open_help_window():
    help_window = tk.Toplevel()
    help_window.title("Help & Support")
    help_window.geometry("400x300")

    help_label = tk.Label(help_window, text="Help & Support", font=("Arial", 20))
    help_label.pack(pady=10)

    help_text = """If you have any issues or questions, 
    please follow the steps:
    1. Check out the FAQ section.
    2. If you can't find your answer, please contact us at support@mistral7.com"""
    help_message = tk.Message(help_window, text=help_text, width=350)
    help_message.pack(pady=10)

    close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)

def open_faq_window():
    faq_window = tk.Toplevel()
    faq_window.title("FAQ")
    faq_window.geometry("400x300")

    faq_label = tk.Label(faq_window, text="Frequently Asked Questions", font=("Arial", 20))
    faq_label.pack(pady=10)

    faq_text = """1. How to change the bot's voice?
    Answer: Go to Settings -> Voice Settings.
    
    2. How to share files?
    Answer: Click on the attachment icon in the chat interface."""
    faq_message = tk.Message(faq_window, text=faq_text, width=350)
    faq_message.pack(pady=10)

    close_button = tk.Button(faq_window, text="Close", command=faq_window.destroy)
    close_button.pack(pady=10)

def show_error_message(error):
    messagebox.showerror("Error", error)

def show_info_message(info):
    messagebox.showinfo("Information", info)
```