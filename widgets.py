```python
import tkinter as tk
from tkinter import ttk

class MainScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.user_section = tk.Frame(self)
        self.bot_section = tk.Frame(self)
        self.user_section.pack(side="left", fill="both", expand=True)
        self.bot_section.pack(side="right", fill="both", expand=True)

class NavigationBar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.home_button = ttk.Button(self, text="Home")
        self.voice_chat_button = ttk.Button(self, text="Voice Chat")
        self.profile_button = ttk.Button(self, text="Profile")
        self.settings_button = ttk.Button(self, text="Settings")
        self.home_button.pack(side="left")
        self.voice_chat_button.pack(side="left")
        self.profile_button.pack(side="left")
        self.settings_button.pack(side="left")

class ChatInterface(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.text_chat = TextChat(self)
        self.voice_chat = VoiceChat(self)
        self.text_chat.pack(side="top", fill="both", expand=True)
        self.voice_chat.pack(side="bottom", fill="both", expand=True)

class TextChat(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.input_field = ttk.Entry(self)
        self.send_button = ttk.Button(self, text="Send")
        self.input_field.pack(side="left", fill="x", expand=True)
        self.send_button.pack(side="right")

class VoiceChat(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.microphone_button = ttk.Button(self, text="🎙️")
        self.microphone_button.pack(side="left")

class UserProfile(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.name_label = ttk.Label(self, text="Name")
        self.avatar_label = ttk.Label(self, text="Avatar")
        self.bio_label = ttk.Label(self, text="Bio")
        self.name_label.pack(side="top")
        self.avatar_label.pack(side="top")
        self.bio_label.pack(side="top")

class BotProfile(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.name_label = ttk.Label(self, text="Name")
        self.avatar_label = ttk.Label(self, text="Avatar")
        self.bio_label = ttk.Label(self, text="Bio")
        self.name_label.pack(side="top")
        self.avatar_label.pack(side="top")
        self.bio_label.pack(side="top")
```
This code creates the basic structure of the GUI using tkinter. It includes the main screen, navigation bar, chat interface, text chat, voice chat, user profile, and bot profile. Each of these is a separate class that inherits from tkinter's Frame class. The widgets are packed into their respective frames using the pack method.