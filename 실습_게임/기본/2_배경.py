import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Stick figure's battle")

background = pygame.image.load("E:\\Python\\para.png")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()

#2_create_frame.py 명령어