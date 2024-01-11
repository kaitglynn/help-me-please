```python
import tkinter as tk

# Define the themes
THEMES = {
    "light": {
        "main_bg": "#ffffff",
        "secondary_bg": "#f0f0f0",
        "main_fg": "#000000",
        "secondary_fg": "#555555",
        "accent": "#0077ff",
        "error": "#ff0000",
    },
    "dark": {
        "main_bg": "#333333",
        "secondary_bg": "#222222",
        "main_fg": "#ffffff",
        "secondary_fg": "#bbbbbb",
        "accent": "#0077ff",
        "error": "#ff5555",
    },
}

currentTheme = "light"

def apply_theme(theme_name):
    global currentTheme
    if theme_name not in THEMES:
        print(f"Error: {theme_name} theme does not exist.")
        return

    theme = THEMES[theme_name]
    currentTheme = theme_name

    # Apply the theme to the main screen
    mainScreen.config(bg=theme["main_bg"])
    navigationBar.config(bg=theme["secondary_bg"])
    textInputField.config(bg=theme["main_bg"], fg=theme["main_fg"])
    voiceInputButton.config(bg=theme["accent"], fg=theme["main_fg"])
    userProfile.config(bg=theme["secondary_bg"], fg=theme["main_fg"])
    botProfile.config(bg=theme["secondary_bg"], fg=theme["main_fg"])
    fileAttachment.config(bg=theme["accent"], fg=theme["main_fg"])
    chatHistoryTab.config(bg=theme["secondary_bg"], fg=theme["main_fg"])
    searchBar.config(bg=theme["main_bg"], fg=theme["main_fg"])

def changeTheme(new_theme):
    apply_theme(new_theme)
```