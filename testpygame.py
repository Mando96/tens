import pygame

pygame.init()
screen = pygame.display.set_mode((900,500))
pygame.display.set_caption("Tens")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')

test_surface = pygame.image.load('img/grasss.jpg').convert()
card = pygame.image.load('img/qd.png').convert()
text_surface = test_font.render("Tens", False, 'Green')
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))
    screen.blit(card,(0,0))
    screen.blit(text_surface,(300,50))

    pygame.display.update()
    clock.tick(60)

