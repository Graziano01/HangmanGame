import pygame
from main import SCREEN

def draw(life: int) -> None:
    if life == 10:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
    elif life == 9:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
    elif life == 8:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
    elif life == 7:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
        pygame.draw.line(SCREEN, "black", [1100, 250], [1100, 300] ,10)
    elif life == 6:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
        pygame.draw.line(SCREEN, "black", [1100, 250], [1100, 300] ,10)
        pygame.draw.circle(SCREEN, "black", [1100, 325], 30)
    elif life == 5:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
        pygame.draw.line(SCREEN, "black", [1100, 250], [1100, 300] ,10)
        pygame.draw.circle(SCREEN, "black", [1100, 325], 30)
        pygame.draw.line(SCREEN, "black", [1100, 350], [1100, 500], 10)
    elif life == 4:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
        pygame.draw.line(SCREEN, "black", [1100, 250], [1100, 300] ,10)
        pygame.draw.circle(SCREEN, "black", [1100, 325], 30)
        pygame.draw.line(SCREEN, "black", [1100, 350], [1100, 500], 10)
        pygame.draw.line(SCREEN, "black", [1100, 500], [1050, 550], 10)
    elif life == 3:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
        pygame.draw.line(SCREEN, "black", [1100, 250], [1100, 300] ,10)
        pygame.draw.circle(SCREEN, "black", [1100, 325], 30)
        pygame.draw.line(SCREEN, "black", [1100, 350], [1100, 500], 10)
        pygame.draw.line(SCREEN, "black", [1100, 500], [1050, 550], 10)
        pygame.draw.line(SCREEN, "black", [1100, 500], [1150, 550], 10)
    elif life == 2:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
        pygame.draw.line(SCREEN, "black", [1100, 250], [1100, 300] ,10)
        pygame.draw.circle(SCREEN, "black", [1100, 325], 30)
        pygame.draw.line(SCREEN, "black", [1100, 350], [1100, 500], 10)
        pygame.draw.line(SCREEN, "black", [1100, 500], [1050, 550], 10)
        pygame.draw.line(SCREEN, "black", [1100, 500], [1150, 550], 10)
        pygame.draw.line(SCREEN, "black", [1100, 370], [1050, 380], 10)
    elif life == 1:
        pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        pygame.draw.line(SCREEN, "black", [800, 250], [800, 640] ,10)
        pygame.draw.rect(SCREEN, "black", [800, 250, 300, 10])
        pygame.draw.line(SCREEN, "black", [1100, 250], [1100, 300] ,10)
        pygame.draw.circle(SCREEN, "black", [1100, 325], 30)
        pygame.draw.line(SCREEN, "black", [1100, 350], [1100, 500], 10)
        pygame.draw.line(SCREEN, "black", [1100, 500], [1050, 550], 10)
        pygame.draw.line(SCREEN, "black", [1100, 500], [1150, 550], 10)
        pygame.draw.line(SCREEN, "black", [1100, 370], [1050, 380], 10)
        pygame.draw.line(SCREEN, "black", [1100, 370], [1150, 380], 10)