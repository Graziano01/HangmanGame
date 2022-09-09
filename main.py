import pygame, sys, random
import sqlite3
from button import Button

pygame.init()                                                                                                       # Inizializza la finestra

screen = pygame.display.set_mode((1280, 720))                                                                       # Main screen
pygame.display.set_caption("Hangman Game")                                                                          # Titolo della finestra

background = pygame.image.load("assets/img.png")                                                                    # Carica il background
font = pygame.font.SysFont("Arial", 80, bold=True)                                                                  # Imposta il font
underscore_font = pygame.font.SysFont("Arial", 60, bold=True)                                                       # Imposta il font per l'underscore

c = sqlite3.connect("hangman.db")
cu = c.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS stats (name TEXT, score INTEGER)")
c.commit()

# Problema: quando si aggiornerà lo score a fine partita, verrà resettato a 0 quando si inserisce nuovamente lo stesso nome
# Problema: nomi ripetuti nella tabella
def insert_db(db_name: str, db_score: int) -> None:                                                                 # Funzione per inserire valori nel database
    connect = sqlite3.connect("hangman.db")                                                                         # Connessione al database
    cursor = connect.cursor()                                                                                       # cursore per eseguire le query
    q = "INSERT INTO stats (name, score) VALUES (?, ?)"                                                             # query per inserire i valori
    tupla = (db_name, db_score)                                                                                     # tupla con i valori da inserire
    cursor.execute(q, tupla)                                                                                        # Esecuzione della query
    connect.commit()                                                                                                # Salva le modifiche

def select_name_db() -> str:
    connect = sqlite3.connect("hangman.db")
    cursor = connect.cursor()
    q = "SELECT name FROM stats"
    cursor.execute(q)
    data = cursor.fetchall()
    return data

def select_score_db() -> int:
    connect = sqlite3.connect("hangman.db")
    cursor = connect.cursor()
    q = "SELECT score FROM stats"
    cursor.execute(q)
    data = cursor.fetchall()
    return data

def game_over_eng():
    user_text = ""
    input_rect = pygame.Rect(520, 250, 250, 40)
    name_font = pygame.font.SysFont("Arial", 30, bold=True)
    counter = 0
    while True:
        screen.fill("white")

        mouse_pos = pygame.mouse.get_pos()

        name_text = font.render("INSERT YOUR NAME", True, "black")
        name_rect = name_text.get_rect(center=(640, 100))
        screen.blit(name_text, name_rect)

        pygame.draw.rect(screen, "black", input_rect, 2)
        text_surf = name_font.render(user_text, True, "black")
        text_rect = text_surf.get_rect(center=(input_rect.centerx, input_rect.centery))
        screen.blit(text_surf, text_rect)

        enter_but = Button(image=pygame.image.load("assets/rect2.png"),
                            pos=(850, 270),                                                               
                            text_input="ENTER", font=name_font,
                            base_color="black",
                            hovering_color="red")

        for botton in [enter_but]:
            botton.changeColor(mouse_pos)
            botton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_backspace:
                    user_text = user_text[:-1]
                else:
                    counter += 1
                    user_text += event.unicode
                    if counter == 14:
                        break
            if event.type == pygame.mousebottondown:
                if enter_but.checkForInput(mouse_pos):
                    db_name = user_text
                    db_score = 0
                    insert_db(db_name, db_score)
                    play_menu_eng()

        pygame.display.update()

def game_over_ita() -> None:
    user_text = ""
    input_rect = pygame.Rect(520, 250, 250, 40)
    name_font = pygame.font.SysFont("Arial", 30, bold=True)
    counter = 0
    while True:
        screen.fill("white")

        mouse_pos = pygame.mouse.get_pos()

        name_text = font.render("INSERISCI IL TUO NOME", True, "black")
        name_rect = name_text.get_rect(center=(640, 100))
        screen.blit(name_text, name_rect)

        pygame.draw.rect(screen, "black", input_rect, 2)
        text_surf = name_font.render(user_text, True, "black")
        text_rect = text_surf.get_rect(center=(input_rect.centerx, input_rect.centery))
        screen.blit(text_surf, text_rect)

        enter_but = Button(image=pygame.image.load("assets/rect2.png"),
                            pos=(850, 270),                                                               
                            text_input="INVIO", font=name_font,
                            base_color="black",
                            hovering_color="red")

        for botton in [enter_but]:
            botton.changeColor(mouse_pos)
            botton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKspace:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                    counter += 1
                    if counter > 14:
                        break
            if event.type == pygame.mousebottondown:
                if enter_but.checkForInput(mouse_pos):
                    db_name = user_text
                    db_score = 0
                    insert_db(db_name, db_score)
                    play_menu_eng()

        pygame.display.update()

def play_menu_eng() -> None:                                                                                        # Funzione per il Menu di Gioco Inglese
    while True:
        screen.fill("black")

        play_mouse_pos = pygame.mouse.get_pos()

        play = font.render("SELECT THE DIFFICULTY", True, "orange")                                                 # Testo selezione difficolta'
        play_rect = play.get_rect(center=(640, 100))
        screen.blit(play, play_rect)

        easy_but = Button(image=None, pos=(640, 250),                                                               # Bottone partita facile
                            text_input="EASY", font=font,
                            base_color="white",
                            hovering_color="red")
        medium_but = Button(image=None, pos=(640,360),                                                              # Bottone partita media
                            text_input="MEDIUM", font=font,
                            base_color="white",
                            hovering_color="red")
        hard_but = Button(image=None, pos=(640, 470),                                                               # Bottone partita difficile
                            text_input="HARD", font=font,
                            base_color="white",
                            hovering_color="red")

        play_back = Button(image=None, pos=(140, 650),                                                              # Bottone per tornare al menu principale
                            text_input="BACK", font=font, 
                            base_color="white", 
                            hovering_color="green")

        for button in [easy_but, medium_but, hard_but, play_back]:
            button.changeColor(play_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():                                                                             # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.mousebottondown:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu_eng()
                if easy_but.checkForInput(play_mouse_pos):
                    easy_game_eng()
                if medium_but.checkForInput(play_mouse_pos):
                    med_game_eng()
                if hard_but.checkForInput(play_mouse_pos):
                    hard_game_eng()

        pygame.display.update()

def play_menu_ita() -> None:                                                                                          # Funzione per il Menu di Gioco Italiano
    while True:
        screen.fill("black")

        play_mouse_pos = pygame.mouse.get_pos()

        play = font.render("SELEZIONA LA DIFFICOLTA'", True, "orange")                                                # Testo selezione difficoltà
        play_rect = play.get_rect(center=(640, 100))
        screen.blit(play, play_rect)

        play_back = Button(image=None, pos=(230, 650),                                                                # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=font, 
                            base_color="white", 
                            hovering_color="green")

        easy_but = Button(image=None, pos=(640, 250),                                                                 # Bottone partita facile
                            text_input="FACILE", font=font,
                            base_color="white",
                            hovering_color="red")
        medium_but = Button(image=None, pos=(640,360),                                                                # Bottone partita media
                            text_input="MEDIO", font=font,
                            base_color="white",
                            hovering_color="red")
        hard_but = Button(image=None, pos=(640, 470),                                                                 # Bottone partita difficile
                            text_input="DIFFICILE", font=font,
                            base_color="white",
                            hovering_color="red")

        for button in [easy_but, medium_but, hard_but, play_back]:
            button.changeColor(play_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():                                                                              # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.mousebottondown:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu_ita()
                if easy_but.checkForInput(play_mouse_pos):
                    easy_game_ita()
                if medium_but.checkForInput(play_mouse_pos):
                    med_game_ita()
                if hard_but.checkForInput(play_mouse_pos):
                    hard_game_ita()

        pygame.display.update()

def stats_menu_eng() -> None:                                                                                         # Funzione per il Menu delle Statistiche Inglese   
    blacklist = ["()[],'"]
    db_text = select_name_db()
    for letter in blacklist:
        db_text = db_text.replace(letter, "")
    while True:
        screen.fill("black")

        stats_mouse_pos = pygame.mouse.get_pos()

        stats_text = font.render("STATS SCREEN", True, "white")
        stats_rect = stats_text.get_rect(center=(640, 260))
        screen.blit(stats_text, stats_rect)

        db_text = font.render(str(db_text), True, "white")
        db_rect = db_text.get_rect(center=(640, 400))
        screen.blit(db_text, db_rect)

        stats_back = Button(image=None, pos=(150, 600),                                                              # Bottone per tornare al menu principale
                            text_input="BACK", font=font,
                            base_color="white", 
                            hovering_color="green")

        stats_back.changeColor(stats_mouse_pos)
        stats_back.update(screen)

        for event in pygame.event.get():                                                                             # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.mousebottondown:
                if stats_back.checkForInput(stats_mouse_pos):
                    main_menu_eng()
        
        pygame.display.update()

def stats_menu_ita() -> None:                                                                                        # Funzione per il Menu delle Statistiche
    while True:
        screen.fill("black")

        stats_mouse_pos = pygame.mouse.get_pos()

        stats_text = font.render("SCHERMO STATISTICHE", True, "white")
        stats_rect = stats_text.get_rect(center=(640, 260))
        screen.blit(stats_text, stats_rect)

        stats_back = Button(image=None, pos=(640, 460),                                                              # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=font,
                            base_color="white", 
                            hovering_color="green")

        stats_back.changeColor(stats_mouse_pos)
        stats_back.update(screen)

        for event in pygame.event.get():                                                                             # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.mousebottondown:
                if stats_back.checkForInput(stats_mouse_pos):
                    main_menu_ita()
        
        pygame.display.update()

def easy_game_eng() -> None:
    words = []
    with open("assets/wordlistengCorte.txt", "r") as f:                                                             # Apertura file con le parole
        for line in f:
            word = line.rstrip("\n")                                                                                
            words.append(word)                                                                                      # Aggiunta delle parole alla lista
        rand_word = random.choice(words)                                                                            # Scelta di una parola a caso dalla lista
        rand_word_len = len(rand_word)
    print(rand_word)
    
    while True:
        screen.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:                                                                              # Ciclo per stampare le lettere nascote della parola
            hidden = underscore_font.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))                                                            # Posizione delle lettere nascoste
            screen.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        pygame.draw.rect(screen, "black", [50,300,550,350],2)                                                       # Rettangolo delle lettere

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def med_game_eng() -> None:
    words = []
    with open("assets/wordlistengMedie.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
        rand_word_len = len(rand_word)
    print(rand_word)
    
    while True:
        screen.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:
            hidden = underscore_font.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))
            screen.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def hard_game_eng() -> None:
    words = []
    with open("assets/wordlistengLunghe.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
        rand_word_len = len(rand_word)
    print(rand_word)
    
    while True:
        screen.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:
            hidden = underscore_font.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))
            screen.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def easy_game_ita() -> None:
    words = []
    with open("assets/wordlistitaCorte.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
        rand_word_len = len(rand_word)
    print(rand_word)
    
    while True:
        screen.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:
            hidden = underscore_font.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))
            screen.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def med_game_ita() -> None:
    words = []
    with open("assets/wordlistitaMedie.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
        rand_word_len = len(rand_word)
    print(rand_word)
    
    while True:
        screen.fill("white")

        GAME_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:
            hidden = underscore_font.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))
            screen.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def hard_game_ita() -> None:
    words = []
    with open("assets/wordlistitaLunghe.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
        rand_word_len = len(rand_word)
    print(rand_word)
    
    while True:
        screen.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:
            hidden = underscore_font.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))
            screen.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main_menu_eng() -> None:                                                                                          # Funzione per il Menu Principale
    while True:
        screen.blit(background, (0, 0))                                                                             # Imposta il background

        mouse_pos = pygame.mouse.get_pos()                                                                          # Posizione del mouse

        play_but = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per giocare
                    pos=(1050, 80), text_input="PLAY", font=font,
                    base_color="black", hovering_color="red")

        stats_but = Button(image=pygame.image.load("assets/rect.png"),                                              # Bottone per le statistiche
                    pos=(1050, 190), text_input="STATS", font=font,
                    base_color="black", hovering_color="red")

        quit_but = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per uscire dal gioco
                    pos=(1050, 300), text_input="QUIT", font=font, 
                    base_color="black", hovering_color="red")

        ita_but = Button(image=pygame.image.load("assets/ita.png"),
                    pos=(40, 40), text_input="", font=font,
                    base_color="black", hovering_color="red")

        for button in [play_but, stats_but, quit_but, ita_but]:                                                     # Aggiorna i bottoni
            button.changeColor(mouse_pos)                                                                           # Cambia il colore del bottone
            button.update(screen)                                                                                   # Aggiorna il bottone

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:                                                                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.mousebottondown:                
                if quit_but.checkForInput(mouse_pos):               
                    pygame.quit()
                    sys.exit()                                                                                      # Se si preme il bottone QUIT chiude la finestra
                if stats_but.checkForInput(mouse_pos):
                    stats_menu_eng()                                                                                  # Se si preme il bottone STATS apre il menu delle statistiche
                if play_but.checkForInput(mouse_pos):   
                    play_menu_eng()                                                                                    # Se si preme il bottone PLAY apre il menu di gioco
                if ita_but.checkForInput(mouse_pos):
                    main_menu_ita()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

def main_menu_ita() -> None:                                                                                          # Funzione per il Menu Principale
    while True:
        screen.blit(background, (0, 0))                                                                             # Imposta il background

        mouse_pos = pygame.mouse.get_pos()                                                                          # Posizione del mouse

        play_but = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per giocare
                    pos=(1010, 80), text_input="GIOCA", font=font,
                    base_color="black", hovering_color="red")

        stats_but = Button(image=pygame.image.load("assets/rect1.png"),                                             # Bottone per le statistiche
                    pos=(1010, 190), text_input="STATISTICHE", font=font,
                    base_color="black", hovering_color="red")

        quit_but = Button(image=pygame.image.load("assets/rect2.png"),                                              # Bottone per uscire dal gioco
                    pos=(1010, 300), text_input="ESCI", font=font, 
                    base_color="black", hovering_color="red")

        eng_but = Button(image=pygame.image.load("assets/eng.png"),
                    pos=(40, 40), text_input="", font=font,
                    base_color="black", hovering_color="red")

        for button in [play_but, stats_but, quit_but, eng_but]:                                                     # Aggiorna i bottoni
            button.changeColor(mouse_pos)                                                                           # Cambia il colore del bottone
            button.update(screen)                                                                                   # Aggiorna il bottone

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:                                                                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.mousebottondown:                
                if quit_but.checkForInput(mouse_pos):               
                    pygame.quit()
                    sys.exit()                                                                                      # Se si preme il bottone QUIT chiude la finestra
                if stats_but.checkForInput(mouse_pos):
                    stats_menu_ita()                                                                                # Se si preme il bottone STATS apre il menu delle statistiche
                if play_but.checkForInput(mouse_pos):
                    play_menu_ita()                                                                                 # Se si preme il bottone PLAY apre il menu di gioco
                if eng_but.checkForInput(mouse_pos):
                    main_menu_eng()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

if __name__ == "__main__":  
    main_menu_eng()