import pygame, random, sys, os
pygame.init()
pygame.display.set_caption('Pigeon Puncher')
__author__ = "Tim Dickeson II"
clock = pygame.time.Clock()

#-----Background-----#
bg_path = os.path.join("images", "bg.jpg")
bg = pygame.image.load(bg_path)
bg_rect = bg.get_rect()

size = screen_width, screen_height = 1024, 768 #must be 1024,768
floor = int(screen_height * 0.76)
ceiling = int(screen_height * 0.14)
screen = pygame.display.set_mode(size)
x = 0
x1 = screen_width
y = 0
scroll_speed = 10

def UpdateBackground():
        global x, x1, y, scroll_speed
        screen.blit(bg, bg_rect)
        x -= scroll_speed
        x1 -= scroll_speed
        screen.blit(bg,(x,y))
        screen.blit(bg,(x1,y))
        if x <= -screen_width:
                x = screen_width-scroll_speed #fixes background scrolling issue
        if x1 <= -screen_width:
                x1 = screen_width-scroll_speed

#-----Anderson Walking Animations-----#
'''ATTENTION!!! WALK1 AND WALK2 MUST BE SAME SIZE FOR THIS TO WORK'''
walk1_path = os.path.join("images", "walk1.png")
walk1 = pygame.image.load(walk1_path)

walk2_path = os.path.join("images", "walk2.png")
walk2 = pygame.image.load(walk2_path)

#-----Anderson Jetpack Animations-----#
jetpack_off_path = os.path.join("images", "jetpack_off.png")
jetpack_off = pygame.image.load(jetpack_off_path)

jetpack_on_path = os.path.join("images", "jetpack_on.png")
jetpack_on = pygame.image.load(jetpack_on_path)

#-----Pigeon Flying Animations-----#
pigeon1_path = os.path.join("images", "pigeon1.gif")
pigeon1 = pygame.image.load(pigeon1_path)
pigeon1_rect = pigeon1.get_rect()

pigeon2_path = os.path.join("images", "pigeon2.gif")
pigeon2 = pygame.image.load(pigeon2_path)
pigeon2_rect = pigeon2.get_rect()

#classes and objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [walk1, walk2, jetpack_on, jetpack_off]
        self.index = 0
        self.firstIndex = 0
        self.lastIndex = 1
        self.rect = pygame.Rect(0, 0, 48, 55)
        self.pos_x = screen_width * 0.1
        self.pos_y = floor
        self.change_y = 20
        self.alter_speed = 1

    def walk(self):
        temp_time = pygame.time.get_ticks()
        counter = 0
        switchTimer = 4
        if(temp_time%switchTimer==0):
            temp_time -= switchTimer
            counter+=1

        if(counter%2==0):
            return walk1
        else:
            return walk2

    def jetpackOn(self):
        return jetpack_on

    def jetpackOff(self):
        return jetpack_off

    def animate(self, Surface):
        screen.blit(Surface, self.rect)

    def update(self):
        self.pos_y += self.change_y
        if self.pos_y > floor-self.change_y:
            self.pos_y = floor
        elif self.pos_y < ceiling-self.change_y:
            self.pos_y = ceiling
        
        #-START ANIMATIONS-#
        if self.pos_y >= floor:
            animation = self.walk()
        else:
            if self.change_y < 0:
                animation = self.jetpackOn()
            elif self.change_y > 0:
                animation = self.jetpackOff()
                
        self.rect = (self.pos_x,self.pos_y)
        self.animate(animation)
        #--END ANIMATIONS--#

class Pigeon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pigeon1, pigeon2]
        self.index = 0
        self.firstIndex = 0
        self.lastIndex = 1
        self.rect = pygame.Rect(0, 0, 64, 64)
        self.pos_x = screen_width
        self.pos_y = ceiling
        self.change_x = -30
        self.spawn_pixels = screen_width
        self.count_punched = 0

    def fly(self):
        temp_time = pygame.time.get_ticks()
        counter = 0
        switchTimer = 4
        if(temp_time%switchTimer==0):
            temp_time -= switchTimer
            counter+=1

        if(counter%2==0):
            return pigeon1
        else:
            return pigeon2

    def animate(self, Surface):
        screen.blit(Surface, self.rect)

    def spawn(self, pos_x, pos_y):
        self.pos_x = screen_width
        self.pos_y = random.randrange(ceiling,floor)
        self.count_punched += 1

    def update(self):
        if(self.pos_x<=screen_width-self.spawn_pixels):
            self.spawn(self.pos_x, self.pos_y)
        self.pos_x += self.change_x

        #-START ANIMATIONS-#
        self.rect = (self.pos_x, self.pos_y)
        self.animate(self.fly())
        #--END ANIMATIONS--#

player = Player()
pigeon = Pigeon()
#-----Game Loop-----#
gameRunning = True
while gameRunning:
    UpdateBackground()
    Pigeon.update(pigeon)
    Player.update(player)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            player.change_y *= -1
        if event.type == pygame.KEYUP:
            player.change_y *= -1
        if event.type == pygame.QUIT:
            gameRunning = False
            pygame.quit()
            sys.exit()
