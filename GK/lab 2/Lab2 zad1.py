import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Przekształcenia wielokąta")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)


# Funkcja do rysowania wielokąta o n wierzchołkach
def draw_polygon(n, radius, center_x, center_y, color):
    vertices = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        vertices.append((x, y))
    pygame.draw.polygon(win, color, vertices)


# Inicjalizacja parametrów wielokąta
num_vertices = 11  # Domyślnie pięciokąt
radius = 150
center_x = 300
center_y = 300
color = CZERWONY

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # Zmiana wielkości wielokąta na podstawie wciśniętego klawisza
            if event.key == pygame.K_1:
                num_vertices = 3  # Trójkąt
            elif event.key == pygame.K_2:
                num_vertices = 4  # Czworokąt
            elif event.key == pygame.K_3:
                num_vertices = 5  # Pięciokąt
            elif event.key == pygame.K_4:
                num_vertices = 6  # Sześciokąt
            elif event.key == pygame.K_5:
                num_vertices = 7  # Siedmiokąt
            elif event.key == pygame.K_6:
                num_vertices = 8  # Ośmiokąt
            elif event.key == pygame.K_7:
                num_vertices = 9  # Dziewięciokąt
            elif event.key == pygame.K_8:
                num_vertices = 10  # Dziesięciokąt
            elif event.key == pygame.K_9:
                num_vertices = 12  # Dwunastokąt

    # Czyszczenie okna
    win.fill((0, 0, 0))

    # Rysowanie wielokąta
    draw_polygon(num_vertices, radius, center_x, center_y, color)

    # Odświeżenie ekranu
    pygame.display.update()

pygame.quit()
