import pygame, sys, random
import sqlite3
from button import Button

pygame.init()                                                                                                       # Inizializza la finestra

SCREEN = pygame.display.set_mode((1280, 720))                                                                       # Main Menu
pygame.display.set_caption("Hangman Game")                                                                          # Titolo della finestra

BACKGROUND = pygame.image.load("assets/img.png")                                                                    # Carica il background
FONT = pygame.font.SysFont("Arial", 80, bold=True)                                                                  # Imposta il font
LANGUAGE = "ENG"

"""
Database
"""
def connectDB() -> None:                                                                                            # Funzione per connettersi al database
    CONNECT = sqlite3.connect("hangman.db")                                                                         # Connessione al database
    CURSOR = CONNECT.cursor()
    Q = "CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, score INTEGER)"
    CURSOR.execute(Q)                                                                                               # Crea la tabella stats se non esiste

def selectWord() -> str:                                                                                            # Funzione per selezionare una parola random
    WORDS = []
    with open("assets/wordlist.txt") as f:                                                                          # Apre il file wordlist.txt
        for line in f:
            WORD = line.rstrip("\n")                                                                                # Rimuove il carattere di fine riga
            WORDS.append(WORD)                                                                                      # Aggiunge la parola alla lista
    RAND_WORD = random.choice(WORDS)                                                                                # Seleziona una parola random

def playMenuEng() -> None:                                                                                          # Funzione per il Menu di Gioco Inglese
    while True:
        SCREEN.fill("black")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = FONT.render("PLAY SCREEN", True, "white")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),                                                              # Bottone per tornare al menu principale
                            text_input="BACK", font=FONT, 
                            base_color="white", 
                            hovering_color="green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenuEng()

        pygame.display.update()

def playMenuIta() -> None:                                                                                          # Funzione per il Menu di Gioco Italiano
    while True:
        SCREEN.fill("black")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = FONT.render("SCHERMO DI GIOCO", True, "white")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),                                                              # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=FONT, 
                            base_color="white", 
                            hovering_color="green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenuIta()

        pygame.display.update()

def statsMenuEng() -> None:                                                                                         # Funzione per il Menu delle Statistiche
    while True:
        SCREEN.fill("black")

        STATS_MOUSE_POS = pygame.mouse.get_pos()

        STATS_TEXT = FONT.render("STATS SCREEN", True, "white")
        STATS_RECT = STATS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(STATS_TEXT, STATS_RECT)

        STATS_BACK = Button(image=None, pos=(640, 460),                                                             # Bottone per tornare al menu principale
                            text_input="BACK", font=FONT,
                            base_color="white", 
                            hovering_color="green")

        STATS_BACK.changeColor(STATS_MOUSE_POS)
        STATS_BACK.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STATS_BACK.checkForInput(STATS_MOUSE_POS):
                    mainMenuEng()
        
        pygame.display.update()

def statsMenuIta() -> None:                                                                                         # Funzione per il Menu delle Statistiche
    while True:
        SCREEN.fill("black")

        STATS_MOUSE_POS = pygame.mouse.get_pos()

        STATS_TEXT = FONT.render("SCHERMO STATISTICHE", True, "white")
        STATS_RECT = STATS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(STATS_TEXT, STATS_RECT)

        STATS_BACK = Button(image=None, pos=(640, 460),                                                             # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=FONT,
                            base_color="white", 
                            hovering_color="green")

        STATS_BACK.changeColor(STATS_MOUSE_POS)
        STATS_BACK.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STATS_BACK.checkForInput(STATS_MOUSE_POS):
                    mainMenuIta()
        
        pygame.display.update()

def mainMenuEng() -> None:                                                                                          # Funzione per il Menu Principale
    while True:
        LANGUAGE = "ENG"
        SCREEN.blit(BACKGROUND, (0, 0))                                                                             # Imposta il background

        MOUSE_POS = pygame.mouse.get_pos()                                                                          # Posizione del mouse

        PLAY_BUT = Button(image=pygame.image.load("assets/rect.png"),                                               # Bottone per giocare
                    pos=(1050, 80), text_input="PLAY", font=FONT,
                    base_color="black", hovering_color="red")

        STATS_BUT = Button(image=pygame.image.load("assets/rect.png"),                                              # Bottone per le statistiche
                    pos=(1050, 190), text_input="STATS", font=FONT,
                    base_color="black", hovering_color="red")

        QUIT_BUT = Button(image=pygame.image.load("assets/rect.png"),                                               # Bottone per uscire dal gioco
                    pos=(1050, 300), text_input="QUIT", font=FONT, 
                    base_color="black", hovering_color="red")

        ITA_BUT = Button(image=pygame.image.load("assets/ita.png"),
                    pos=(40, 40), text_input="", font=FONT,
                    base_color="black", hovering_color="red")

        for button in [PLAY_BUT, STATS_BUT, QUIT_BUT, ITA_BUT]:                                                     # Aggiorna i bottoni
            button.changeColor(MOUSE_POS)                                                                           # Cambia il colore del bottone
            button.update(SCREEN)                                                                                   # Aggiorna il bottone

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:                                                                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if QUIT_BUT.checkForInput(MOUSE_POS):               
                    pygame.quit()
                    sys.exit()                                                                                      # Se si preme il bottone QUIT chiude la finestra
                if STATS_BUT.checkForInput(MOUSE_POS):
                    if LANGUAGE == "ENG":
                        statsMenuEng()                                                                              # Se si preme il bottone STATS apre il menu delle statistiche
                    elif LANGUAGE == "ITA":
                        statsMenuIta()
                if PLAY_BUT.checkForInput(MOUSE_POS):
                    if LANGUAGE == "ENG":    
                        playMenuEng()                                                                               # Se si preme il bottone PLAY apre il menu di gioco
                    elif LANGUAGE == "ITA":
                        playMenuIta()
                if ITA_BUT.checkForInput(MOUSE_POS):
                    mainMenuIta()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

def mainMenuIta() -> None:                                                                                          # Funzione per il Menu Principale
    while True:
        LANGUAGE = "ITA"
        SCREEN.blit(BACKGROUND, (0, 0))                                                                             # Imposta il background

        MOUSE_POS = pygame.mouse.get_pos()                                                                          # Posizione del mouse

        PLAY_BUT = Button(image=pygame.image.load("assets/rect.png"),                                               # Bottone per giocare
                    pos=(1010, 80), text_input="GIOCA", font=FONT,
                    base_color="black", hovering_color="red")

        STATS_BUT = Button(image=pygame.image.load("assets/rect.png"),                                              # Bottone per le statistiche
                    pos=(1010, 190), text_input="STATISTICHE", font=FONT,
                    base_color="black", hovering_color="red")

        QUIT_BUT = Button(image=pygame.image.load("assets/rect.png"),                                               # Bottone per uscire dal gioco
                    pos=(1010, 300), text_input="ESCI", font=FONT, 
                    base_color="black", hovering_color="red")

        ENG_BUT = Button(image=pygame.image.load("assets/eng.png"),
                    pos=(40, 40), text_input="", font=FONT,
                    base_color="black", hovering_color="red")

        for button in [PLAY_BUT, STATS_BUT, QUIT_BUT, ENG_BUT]:                                                     # Aggiorna i bottoni
            button.changeColor(MOUSE_POS)                                                                           # Cambia il colore del bottone
            button.update(SCREEN)                                                                                   # Aggiorna il bottone

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:                                                                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if QUIT_BUT.checkForInput(MOUSE_POS):               
                    pygame.quit()
                    sys.exit()                                                                                      # Se si preme il bottone QUIT chiude la finestra
                if STATS_BUT.checkForInput(MOUSE_POS):
                    if LANGUAGE == "ITA":
                        statsMenuIta()                                                                              # Se si preme il bottone STATS apre il menu delle statistiche
                    elif LANGUAGE == "ENG":
                        statsMenuEng()
                if PLAY_BUT.checkForInput(MOUSE_POS):
                    if LANGUAGE == "ITA":    
                        playMenuIta()                                                                               # Se si preme il bottone PLAY apre il menu di gioco
                    elif LANGUAGE == "ENG":
                        playMenuEng()
                if ENG_BUT.checkForInput(MOUSE_POS):
                    mainMenuEng()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

if __name__ == "__main__":  
    mainMenuEng()