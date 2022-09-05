import pygame, sys, random
import sqlite3
from button import Button

pygame.init()                                                                                                       # Inizializza la finestra

SCREEN = pygame.display.set_mode((1280, 720))                                                                       # Main screen
pygame.display.set_caption("Hangman Game")                                                                          # Titolo della finestra

BACKGROUND = pygame.image.load("assets/img.png")                                                                    # Carica il background
FONT = pygame.font.SysFont("Arial", 80, bold=True)                                                                  # Imposta il font

def connectDB() -> None:                                                                                            # Funzione per connettersi al database
    CONNECT = sqlite3.connect("hangman.db")                                                                         # Connessione al database
    CURSOR = CONNECT.cursor()                                                                                       # Cursore per eseguire le query
    Q = "CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, score INTEGER)"# Query
    CURSOR.execute(Q)                                                                                               # Esegui la query

def playMenuEng() -> None:                                                                                          # Funzione per il Menu di Gioco Inglese
    while True:
        SCREEN.fill("black")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = FONT.render("SELECT THE DIFFICULTY", True, "orange")                                            # Testo selezione difficolta'
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        EASY_BUT = Button(image=None, pos=(640, 250),                                                               # Bottone partita facile
                            text_input="EASY", font=FONT,
                            base_color="white",
                            hovering_color="red")
        MEDIUM_BUT = Button(image=None, pos=(640,360),                                                              # Bottone partita media
                            text_input="MEDIUM", font=FONT,
                            base_color="white",
                            hovering_color="red")
        HARD_BUT = Button(image=None, pos=(640, 470),                                                               # Bottone partita difficile
                            text_input="HARD", font=FONT,
                            base_color="white",
                            hovering_color="red")

        PLAY_BACK = Button(image=None, pos=(140, 650),                                                              # Bottone per tornare al menu principale
                            text_input="BACK", font=FONT, 
                            base_color="white", 
                            hovering_color="green")

        for button in [EASY_BUT, MEDIUM_BUT, HARD_BUT, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenuEng()
                if EASY_BUT.checkForInput(PLAY_MOUSE_POS):
                    easyGameEng()
                if MEDIUM_BUT.checkForInput(PLAY_MOUSE_POS):
                    medGameEng()
                if HARD_BUT.checkForInput(PLAY_MOUSE_POS):
                    hardGameEng()

        pygame.display.update()

def playMenuIta() -> None:                                                                                          # Funzione per il Menu di Gioco Italiano
    while True:
        SCREEN.fill("black")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = FONT.render("SELEZIONA LA DIFFICOLTA'", True, "orange")                                         # Testo selezione difficoltà
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(230, 650),                                                              # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=FONT, 
                            base_color="white", 
                            hovering_color="green")

        EASY_BUT = Button(image=None, pos=(640, 250),                                                               # Bottone partita facile
                            text_input="FACILE", font=FONT,
                            base_color="white",
                            hovering_color="red")
        MEDIUM_BUT = Button(image=None, pos=(640,360),                                                              # Bottone partita media
                            text_input="MEDIO", font=FONT,
                            base_color="white",
                            hovering_color="red")
        HARD_BUT = Button(image=None, pos=(640, 470),                                                               # Bottone partita difficile
                            text_input="DIFFICILE", font=FONT,
                            base_color="white",
                            hovering_color="red")

        for button in [EASY_BUT, MEDIUM_BUT, HARD_BUT, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenuIta()
                if EASY_BUT.checkForInput(PLAY_MOUSE_POS):
                    easyGameIta()
                if MEDIUM_BUT.checkForInput(PLAY_MOUSE_POS):
                    medGameIta()
                if HARD_BUT.checkForInput(PLAY_MOUSE_POS):
                    hardGameIta()

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

def easyGameEng() -> None:
    WORDS = []
    with open("assets/wordlistengCorte.txt", "r") as f:
        for line in f:
            WORD = line.rstrip("\n")
            WORDS.append(WORD)
        RAND_WORD = random.choice(WORDS)
        RAND_WORD_LEN = len(RAND_WORD)
    print(RAND_WORD)
    
    while True:
        SCREEN.fill("white")

        GAME_MOUSE_POS = pygame.mouse.get_pos()

        COUNTER = 0
        SPACE = 10

        while COUNTER < RAND_WORD_LEN:
            HIDDEN = FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((500) + SPACE), (300))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 60
            COUNTER += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def medGameEng() -> None:
    WORDS = []
    with open("assets/wordlistengMedie.txt", "r") as f:
        for line in f:
            WORD = line.rstrip("\n")
            WORDS.append(WORD)
        RAND_WORD = random.choice(WORDS)
        RAND_WORD_LEN = len(RAND_WORD)
    print(RAND_WORD)
    
    while True:
        SCREEN.fill("white")

        GAME_MOUSE_POS = pygame.mouse.get_pos()

        COUNTER = 0
        SPACE = 10

        while COUNTER < RAND_WORD_LEN:
            HIDDEN = FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((500) + SPACE), (300))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 60
            COUNTER += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def hardGameEng() -> None:
    WORDS = []
    with open("assets/wordlistengLunghe.txt", "r") as f:
        for line in f:
            WORD = line.rstrip("\n")
            WORDS.append(WORD)
        RAND_WORD = random.choice(WORDS)
        RAND_WORD_LEN = len(RAND_WORD)
    print(RAND_WORD)
    
    while True:
        SCREEN.fill("white")

        GAME_MOUSE_POS = pygame.mouse.get_pos()

        COUNTER = 0
        SPACE = 10

        while COUNTER < RAND_WORD_LEN:
            HIDDEN = FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((500) + SPACE), (300))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 60
            COUNTER += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def easyGameIta() -> None:
    WORDS = []
    with open("assets/wordlistitaCorte.txt", "r") as f:
        for line in f:
            WORD = line.rstrip("\n")
            WORDS.append(WORD)
        RAND_WORD = random.choice(WORDS)
        RAND_WORD_LEN = len(RAND_WORD)
    print(RAND_WORD)
    
    while True:
        SCREEN.fill("white")

        GAME_MOUSE_POS = pygame.mouse.get_pos()

        COUNTER = 0
        SPACE = 10

        while COUNTER < RAND_WORD_LEN:
            HIDDEN = FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((500) + SPACE), (300))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 60
            COUNTER += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def medGameIta() -> None:
    WORDS = []
    with open("assets/wordlistitaMedie.txt", "r") as f:
        for line in f:
            WORD = line.rstrip("\n")
            WORDS.append(WORD)
        RAND_WORD = random.choice(WORDS)
        RAND_WORD_LEN = len(RAND_WORD)
    print(RAND_WORD)
    
    while True:
        SCREEN.fill("white")

        GAME_MOUSE_POS = pygame.mouse.get_pos()

        COUNTER = 0
        SPACE = 10

        while COUNTER < RAND_WORD_LEN:
            HIDDEN = FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((500) + SPACE), (300))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 60
            COUNTER += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def hardGameIta() -> None:
    WORDS = []
    with open("assets/wordlistitaLunghe.txt", "r") as f:
        for line in f:
            WORD = line.rstrip("\n")
            WORDS.append(WORD)
        RAND_WORD = random.choice(WORDS)
        RAND_WORD_LEN = len(RAND_WORD)
    print(RAND_WORD)
    
    while True:
        SCREEN.fill("white")

        GAME_MOUSE_POS = pygame.mouse.get_pos()

        COUNTER = 0
        SPACE = 10

        while COUNTER < RAND_WORD_LEN:
            HIDDEN = FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((500) + SPACE), (300))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 60
            COUNTER += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def mainMenuEng() -> None:                                                                                          # Funzione per il Menu Principale
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))                                                                             # Imposta il background

        MOUSE_POS = pygame.mouse.get_pos()                                                                          # Posizione del mouse

        PLAY_BUT = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per giocare
                    pos=(1050, 80), text_input="PLAY", font=FONT,
                    base_color="black", hovering_color="red")

        STATS_BUT = Button(image=pygame.image.load("assets/rect.png"),                                              # Bottone per le statistiche
                    pos=(1050, 190), text_input="STATS", font=FONT,
                    base_color="black", hovering_color="red")

        QUIT_BUT = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per uscire dal gioco
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
                    statsMenuEng()                                                                                  # Se si preme il bottone STATS apre il menu delle statistiche
                if PLAY_BUT.checkForInput(MOUSE_POS):   
                    playMenuEng()                                                                                   # Se si preme il bottone PLAY apre il menu di gioco
                if ITA_BUT.checkForInput(MOUSE_POS):
                    mainMenuIta()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

def mainMenuIta() -> None:                                                                                          # Funzione per il Menu Principale
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))                                                                             # Imposta il background

        MOUSE_POS = pygame.mouse.get_pos()                                                                          # Posizione del mouse

        PLAY_BUT = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per giocare
                    pos=(1010, 80), text_input="GIOCA", font=FONT,
                    base_color="black", hovering_color="red")

        STATS_BUT = Button(image=pygame.image.load("assets/rect1.png"),                                             # Bottone per le statistiche
                    pos=(1010, 190), text_input="STATISTICHE", font=FONT,
                    base_color="black", hovering_color="red")

        QUIT_BUT = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per uscire dal gioco
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
                    statsMenuIta()                                                                                  # Se si preme il bottone STATS apre il menu delle statistiche
                if PLAY_BUT.checkForInput(MOUSE_POS):
                    playMenuIta()                                                                                   # Se si preme il bottone PLAY apre il menu di gioco
                if ENG_BUT.checkForInput(MOUSE_POS):
                    mainMenuEng()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

if __name__ == "__main__":  
    mainMenuEng()