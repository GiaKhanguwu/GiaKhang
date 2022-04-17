import pygame
from paddle import Paddle
from obstacle import Obstacle
import random
from pygame import mixer

mixer.init()
mixer.music.load("C:Users/klabl/Downloads/PG_Family_Friendly_Music.mp3")
mixer.music.set_volume(1)

bg_img = pygame.image.load('C:Users/klabl/Downloads/download.jpg')
Speed = 4
X = int(random.random() * random.random() * 400)
Y = int(random.random() * random.random() * 400)
pygame.init()
print(X, Y)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ponk")
obstacle = Obstacle(RED, 10, 10)
obstacle.rect.x = X
obstacle.rect.y = Y
paddleA = Paddle(WHITE, 20, 20)
paddleA.rect.x = 0
paddleA.rect.y = 0
paddleB = Paddle(WHITE, 20, 20)
paddleB.rect.x = 0
paddleB.rect.y = 0
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(obstacle)
carryOn = True
clock = pygame.time.Clock()
scoreA = 0
scoreB = 0
mixer.music.play()
mixer.music.pause()

# -------- Main Program Loop -----------
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(Speed)
    if keys[pygame.K_s]:
        paddleA.moveDown(Speed)
    if keys[pygame.K_UP]:
        paddleB.moveUp(Speed)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(Speed)
    if keys[pygame.K_a]:
        if obstacle.rect.x > 690:
            obstacle.rect.x = 690
        if obstacle.rect.x > 10:
            obstacle.rect.x = 10
        paddleA.moveBackward(Speed)
    if keys[pygame.K_d]:
        if obstacle.rect.x > 690:
            obstacle.rect.x = 690
        if obstacle.rect.x > 10:
            obstacle.rect.x = 10
        paddleA.moveForward(Speed)
    if keys[pygame.K_LEFT]:
        if obstacle.rect.x > 10:
            obstacle.rect.x = 10
        paddleB.moveBackward(Speed)
    if keys[pygame.K_RIGHT]:
        paddleB.moveForward(Speed)
    all_sprites_list.update()
    if pygame.sprite.collide_mask(obstacle, paddleA):
        scoreA += 1
        X = int(random.random() * 500)
        Y = int(random.random() * 300)
    elif pygame.sprite.collide_mask(obstacle, paddleB):
        scoreB += 1
        X = int(random.random() * 500)
        Y = int(random.random() * 300)
    obstacle.rect.x = X
    obstacle.rect.y = Y
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))
    if scoreA >= 10:
        text = font.render('A win uwu',1,WHITE)
        screen.blit(bg_img,(250,350))
        screen.blit(text, (350, 250))
        mixer.music.unpause()
    elif scoreB >= 10:
        text = font.render('B win uwu',1,WHITE)
        screen.blit(text, (350, 250))
        screen.blit(bg_img,(350,250))
        mixer.music.unpause()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()