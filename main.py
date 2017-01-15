import pygame, random, os, time
pygame.init()
pygame.display.set_caption('Pigeon Puncher')
__author__ = 'Tim Dickeson II'
clock = pygame.time.Clock()

White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (30, 30, 30)

#-----Background-----#
bg_path = os.path.join('images', 'bg.jpg')
bg = pygame.image.load(bg_path)
bg_rect = bg.get_rect()

size = screen_width, screen_height = 1024, 768 #must be 1024,768
floor = int(screen_height * 0.78)
ceiling = int(screen_height * 0.14)
screen = pygame.display.set_mode(size)
x = 0
x1 = screen_width
y = 0
scroll_speed = 10
times_ran = 0

def UpdateBackground():
        global x, x1, y, scroll_speed
        screen.blit(bg, bg_rect)
        x -= scroll_speed
        x1 -= scroll_speed
        screen.blit(bg,(x,y))
        screen.blit(bg,(x1,y))
        if x <= -screen_width:
                x = screen_width-scroll_speed
        if x1 <= -screen_width:
                x1 = screen_width-scroll_speed

#-----Anderson Walking Animations-----#
walk1_path = os.path.join('images', 'walk1.png')
walk1 = pygame.image.load(walk1_path)

walk2_path = os.path.join('images', 'walk2.png')
walk2 = pygame.image.load(walk2_path)

#-----Anderson Jetpack Animations-----#
jetpack_off_path = os.path.join('images', 'jetpack_off.png')
jetpack_off = pygame.image.load(jetpack_off_path)

jetpack_on_path = os.path.join('images', 'jetpack_on.png')
jetpack_on = pygame.image.load(jetpack_on_path)

#-----Anderson Punch Animation-----#
punch_pic_path = os.path.join('images', 'punch.png')
punch_pic = pygame.image.load(punch_pic_path)

#-----Pigeon Flying Animations-----#
pigeon1_path = os.path.join('images', 'pigeon1.gif')
pigeon1 = pygame.image.load(pigeon1_path)
pigeon1_rect = pigeon1.get_rect()

pigeon2_path = os.path.join('images', 'pigeon2.gif')
pigeon2 = pygame.image.load(pigeon2_path)
pigeon2_rect = pigeon2.get_rect()

#-----Game Icon-----#
pygame.display.set_icon(punch_pic)

#classes and objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [walk1, walk2, jetpack_on, jetpack_off]
        self.index = 0
        self.firstIndex = 0
        self.lastIndex = 1
        self.pos_x = screen_width * 0.1
        self.pos_y = floor
        self.rect = pygame.Rect(0, 0, 45, 50)
        self.change_y = 30

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

    def punch(self):
        return punch_pic

    def animate(self, Surface):
        screen.blit(Surface, self.rect)

    def detectCollision(self):
        if player.rect.colliderect(pigeon.rect):
            animation = self.punch()
            pigeon.spawn(pigeon.pos_x, pigeon.pos_y)
            return True
        else:
            return False

    def update(self):
        self.pos_y += self.change_y
        if self.pos_y > floor-self.change_y:
            self.pos_y = floor
        elif self.pos_y < ceiling-self.change_y:
            self.pos_y = ceiling
        
        #-START ANIMATIONS-#
        if self.detectCollision() == True:
            animation = self.punch()
        elif self.pos_y >= floor:
            animation = self.walk()
        else:
            if self.change_y < 0:
                animation = self.jetpackOn()
            elif self.change_y > 0:
                animation = self.jetpackOff()
                
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 45, 50)
        self.detectCollision()
        self.animate(animation)
        #--END ANIMATIONS--#
player = Player()

class Pigeon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pigeon1, pigeon2]
        self.index = 0
        self.firstIndex = 0
        self.lastIndex = 1
        self.pos_x = screen_width
        self.pos_y = floor
        self.rect = pygame.Rect(0, 0, 48, 55)        
        self.change_x = -35
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
            gameRunning = False
            gameOver()
            self.count_punched -= 1
        self.pos_x += self.change_x
        
        #-START ANIMATIONS-#
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 48, 55)
        self.animate(self.fly())
        #--END ANIMATIONS--#
pigeon = Pigeon()

def text_objects(text, font):
    textSurface = font.render(text, True, White)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font('game_font.ttf',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def display_score(text):
    largeText = pygame.font.Font('game_font.ttf', 60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.left = 10
    screen.blit(TextSurf, TextRect)

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverTasks()
        UpdateBackground()
        Player.update(player)
        largeText = pygame.font.Font('game_font.ttf', 60)
        TextSurf, TextRect = text_objects('Pigeon Puncher', largeText)
        TextRect.center = ((screen_width/2),(screen_height/2))
        screen.blit(TextSurf, TextRect)
        button('Start',
               TextRect.center[0]-50, TextRect.center[1]+50,
               80, 50,
               Black, Grey,
               gameLoop)
        pygame.display.flip()
        clock.tick(120)

def gameLoop():
    global times_ran
    gameRunning = True
    while gameRunning:
        UpdateBackground()
        Pigeon.update(pigeon)
        Player.update(player)
        if times_ran > 0:
            display_score('Score: ' + str(pigeon.count_punched))
        else:
            pigeon.count_punched = 0
            display_score('Score: 0')
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                player.change_y *= -1
            if event.type == pygame.KEYUP:
                player.change_y *= -1
            if event.type == pygame.QUIT:
                gameOverTasks()
        times_ran += 1

def restartGameLoop():
    global times_ran
    times_ran = 0
    Pigeon.count_punched = 0
    Pigeon.spawn(pigeon, screen_width, floor)
    gameLoop()

def gameOver():
    gameRunning = False
    while not gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverTasks()
        UpdateBackground()
        Player.update(player)
        largeText = pygame.font.Font('game_font.ttf', 40)
        TextSurf, TextRect = text_objects('Game Over. You scored: ' + str(pigeon.count_punched), largeText)
        TextRect.center = ((screen_width/2),(screen_height/2))
        screen.blit(TextSurf, TextRect)
        button('Try Again',
               TextRect.center[0]-175, TextRect.center[1]+50,
               100, 50,
               Black, Grey,
               restartGameLoop)
        button('Quit',
               TextRect.center[0]+75, TextRect.center[1]+50,
               100, 50,
               Black, Grey,
               gameOverTasks)
        pygame.display.flip()
        clock.tick(120)

def gameOverTasks():
    pygame.quit()
    quit()

def main():
    gameIntro()
    gameLoop()
    gameOver()

if __name__ == '__main__':
    main()


    
