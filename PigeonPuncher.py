import pygame, random
pygame.init()
pygame.display.set_caption('PigeonPuncher')

#initializing and variables
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))

#classes and objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        #blit Anderson where gravity and jump say he is

class Pigeon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        size = pygame.sprite.get_size
        self.rect = size
        self.pos_x = 
        self.pos_y = 
        self.change_x = 0

    def spawn(self):
        #random y value for spawn

    def update(self:
        
#game loop
def main():
    pygame.display.flip()
    
#play until quit
if __name__ == "__main__":
    main()
