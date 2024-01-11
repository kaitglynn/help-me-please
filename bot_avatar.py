```python
import pygame
from pygame.locals import *

class BotAvatar:
    def __init__(self):
        self.avatar = pygame.image.load('bot_avatar.png')
        self.expression = 'neutral'

    def change_expression(self, new_expression):
        self.expression = new_expression
        self.avatar = pygame.image.load(f'bot_avatar_{new_expression}.png')

    def draw(self, surface):
        surface.blit(self.avatar, (0, 0))

    def update(self, new_expression):
        self.change_expression(new_expression)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    bot_avatar = BotAvatar()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill((255, 255, 255))
        bot_avatar.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
```