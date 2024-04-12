import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

def draw_circle():
    pygame.draw.circle(win, FIOLETOWY, (300, 300), 150)

def draw_square():
    pygame.draw.rect(win, CZERWONY , (225, 225, 150, 150))

def draw_triangle():
    points = [(300, 150), (225, 375), (375, 375)]
    pygame.draw.polygon(win, ZIELONY, points)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                draw_circle()  # Koło
            elif event.key == pygame.K_2:
                draw_square()  # Kwadrat
            elif event.key == pygame.K_3:
                draw_triangle()  # Trójkąt

    pygame.display.update()

pygame.quit()
