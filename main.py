import pygame, sys
from button import Button

pygame.init()                                                       # Inizializza la finestra

SCREEN = pygame.display.set_mode((1280, 720))                       # Main Menu
pygame.display.set_caption("Hangman Game")                          # Titolo della finestra

BACKGROUND = pygame.image.load("img.png")                           # Carica il background
FONT = pygame.font.SysFont("Arial", 80, bold=True)                  # Imposta il font

def mainMenu() -> None:                                             # Funzione per il Menu Principale
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))                             # Imposta il background

        MOUSE_POS = pygame.mouse.get_pos()                          # Posizione del mouse

        PLAY_BUT = Button(image=pygame.image.load("rect.png"),      # Bottone per giocare
                    pos=(1050, 80), text_input="PLAY", font=FONT,
                    base_color="black", hovering_color="red")

        STATS_BUT = Button(image=pygame.image.load("rect.png"),     # Bottone per le statistiche
                    pos=(1050, 190), text_input="STATS", font=FONT,
                    base_color="black", hovering_color="red")

        QUIT_BUT = Button(image=pygame.image.load("rect.png"),      # Bottone per uscire dal gioco
                    pos=(1050, 300), text_input="QUIT", font=FONT, 
                    base_color="black", hovering_color="red")

        for button in [PLAY_BUT, STATS_BUT, QUIT_BUT]:                                   
            button.changeColor(MOUSE_POS)                           # Cambia il colore del bottone
            button.update(SCREEN)                                   # Aggiorna il bottone

        for event in pygame.event.get():                            # Eventi
            if event.type == pygame.QUIT:                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if QUIT_BUT.checkForInput(MOUSE_POS):               
                    pygame.quit()
                    sys.exit()                                      # Se si preme il bottone QUIT chiude la finestra

        pygame.display.update()                                     # Aggiorna lo schermo

if __name__ == "__main__":
    mainMenu()