import pygame, sys
from button import Button

pygame.init()                                                       # Inizializza la finestra

SCREEN = pygame.display.set_mode((1280, 720))                       # Main Menu
pygame.display.set_caption("Hangman Game")                          # Titolo della finestra

BACKGROUND = pygame.image.load("img.png")                                   # Carica il background
FONT = pygame.font.SysFont("Arial", 80, bold=True)                  # Imposta il font

def mainMenu() -> None:                                             # Funzione per il Menu Principale
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))                                     # Imposta il background

        MOUSE_POS = pygame.mouse.get_pos()                          # Posizione del mouse

        QUIT_BUT = Button(image=pygame.image.load("quit.png"),      # Bottone per uscire dal gioco
                    pos=(640, 460), text_input="QUIT", font=FONT, 
                    base_color="black", hovering_color="red")

        TESTO_MENU1 = FONT.render("PROVA 1", True, "black")         # Testo 1
        TESTO_CENT1 = TESTO_MENU1.get_rect(center=(1000, 80))       # Posizione testo 1
        
        TESTO_MENU2 = FONT.render("PROVA 2", True, "black")         # Testo 2
        TESTO_CENT2 = TESTO_MENU2.get_rect(center=(1000, 170))      # Posizione testo 2
        
        TESTO_MENU3 = FONT.render("PROVA 3", True, "black")         # Testo 3
        TESTO_CENT3 = TESTO_MENU3.get_rect(center=(1000, 250))      # Posizione testo 3
        
        SCREEN.blit(TESTO_MENU1, TESTO_CENT1)                       # Colloca testo 1 nello schermo
        SCREEN.blit(TESTO_MENU2, TESTO_CENT2)                       # Colloca testo 2 nello schermo
        SCREEN.blit(TESTO_MENU3, TESTO_CENT3)                       # Colloca testo 3 nello schermo

        for button in [QUIT_BUT]:                                   
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