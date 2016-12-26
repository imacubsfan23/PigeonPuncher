import pygame, random, sys, os
pygame.init()
pygame.display.set_caption('Pigeon Puncher')
__author__ = "Tim Dickeson II"

#Background size must be 1024x768
size = screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode(size)

x,x1,y,scroll_speed = 0,screen_width,0,10

#-----Background-----#
bg_path = os.path.join("images", "temp_bg.jpg")
temp_bg = pygame.image.load(bg_path)
temp_bg_rect = temp_bg.get_rect()

#-----Anderson Walking Animations-----#
walk1_path = os.path.join("images", "temp_walk1.png")
temp_walk1 = pygame.image.load(walk1_path)
temp_walk1_rect = temp_walk1.get_rect()

walk2_path = os.path.join("images", "temp_walk2.png")
temp_walk2 = pygame.image.load(walk2_path)
temp_walk2_rect = temp_walk2.get_rect()

#-----Anderson Jetpack Animations-----#
jetpack_off_path = os.path.join("images", "temp_jetpack_off.png")
temp_jetpack_off = pygame.image.load(jetpack_off_path)
temp_jetpack_off_rect = temp_jetpack_off.get_rect()

jetpack_on_path = os.path.join("images", "temp_jetpack_on.png")
temp_jetpack_on = pygame.image.load(jetpack_on_path)
temp_jetpack_on_rect = temp_jetpack_on.get_rect()

#-----Pigeon Flying Animations-----#
pigeon1_path = os.path.join("images", "temp_pigeon1.png")
temp_pigeon1 = pygame.image.load(pigeon1_path)
temp_pigeon1_rect = temp_pigeon1.get_rect()

pigeon2_path = os.path.join("images", "temp_pigeon2.png")
temp_pigeon2 = pygame.image.load(pigeon2_path)
temp_pigeon2_rect = temp_pigeon2.get_rect()

'''#classes and objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        #blit Anderson where gravity and jump say he is

class Pigeon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        size = (20,20)
        #self.rect = self.get_rect()
        self.pos_x = screen_width
        self.change_x = -5

    def spawn(self, pos_y):
        self.pos_y = random.randrange(0,screen_height-60)

    def update(self):
        self.pos_x += self.change_x'''

#game loop
gameRunning = True
while gameRunning:
        #blit background
        screen.blit(temp_bg, temp_bg_rect)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameRunning = False
                        pygame.quit()
                        sys.exit()
                        
        #scroll handling
        x -= scroll_speed
        x1 -= scroll_speed
        screen.blit(temp_bg,(x,y))
        screen.blit(temp_bg,(x1,y))
        if x < -screen_width:
                x = screen_width
        if x1 < -screen_width:
                x1 = screen_width
        #end scroll handling
        
        pygame.display.flip()
