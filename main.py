import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

wood_bg = pygame.image.load('assets/Wood_BG.png')
land_bg = pygame.image.load('assets/Land_BG.png')
water_bg = pygame.image.load('assets/Water_BG.png')
cloud1 = pygame.image.load('assets/Cloud1.png')
cloud2 = pygame.image.load('assets/Cloud2.png')
crosshair = pygame.image.load('assets/crosshair.png')
duck_surface = pygame.image.load('assets/duck.png')

game_font = pygame.font.Font(None, 60)
text_surface = game_font.render('You won!', True, (255, 255, 255))
text_rect = text_surface.get_rect(center =  (640, 360))
land_pos_y = 560
land_speed = 1

water_pos_y = 640
water_speed = 1.5

duck_list = []
for duck in range(20):
    duck_pos_x = random.randrange(70, 1200)
    duck_pos_y = random.randrange(120, 600)
    duck_rect = duck_surface.get_rect(center = (duck_pos_x, duck_pos_y))
    duck_list.append(duck_rect)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index,duck_rect in enumerate(duck_list):
                # if crosshair_rect.colliderect(duck_rect):
                if duck_rect.collidepoint(event.pos):
                    del duck_list[index]

    screen.blit(wood_bg, (0, 0))

    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)
    if len(duck_list) <= 0:
        screen.blit(text_surface, text_rect)

    land_pos_y -= land_speed
    if land_pos_y <= 520 or land_pos_y >= 600:
        land_speed *= -1
    screen.blit(land_bg, (0, land_pos_y))

    water_pos_y += water_speed
    if water_pos_y <= 620 or water_pos_y >= 680:
        water_speed *= -1
    screen.blit(water_bg, (0, water_pos_y))

    screen.blit(crosshair, crosshair_rect)
    screen.blit(cloud1,(70, 50))
    screen.blit(cloud2,(150, 80))
    screen.blit(cloud1,(604, 10))
    screen.blit(cloud2, (1000, 50))
    screen.blit(cloud1, (412, 55))


    pygame.display.update()
    clock.tick(170)
