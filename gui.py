```python
import tkinter as tk
from tkinter import ttk
from chat_interface import ChatInterface
from voice_chat import VoiceChat
from user_profile import UserProfile
from bot_profile import BotProfile
from file_sharing import FileSharing
from chat_history import ChatHistory
from search import Search
from notifications import Notifications
from themes import Themes
from help_support import HelpSupport

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mistral 7")
        self.root.geometry("800x600")

        self.chat_interface = ChatInterface(self.root)
        self.voice_chat = VoiceChat(self.root)
        self.user_profile = UserProfile(self.root)
        self.bot_profile = BotProfile(self.root)
        self.file_sharing = FileSharing(self.root)
        self.chat_history = ChatHistory(self.root)
        self.search = Search(self.root)
        self.notifications = Notifications(self.root)
        self.themes = Themes(self.root)
        self.help_support = HelpSupport(self.root)

        self.create_widgets()

    def create_widgets(self):
        self.create_main_screen()
        self.create_navigation_bar()

    def create_main_screen(self):
        self.main_screen = ttk.Frame(self.root)
        self.main_screen.pack(fill='both', expand=True)

        self.user_section = ttk.Frame(self.main_screen)
        self.user_section.pack(side='left', fill='both', expand=True)

        self.bot_section = ttk.Frame(self.main_screen)
        self.bot_section.pack(side='right', fill='both', expand=True)

    def create_navigation_bar(self):
        self.navigation_bar = ttk.Frame(self.root)
        self.navigation_bar.pack(side='bottom', fill='x')

        self.home_button = ttk.Button(self.navigation_bar, text='Home', command=self.chat_interface.display)
        self.home_button.pack(side='left')

        self.voice_chat_button = ttk.Button(self.navigation_bar, text='Voice Chat', command=self.voice_chat.display)
        self.voice_chat_button.pack(side='left')

        self.profile_button = ttk.Button(self.navigation_bar, text='Profile', command=self.user_profile.display)
        self.profile_button.pack(side='left')

        self.settings_button = ttk.Button(self.navigation_bar, text='Settings', command=self.themes.display)
        self.settings_button.pack(side='left')

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
```