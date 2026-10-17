import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Offline Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

score_surface = test_font.render('Hopper', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,50))
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_hitbox = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_hitbox = player_surface.get_rect(midbottom = (80,300))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       # if event.type == pygame.MOUSEMOTION:
       #    if player_hitbox.collidepoint(event.pos):
       #        print('HI')
               
                            # w,h
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    screen.blit(score_surface, score_rect)

    #pygame.draw.line(screen,'black',(0,0),(800,400),10)
    #pygame.draw.ellipse(screen,'black',pygame.Rect(50,200,100,100))

    snail_hitbox.x -= 4
    if snail_hitbox.right <= 0:
        snail_hitbox.left = 800

    screen.blit(snail_surface,snail_hitbox)
    screen.blit(player_surface,player_hitbox)

    # 0 no hit or 1 hit
    #if player_hitbox.colliderect(snail_hitbox):

   # mouse_pos = pygame.mouse.get_pos()
   # if player_hitbox.collidepoint(mouse_pos):
   #     print(pygame.mouse.get_pressed())


    # Draw everything 
    # Update everything
    pygame.display.update()
    clock.tick(60) # Ceiling the frame rate to 60 frames per second


    
