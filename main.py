from tkinter.tix import INTEGER
import pygame, sys, random
import sqlite3
from button import Button

pygame.init()                                                                                                       # Inizializza la finestra

SCREEN = pygame.display.set_mode((1280, 720))                                                                       # Main screen
pygame.display.set_caption("Hangman Game")                                                                          # Titolo della finestra

BACKGROUND = pygame.image.load("assets/img.png")                                                                    # Carica il background
FONT = pygame.font.SysFont("Arial", 80, bold=True)                                                                  # Imposta il font
UNDERSCORE_FONT = pygame.font.SysFont("Arial", 60, bold=True)                                                       # Imposta il font per l'underscore

c = sqlite3.connect("hangman.db")
cu = c.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS stats (name TEXT, score INTEGER)")
c.commit()

# Problema: quando si aggiornerà lo score a fine partita, verrà resettato a 0 quando si inserisce nuovamente lo stesso nome
# Problema: nomi ripetuti nella tabella
def insertDB(DB_NAME, DB_SCORE) -> None:                                                                            # Funzione per inserire valori nel database
    CONNECT = sqlite3.connect("hangman.db")                                                                         # Connessione al database
    CURSOR = CONNECT.cursor()                                                                                       # Cursore per eseguire le query
    Q = "INSERT INTO stats (name, score) VALUES (?, ?)"                                                             # Query per inserire i valori
    TUPLA = (DB_NAME, DB_SCORE)                                                                                     # Tupla con i valori da inserire
    CURSOR.execute(Q, TUPLA)                                                                                        # Esecuzione della query
    CONNECT.commit()                                                                                                # Salva le modifiche

def getNameEng():
    USER_TEXT = ""
    INPUT_RECT = pygame.Rect(520, 250, 250, 40)
    NAME_FONT = pygame.font.SysFont("Arial", 30, bold=True)
    COUNTER = 0
    while True:
        SCREEN.fill("white")

        MOUSE_POS = pygame.mouse.get_pos()

        NAME_TEXT = FONT.render("INSERT YOUR NAME", True, "black")
        NAME_RECT = NAME_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(NAME_TEXT, NAME_RECT)

        pygame.draw.rect(SCREEN, "black", INPUT_RECT, 2)
        TEXT_SURF = NAME_FONT.render(USER_TEXT, True, "black")
        TEXT_RECT = TEXT_SURF.get_rect(center=(INPUT_RECT.centerx, INPUT_RECT.centery))
        SCREEN.blit(TEXT_SURF, TEXT_RECT)

        ENTER_BUT = Button(image=pygame.image.load("assets/rect2.png"),
                            pos=(850, 270),                                                               
                            text_input="ENTER", font=NAME_FONT,
                            base_color="black",
                            hovering_color="red")

        for botton in [ENTER_BUT]:
            botton.changeColor(MOUSE_POS)
            botton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    USER_TEXT = USER_TEXT[:-1]
                else:
                    COUNTER += 1
                    USER_TEXT += event.unicode
                    if COUNTER == 14:
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ENTER_BUT.checkForInput(MOUSE_POS):
                    DB_NAME = USER_TEXT
                    DB_SCORE = 0
                    insertDB(DB_NAME, DB_SCORE)
                    playMenuEng()

        pygame.display.update()

def getNameIta():
    USER_TEXT = ""
    INPUT_RECT = pygame.Rect(520, 250, 250, 40)
    NAME_FONT = pygame.font.SysFont("Arial", 30, bold=True)
    COUNTER = 0
    while True:
        SCREEN.fill("white")

        MOUSE_POS = pygame.mouse.get_pos()

        NAME_TEXT = FONT.render("INSERISCI IL TUO NOME", True, "black")
        NAME_RECT = NAME_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(NAME_TEXT, NAME_RECT)

        pygame.draw.rect(SCREEN, "black", INPUT_RECT, 2)
        TEXT_SURF = NAME_FONT.render(USER_TEXT, True, "black")
        TEXT_RECT = TEXT_SURF.get_rect(center=(INPUT_RECT.centerx, INPUT_RECT.centery))
        SCREEN.blit(TEXT_SURF, TEXT_RECT)

        ENTER_BUT = Button(image=pygame.image.load("assets/rect2.png"),
                            pos=(850, 270),                                                               
                            text_input="INVIO", font=NAME_FONT,
                            base_color="black",
                            hovering_color="red")

        for botton in [ENTER_BUT]:
            botton.changeColor(MOUSE_POS)
            botton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    USER_TEXT = USER_TEXT[:-1]
                else:
                    USER_TEXT += event.unicode
                    COUNTER += 1
                    if COUNTER > 14:
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ENTER_BUT.checkForInput(MOUSE_POS):
                    DB_NAME = USER_TEXT
                    DB_SCORE = 0
                    insertDB(DB_NAME, DB_SCORE)
                    playMenuEng()

        pygame.display.update()

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

def check_letter(c: str, s: str) -> list:
    lst = []
    for pos,char in enumerate(s):
        if(char == c):
            lst.append(pos)
    print(lst)
    return lst


def easyGameEng() -> None:
    WORDS = []
    with open("assets/wordlistengCorte.txt", "r") as f:                                                             # Apertura file con le parole
        for line in f:
            WORD = line.rstrip("\n")                                                                                
            WORDS.append(WORD)                                                                                      # Aggiunta delle parole alla lista
        RAND_WORD = random.choice(WORDS)                                                                            # Scelta di una parola a caso dalla lista
        RAND_WORD_LEN = len(RAND_WORD)
    print(RAND_WORD)
    
    lst = []

    while True:
        SCREEN.fill("white")

        GAME_MOUSE_POS = pygame.mouse.get_pos()

        COUNTER = 0
        SPACE = 10

        while COUNTER < RAND_WORD_LEN:                                                                              # Ciclo per stampare le lettere nascote della parola
            HIDDEN = UNDERSCORE_FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((60) + SPACE), (150))                                                           # Posizione delle lettere nascoste
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 50
            COUNTER += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)                                                      # Rettangolo delle lettere

        lst = check_letter("a",RAND_WORD)
        # lst_len = len(lst)
        # i = 0

        # while i<lst_len:
        #     letter_a = UNDERSCORE_FONT.render("a", True, "black")
        #     a_rect = letter_a.get_rect()
        #     a_rect.center = (((60) + lst[i]*SPACE), (150))  
        #     i += 1  
        
        SCREEN.blit(letter_a, a_rect)

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
            HIDDEN = UNDERSCORE_FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((60) + SPACE), (150))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 50
            COUNTER += 1
        
        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)   

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
            HIDDEN = UNDERSCORE_FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((60) + SPACE), (150))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 50
            COUNTER += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)   

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
            HIDDEN = UNDERSCORE_FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((60) + SPACE), (150))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 50
            COUNTER += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)   

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
            HIDDEN = UNDERSCORE_FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((60) + SPACE), (150))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 50
            COUNTER += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)   

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
            HIDDEN = UNDERSCORE_FONT.render("_", True, "black")
            HIDDEN_RECT = HIDDEN.get_rect()
            HIDDEN_RECT.center = (((60) + SPACE), (150))
            SCREEN.blit(HIDDEN, HIDDEN_RECT)
            SPACE += 50
            COUNTER += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)   

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
                    getNameEng()                                                                                    # Se si preme il bottone PLAY apre il menu di gioco
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
                    getNameIta()                                                                                    # Se si preme il bottone PLAY apre il menu di gioco
                if ENG_BUT.checkForInput(MOUSE_POS):
                    mainMenuEng()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

if __name__ == "__main__":  
    mainMenuEng()