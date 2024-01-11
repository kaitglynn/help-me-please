```python
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.create_chat_interface()

    def create_chat_interface(self):
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        self.text_display = scrolledtext.ScrolledText(self.chat_frame)
        self.text_display.pack(fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(self.chat_frame)
        self.input_frame.pack(fill=tk.X)

        self.text_input = tk.Entry(self.input_frame)
        self.text_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_text_message)
        self.send_button.pack(side=tk.RIGHT)

        self.emoji_button = tk.Button(self.input_frame, text="Emoji", command=self.add_emoji)
        self.emoji_button.pack(side=tk.RIGHT)

        self.attachment_button = tk.Button(self.input_frame, text="Attach", command=self.share_file)
        self.attachment_button.pack(side=tk.RIGHT)

    def send_text_message(self):
        message = self.text_input.get()
        if message:
            self.text_display.insert(tk.END, f"You: {message}\n")
            self.text_input.delete(0, tk.END)

    def add_emoji(self):
        # Function to add emoji to the chat
        pass

    def share_file(self):
        # Function to share files
        pass

if __name__ == "__main__":
    root = tk.Tk()
    ChatInterface(root)
    root.mainloop()
```