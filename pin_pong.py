from pygame import *
from random import randint

class players(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, X, Y):
        super().__init__()
        self.X = X
        self.Y = Y
        self.image = transform.scale(image.load(player_image), (self.X, self.Y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def UP():
        self.rect.y += self.speed 
    def DOWN():
        self.rect.y -= self.speed

class orbs(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, X, Y):
        super().__init__()
        self.X = X
        self.Y = Y
        self.image = transform.scale(image.load(player_image), (self.X, self.Y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

Raketka1 = 'ракетка номер 1.png'
Raketka2 = 'ракетка номер 2.png'
orb_png = 'Кубомяч.png'


belety_count = 0
bellets = sprite.Group()

win_y = 700
win_x = 500
window = display.set_mode((win_y, win_x))
finish = False
font.init()
font2 = font.Font(None, 70)

font.init()
font2 = font.Font(None, 70) 


game = True
clock = time.Clock()
FPS = 60

player1 = players(Raketka1, 30, win_x - 250,2,15,135)
player2 = players(Raketka2, 670, win_x - 250,2,15,135)
orb = orbs(orb_png, win_y/2, win_x/2,2,50,50)

background = transform.scale(image.load('Фон.png'), (win_y, win_x))

Score1 = 0
Score2 = 0

DEAD_TIMER = 0

orb_y = 2
orb_event1 = randint(1,2)
orb_event2 = randint(1,2)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))

    DEAD_TIMER += 1
    if DEAD_TIMER == 500:
        DEAD_TIMER = 0
        orb.speed += 0.1
        orb_y += 0.1

    player1.reset()
    player2.reset()
    orb.reset()


    if orb.rect.y < 75:
        orb_event1 = 1
    if orb_event1 == 1:
        orb.rect.y += orb_y

    if orb.rect.y > 450:
        orb_event1 = 2
    if orb_event1 == 2:
        orb.rect.y -= orb_y
    
    print(orb.speed)
    if player1.rect.x-orb.rect.x < 0 and player1.rect.x-orb.rect.x > -14 and player1.rect.y-orb.rect.y < 40 and player1.rect.y-orb.rect.y > -120:
        orb_event2 = 1   
    elif player1.rect.x-orb.rect.x > 40:
        orb_event2 = 1  
        Score2 += 1
    if orb_event2 == 1:
        orb.rect.x += orb.speed

    if player2.rect.x-orb.rect.x < 42 and player2.rect.x-orb.rect.x > 30 and player2.rect.y-orb.rect.y < 40 and player2.rect.y-orb.rect.y > -120:
        orb_event2 = 2
    elif player2.rect.x-orb.rect.x < -10:
        orb_event2 = 2  
        Score1 += 1    
    if orb_event2 == 2:
        orb.rect.x -= orb.speed

    keys_presed = key.get_pressed()
    if keys_presed[K_w] and player1.rect.y > 75:
        player1.rect.y -= player1.speed
    if keys_presed[K_s] and player1.rect.y < 350:
        player1.rect.y += player1.speed
    if keys_presed[K_UP] and player2.rect.y > 75:
        player2.rect.y -= player2.speed
    if keys_presed[K_DOWN] and player2.rect.y < 350:
        player2.rect.y += player2.speed

    Final_text = font2.render(str(Score1), 1, (0, 0, 0))
    window.blit(Final_text, (250, 5))
    Final_text = font2.render(str(Score2), 1, (0, 0, 0))
    window.blit(Final_text, (455, 5))

    display.update()
    clock.tick(FPS)