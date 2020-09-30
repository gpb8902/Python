import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Stick figure's battle")

background = pygame.image.load("E:\\Python\\para.png")

character = pygame.image.load("E:\\Python\\test.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2
character_y_pos = screen_height - character_height

character1 = pygame.image.load("E:\\Python\\test1.png")
character1_size = character1.get_rect().size
character1_width = character1_size[0]
character1_height = character1_size[1]
character1_x_pos = screen_width / 4
character1_y_pos = screen_height - character_height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(character1, (character1_x_pos, character1_y_pos))

    pygame.display.update()

pygame.quit()