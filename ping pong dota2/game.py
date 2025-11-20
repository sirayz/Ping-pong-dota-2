from pygame import *

init()
font.init()

window = display.set_mode((700,500))                                                      #окно
display.set_caption('dota2pingpoing')
background = transform.scale(image.load('1032683.jpg'),(700,500))                                                 

RED = (255, 0, 0)
WHITE = (255, 255, 255)

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

class Player(GameSprite):                                                #управление вторым тиником
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

class Lay(GameSprite):                                                     #управление первым тиником
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

class Visp(GameSprite):
    pass

speed_x = 3
speed_y = 3


player = Player('tiny.png',10,10,10)       #точка появления (первые 2 координаты, 3 скорость )
player1 = Lay('init.png',600,400,10)
player2 = Visp('io.png',300,250,5)

game = True
game_over = False

clock = time.Clock()
FPS = 60

game_over_font = font.Font(None, 70)

while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_l and game_over:
                game_over = False
                player2.rect.x = 300
                player2.rect.y = 250
                speed_x = 3
                speed_y = 3
                player.rect.x = 10
                player.rect.y = 10
                player1.rect.x = 600
                player1.rect.y = 400

    if not game_over:

        player2.rect.x += speed_x
        player2.rect.y += speed_y

        if player2.rect.x < 0 or player2.rect.x + player2.rect.width > 700 or \
           player2.rect.y < 0 or player2.rect.y + player2.rect.height > 500:
            game_over = True


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

    if game_over:
        text_over = game_over_font.render("proipali", True, RED)

        text_game_over_rect = text_over.get_rect(center=(700 // 2, 500 // 2 - 30))


        window.blit(text_over, text_game_over_rect)


    

    player1.update()



    
    
    

    

    display.update()
    clock.tick(FPS)




