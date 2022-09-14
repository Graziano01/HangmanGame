import pygame, sys, random
import sqlite3
from button import Button

pygame.init()                                                                                                       # Initialize the window

screen = pygame.display.set_mode((1280, 720))                                                                       # Main screen
pygame.display.set_caption("Hangman Game")                                                                          # Window's Title

background = pygame.image.load("assets/img.png")                                                                    # Load background image 
font = pygame.font.SysFont("Arial", 80, bold=True)                                                                  # Set font
font2 = pygame.font.SysFont("Arial", 60, bold=True)                                                                 # Set font2

c = sqlite3.connect("hangman.db")                                                                                   # Connecion to the database  
cu = c.cursor()                                                                                                     # Cursor for execute the query
cu.execute("CREATE TABLE IF NOT EXISTS stats (name TEXT, score INTEGER)")                                           # Create the table if not exists

# Problema: quando si aggiornerà lo score a fine partita, verrà resettato a 0 quando si inserisce nuovamente lo stesso nome
# Problema: nomi ripetuti nella tabella
def insert_db(db_name: str, db_score: int) -> None:                                                                 # Insert the name and the score in the database
    connect = sqlite3.connect("hangman.db")                                                                         # Connecion to the database
    cursor = connect.cursor()                                                                                       # Cursor for execute the query
    q = "INSERT INTO stats (name, score) VALUES (?, ?)"                                                             # Query
    tupla = (db_name, db_score)                                                                                     # Tuple
    cursor.execute(q, tupla)                                                                                        # Execute the query
    connect.commit()                                                                                                # Save the changes

def select_name_db() -> str:                                                                                        # Function for select the name from the database
    connect = sqlite3.connect("hangman.db")                                                                         # Connecion to the database
    cursor = connect.cursor()                                                                                       # Cursor for execute the query
    q = "SELECT name FROM stats"                                                                                    # Query
    cursor.execute(q)                                                                                               # Execute the query
    data = cursor.fetchall()                                                                                        # Fetch all the data
    return data                                                                                                     # Return the data

def select_score_db() -> int:                                                                                       # Function for select the score from the database
    connect = sqlite3.connect("hangman.db")                                                                         # Connecion to the database
    cursor = connect.cursor()                                                                                       # Cursor for execute the query
    q = "SELECT score FROM stats"                                                                                   # Query
    cursor.execute(q)                                                                                               # Execute the query
    data = cursor.fetchall()                                                                                        # Fetch all the data
    return data                                                                                                     # Return the data

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
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                    counter += 1
                    if counter > 14:
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if enter_but.checkForInput(mouse_pos):
                    db_name = user_text
                    db_score = 0
                    insert_db(db_name, db_score)
                    play_menu_eng()

        pygame.display.update()

def play_menu_eng() -> None:                                                                                        # Function for the english play menu
    while True:
        screen.fill("black")                                                                                        # Fill the screen with black color

        play_mouse_pos = pygame.mouse.get_pos()                                                                     # Get the mouse position

        play = font.render("SELECT THE DIFFICULTY", True, "orange")                                                 # Difficulty text
        play_rect = play.get_rect(center=(640, 100))                                                                # Center the text
        screen.blit(play, play_rect)                                                                                # Blit the text

        easy_but = Button(image=None, pos=(640, 250),                                                               # Easy game button
                            text_input="EASY", font=font,
                            base_color="white",
                            hovering_color="red")
        medium_but = Button(image=None, pos=(640,360),                                                              # Medium game button
                            text_input="MEDIUM", font=font,
                            base_color="white",
                            hovering_color="red")
        hard_but = Button(image=None, pos=(640, 470),                                                               # Hard game button
                            text_input="HARD", font=font,
                            base_color="white",
                            hovering_color="red")

        play_back = Button(image=None, pos=(140, 650),                                                              # Back button
                            text_input="BACK", font=font, 
                            base_color="white", 
                            hovering_color="green")

        for button in [easy_but, medium_but, hard_but, play_back]:
            button.changeColor(play_mouse_pos)                                                                      # Change the color of the button
            button.update(screen)                                                                                   # Update the button

        for event in pygame.event.get():                                                                            # Events
            if event.type == pygame.QUIT:                                                                           # If the user click on the close button
                pygame.quit()                                                                                       # Quit the game
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                                                                # If the user click on the mouse
                if play_back.checkForInput(play_mouse_pos):                                                         # If the user click on the back button
                    main_menu_eng()                                                                                 # Go to the english main menu
                if easy_but.checkForInput(play_mouse_pos):                                                          # If the user click on the easy button
                    easy_game_eng()                                                                                 # Go to the easy game
                if medium_but.checkForInput(play_mouse_pos):                                                        # If the user click on the medium button
                    med_game_eng()                                                                                  # Go to the medium game
                if hard_but.checkForInput(play_mouse_pos):                                                          # If the user click on the hard button
                    hard_game_eng()                                                                                 # Go to the hard game

        pygame.display.update()                                                                                     # Update the screen

def play_menu_ita() -> None:                                                                                        # Funzione per il Menu di Gioco Italiano
    while True:
        screen.fill("black")

        play_mouse_pos = pygame.mouse.get_pos()

        play = font.render("SELEZIONA LA DIFFICOLTA'", True, "orange")                                              # Difficulty text
        play_rect = play.get_rect(center=(640, 100))                                                                # Center the text
        screen.blit(play, play_rect)                                                                                # Blit the text

        play_back = Button(image=None, pos=(230, 650),                                                              # Back button
                            text_input="INDIETRO", font=font, 
                            base_color="white", 
                            hovering_color="green")

        easy_but = Button(image=None, pos=(640, 250),                                                               # Easy game button
                            text_input="FACILE", font=font,
                            base_color="white",
                            hovering_color="red")
        medium_but = Button(image=None, pos=(640,360),                                                              # Medium game button
                            text_input="MEDIO", font=font,
                            base_color="white",
                            hovering_color="red")
        hard_but = Button(image=None, pos=(640, 470),                                                               # Hard game button
                            text_input="DIFFICILE", font=font,
                            base_color="white",
                            hovering_color="red")

        for button in [easy_but, medium_but, hard_but, play_back]:
            button.changeColor(play_mouse_pos)                                                                      # Change the color of the button
            button.update(screen)                                                                                   # Update the button

        for event in pygame.event.get():                                                                            # Events
            if event.type == pygame.QUIT:                                                                           # If the user click on the close button
                pygame.quit()                                                                                       # Quit the game
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                                                                # If the user click on the mouse
                if play_back.checkForInput(play_mouse_pos):                                                         # If the user click on the back button
                    main_menu_ita()                                                                                 # Go to the italian main menu
                if easy_but.checkForInput(play_mouse_pos):                                                          # If the user click on the easy button
                    easy_game_ita()                                                                                 # Go to the easy game
                if medium_but.checkForInput(play_mouse_pos):                                                        # If the user click on the medium button
                    med_game_ita()                                                                                  # Go to the medium game
                if hard_but.checkForInput(play_mouse_pos):                                                          # If the user click on the hard button
                    hard_game_ita()                                                                                 # Go to the hard game

        pygame.display.update()

def stats_menu_eng() -> None:                                                                                       # Funzione per il Menu delle Statistiche Inglese   
    blacklist = ['(', ')', '[', ']',',',"'"]
    prova = []
    db_text = str(select_name_db())
    for char in blacklist:
        db_text = db_text.replace(char, '')
    print(db_text)
    for word in db_text:
        a = word.rstrip(" ")
        prova.append(a)
    print(prova)
    while True:
        screen.fill("black")

        stats_mouse_pos = pygame.mouse.get_pos()

        stats_text = font.render("STATS SCREEN", True, "white")
        stats_rect = stats_text.get_rect(center=(640, 100))
        screen.blit(stats_text, stats_rect)

        db_text = font.render(str(prova), True, "white")
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
            if event.type == pygame.MOUSEBUTTONDOWN:
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

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            hidden = font2.render("_", True, "black")
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
            hidden = font2.render("_", True, "black")
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
            hidden = font2.render("_", True, "black")
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
            hidden = font2.render("_", True, "black")
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
            hidden = font2.render("_", True, "black")
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
            hidden = font2.render("_", True, "black")
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


def main_menu_eng() -> None:                                                                                        # Funzione per il Menu Principale
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
            if event.type == pygame.MOUSEBUTTONDOWN:                
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
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if quit_but.checkForInput(mouse_pos):               
                    pygame.quit()
                    sys.exit()                                                                                      # Se si preme il bottone QUIT chiude la finestra
                if stats_but.checkForInput(mouse_pos):
                    stats_menu_ita()                                                                                # Se si preme il bottone STATS apre il menu delle statistiche
                if play_but.checkForInput(mouse_pos):
                    game_over_ita()                                                                               # Se si preme il bottone PLAY apre il menu di gioco
                if eng_but.checkForInput(mouse_pos):
                    main_menu_eng()
                if play_but.checkForInput(mouse_pos):
                    game_over_ita()                                                                                 # Se si preme il bottone PLAY apre il menu di gioco
                if eng_but.checkForInput(mouse_pos):
                    main_menu_eng()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

if __name__ == "__main__":  
    main_menu_eng()