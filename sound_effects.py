```python
import pygame

class SoundEffects:
    def __init__(self):
        pygame.mixer.init()
        self.send_message_sound = pygame.mixer.Sound('sounds/send_message.wav')
        self.receive_message_sound = pygame.mixer.Sound('sounds/receive_message.wav')
        self.voice_chat_start_sound = pygame.mixer.Sound('sounds/voice_chat_start.wav')
        self.voice_chat_end_sound = pygame.mixer.Sound('sounds/voice_chat_end.wav')
        self.notification_sound = pygame.mixer.Sound('sounds/notification.wav')

    def play_send_message_sound(self):
        pygame.mixer.Sound.play(self.send_message_sound)

    def play_receive_message_sound(self):
        pygame.mixer.Sound.play(self.receive_message_sound)

    def play_voice_chat_start_sound(self):
        pygame.mixer.Sound.play(self.voice_chat_start_sound)

    def play_voice_chat_end_sound(self):
        pygame.mixer.Sound.play(self.voice_chat_end_sound)

    def play_notification_sound(self):
        pygame.mixer.Sound.play(self.notification_sound)
```