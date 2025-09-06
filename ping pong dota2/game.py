from pygame import *

window = display.set_mode((700,500))                                                      #окно
display.set_caption('dota2pingpoing')
background = transform.scale(image.load('1032683.jpg'),(700,500))                                                 


class GameSprite(sprite.Sprite):                                                                             
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):                                                #управление шариком(вторым тиником)
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x < 700 -80:
            self.rect.x +=self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < 500 -80:
            self.rect.y +=self.speed

class laye(GameSprite):                                                     #управление шариком(первым тиником)
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys[K_d] and self.rect.x < 700 -80:
            self.rect.x +=self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < 500 -80:
            self.rect.y +=self.speed

class visp(GameSprite):                                     #управление шариком(отключить потом)
    def update(self):
        keys = key.get_pressed()
        if keys[K_j] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys[K_l] and self.rect.x < 700 -80:
            self.rect.x +=self.speed
        if keys[K_i] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_k] and self.rect.y < 500 -80:
            self.rect.y +=self.speed

speed_x = 3
speed_y = 3


player = Player('tiny.png',10,10,10)       #точка появления (первые 2 координаты, скорость вторые две координаты)
player1 = laye('init.png',600,400,10)
player2 = visp('io.png',-0,0,5)


game = True

clock = time.Clock()
FPS = 60
while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    if player2.rect.x >700:
        speed_x *= -1

    if player2.rect.y >500:
        speed_y *= -1

    if player2.rect.x <0:
        speed_x *= -1

    if player2.rect.y <0:
        speed_y *= -1

    player2.rect.x += speed_x
    player2.rect.y += speed_y

    player.reset()
    player1.reset()
    player2.reset()

    player.update()
    player2.update()

    

    player1.update()



    
    
    

    

    display.update()
    clock.tick(FPS)




