```python
import speech_recognition as sr

class VoiceControlPlugin:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_command(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                return command
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None

class BrowserExtensionPlugin:
    def __init__(self, browser):
        self.browser = browser

    def open_new_tab(self, url):
        self.browser.open_new_tab(url)

    def close_tab(self, tab_id):
        self.browser.close_tab(tab_id)

    def navigate_to(self, url):
        self.browser.get(url)

class CustomPluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin

    def get_plugin(self, name):
        return self.plugins.get(name, None)

# Initialize custom plugin manager
custom_plugin_manager = CustomPluginManager()

# Register voice control plugin
voice_control_plugin = VoiceControlPlugin()
custom_plugin_manager.register_plugin('voice_control', voice_control_plugin)

# Register browser extension plugin
# Assume we have a browser instance
browser_extension_plugin = BrowserExtensionPlugin(browser)
custom_plugin_manager.register_plugin('browser_extension', browser_extension_plugin)
```