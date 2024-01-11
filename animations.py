```python
import pygame
from pygame.locals import *

class Animation:
    def __init__(self, images, speed):
        self.images = images
        self.speed = speed
        self.index = 0
        self.time = 0

    def update(self, dt):
        self.time += dt
        if self.time >= self.speed:
            self.time = 0
            self.index = (self.index + 1) % len(self.images)

    def draw(self, screen, pos):
        image = self.images[self.index]
        rect = image.get_rect()
        rect.center = pos
        screen.blit(image, rect)

def load_images(*filenames):
    return [pygame.image.load(filename) for filename in filenames]

def bot_avatar_animation():
    images = load_images('bot_avatar1.png', 'bot_avatar2.png', 'bot_avatar3.png')
    animation = Animation(images, 0.1)
    return animation

def text_bubble_animation():
    images = load_images('text_bubble1.png', 'text_bubble2.png', 'text_bubble3.png')
    animation = Animation(images, 0.1)
    return animation

def voice_visualizer_animation():
    images = load_images('voice_visualizer1.png', 'voice_visualizer2.png', 'voice_visualizer3.png')
    animation = Animation(images, 0.1)
    return animation
```