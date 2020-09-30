import pygame

pygame.init()

screen_width = 480
screen_height = 640
pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Stick figure's bttle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

#1_create_frame.py 명령어