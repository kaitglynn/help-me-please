```python
import json

class BotProfileSchema:
    def __init__(self, name, avatar, bio):
        self.name = name
        self.avatar = avatar
        self.bio = bio

class BotProfile:
    def __init__(self):
        self.botProfile = BotProfileSchema("Mistral 7", "default_avatar.png", "I'm your friendly AI assistant!")

    def get_profile(self):
        return self.botProfile

    def update_profile(self, name=None, avatar=None, bio=None):
        if name:
            self.botProfile.name = name
        if avatar:
            self.botProfile.avatar = avatar
        if bio:
            self.botProfile.bio = bio

    def save_profile(self):
        with open('bot_profile.json', 'w') as json_file:
            json.dump(self.botProfile.__dict__, json_file)

    def load_profile(self):
        try:
            with open('bot_profile.json', 'r') as json_file:
                data = json.load(json_file)
                self.botProfile = BotProfileSchema(**data)
        except FileNotFoundError:
            self.save_profile()

botProfile = BotProfile()
botProfile.load_profile()
```