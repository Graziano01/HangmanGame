import pygame, sys, random
import sqlite3
from button import Button

pygame.init()                                                                                                       # Initialize the window

SCREEN = pygame.display.set_mode((1280, 720))                                                                       # Main screen
pygame.display.set_caption("Hangman Game")                                                                          # Window's Title

global contprova

BACKGROUND = pygame.image.load("assets/img.png")                                                                    # Load background image 
font = pygame.font.SysFont("Arial", 80, bold=True)                                                                  # Set font
font2 = pygame.font.SysFont("Arial", 60, bold=True)                                                                 # Set font2

text_box_space = 5
text_box_num = 0

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

def get_word(a) -> str:                                                                                             # Function for get the word from the dictionary file
    words = []
    if a == "ee":                                                                                                   # English Easy
        with open("assets/wordlistengCorte.txt", "r") as f:                                                         # Open the file in read mode
            for line in f:                                                                                          # For each line in the file
                word = line.rstrip("\n")                                                                            # Remove the \n from the line
                words.append(word)                                                                                  # Append the word to the list
            rand_word = random.choice(words)                                                                        # Choose a random word from the list
            return rand_word
    elif a == "em":                                                                                                 # English Medium
        with open("assets/wordlistengMedie.txt", "r") as f:                                                         # Apertura file con le parole
            for line in f:
                word = line.rstrip("\n")                                                                                
                words.append(word)                                                                                  # Aggiunta delle parole alla lista
            rand_word = random.choice(words)                                                                        # Scelta di una parola a caso dalla lista
            return rand_word
    elif a == "eh":
        with open("assets/wordlistengLunghe.txt", "r") as f:                                                        # Apertura file con le parole
            for line in f:
                word = line.rstrip("\n")                                                                                
                words.append(word)                                                                                  # Aggiunta delle parole alla lista
            rand_word = random.choice(words)                                                                        # Scelta di una parola a caso dalla lista
            return rand_word
    elif a == "ic":
        with open("assets/wordlistitaCorte.txt", "r") as f:                                                         # Apertura file con le parole
            for line in f:
                word = line.rstrip("\n")                                                                                
                words.append(word)                                                                                  # Aggiunta delle parole alla lista
            rand_word = random.choice(words)                                                                        # Scelta di una parola a caso dalla lista
            return rand_word
    elif a == "im":
        with open("assets/wordlistitaMedie.txt", "r") as f:                                                         # Apertura file con le parole
            for line in f:
                word = line.rstrip("\n")                                                                                
                words.append(word)                                                                                  # Aggiunta delle parole alla lista
            rand_word = random.choice(words)                                                                        # Scelta di una parola a caso dalla lista
            return rand_word
    elif a == "ih":
        with open("assets/wordlistitaLunghe.txt", "r") as f:                                                        # Apertura file con le parole
            for line in f:
                word = line.rstrip("\n")                                                                                
                words.append(word)                                                                                  # Aggiunta delle parole alla lista
            rand_word = random.choice(words)                                                                        # Scelta di una parola a caso dalla lista
            return rand_word

def box_letter(letter: chr) -> chr:
    global text_box_num, text_box_space 
    if text_box_num <= 5:
        text = font2.render(letter, True, "black")
        text_rect = text.get_rect(center=((105)+text_box_space, 400))
        SCREEN.blit(text, text_rect)
        text_box_space += 30
    elif text_box_num > 5 and text_box_num <= 10:
        text = font2.render(letter, True, "black")
        text_rect = text.get_rect(center=((105)+text_box_space, 430))
        SCREEN.blit(text, text_rect)
        text_box_space += 30
    elif text_box_num > 10 and text_box_num <= 15:
        text = font2.render(letter, True, "black")
        text_rect = text.get_rect(center=((105)+text_box_space, 460))
        SCREEN.blit(text, text_rect)
        text_box_space += 30

def game_over_eng():
    user_text = ""
    input_rect = pygame.Rect(520, 250, 250, 40)
    name_font = pygame.font.SysFont("Arial", 30, bold=True)
    counter = 0
    while True:
        SCREEN.fill("white")

        mouse_pos = pygame.mouse.get_pos()

        name_text = font.render("INSERT YOUR NAME", True, "black")
        name_rect = name_text.get_rect(center=(640, 100))
        SCREEN.blit(name_text, name_rect)

        pygame.draw.rect(SCREEN, "black", input_rect, 2)
        text_surf = name_font.render(user_text, True, "black")
        text_rect = text_surf.get_rect(center=(input_rect.centerx, input_rect.centery))
        SCREEN.blit(text_surf, text_rect)

        enter_but = Button(image=pygame.image.load("assets/rect2.png"),
                            pos=(850, 270),                                                               
                            text_input="ENTER", font=name_font,
                            base_color="black",
                            hovering_color="red")

        for botton in [enter_but]:
            botton.changeColor(mouse_pos)
            botton.update(SCREEN)

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
        SCREEN.fill("white")

        mouse_pos = pygame.mouse.get_pos()

        name_text = font.render("INSERISCI IL TUO NOME", True, "black")
        name_rect = name_text.get_rect(center=(640, 100))
        SCREEN.blit(name_text, name_rect)

        pygame.draw.rect(SCREEN, "black", input_rect, 2)
        text_surf = name_font.render(user_text, True, "black")
        text_rect = text_surf.get_rect(center=(input_rect.centerx, input_rect.centery))
        SCREEN.blit(text_surf, text_rect)

        enter_but = Button(image=pygame.image.load("assets/rect2.png"),
                            pos=(850, 270),                                                               
                            text_input="INVIO", font=name_font,
                            base_color="black",
                            hovering_color="red")

        for botton in [enter_but]:
            botton.changeColor(mouse_pos)
            botton.update(SCREEN)

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
        SCREEN.fill("black")                                                                                        # Fill the screen with black color

        play_mouse_pos = pygame.mouse.get_pos()                                                                     # Get the mouse position

        play = font.render("SELECT THE DIFFICULTY", True, "orange")                                                 # Difficulty text
        play_rect = play.get_rect(center=(640, 100))                                                                # Center the text
        SCREEN.blit(play, play_rect)                                                                                # Blit the text

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
            button.update(SCREEN)                                                                                   # Update the button

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
        SCREEN.fill("black")

        play_mouse_pos = pygame.mouse.get_pos()

        play = font.render("SELEZIONA LA DIFFICOLTA'", True, "orange")                                              # Difficulty text
        play_rect = play.get_rect(center=(640, 100))                                                                # Center the text
        SCREEN.blit(play, play_rect)                                                                                # Blit the text

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
            button.update(SCREEN)                                                                                   # Update the button

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
    for word in db_text.split():
        prova.append(word)
    while True:
        SCREEN.fill("black")

        stats_mouse_pos = pygame.mouse.get_pos()

        stats_text = font.render("STATS SCREEN", True, "white")
        stats_rect = stats_text.get_rect(center=(640, 80))
        SCREEN.blit(stats_text, stats_rect)

        db_text = font.render("  ".join(prova), True, "white")
        db_rect = db_text.get_rect(center=(370, 250))
        SCREEN.blit(db_text, db_rect)

        stats_back = Button(image=None, pos=(150, 670),                                                              # Bottone per tornare al menu principale
                            text_input="BACK", font=font,
                            base_color="white", 
                            hovering_color="green")

        stats_back.changeColor(stats_mouse_pos)
        stats_back.update(SCREEN)

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
        SCREEN.fill("black")

        stats_mouse_pos = pygame.mouse.get_pos()

        stats_text = font.render("SCHERMO STATISTICHE", True, "white")
        stats_rect = stats_text.get_rect(center=(640, 260))
        SCREEN.blit(stats_text, stats_rect)

        stats_back = Button(image=None, pos=(640, 460),                                                             # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=font,
                            base_color="white", 
                            hovering_color="green")

        stats_back.changeColor(stats_mouse_pos)
        stats_back.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stats_back.checkForInput(stats_mouse_pos):
                    main_menu_ita()
        
        pygame.display.update()

def win_menu_eng()-> None:
    while True:
        SCREEN.fill("black")

        end_mouse_pos = pygame.mouse.get_pos()

        end_text = font.render("YOU WIN!!!",True,"white")
        end_rect = end_text.get_rect(center=(640,260))
        SCREEN.blit(end_text,end_rect)

        end_back = Button(image=None, pos=(640, 460),                                                             # Bottone per tornare al menu principale
                            text_input="BACK", font=font,
                            base_color="white", 
                            hovering_color="yellow")
        
        end_back.changeColor(end_mouse_pos)
        end_back.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_back.checkForInput(end_mouse_pos):
                    main_menu_eng()
        
        pygame.display.update()

def win_menu_ita()-> None:
    while True:
        SCREEN.fill("black")

        end_mouse_pos = pygame.mouse.get_pos()

        end_text = font.render("HAI VINTO!!!",True,"white")
        end_rect = end_text.get_rect(center=(640,260))
        SCREEN.blit(end_text,end_rect)

        end_back = Button(image=None, pos=(640, 460),                                                             # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=font,
                            base_color="white", 
                            hovering_color="yellow")
        
        end_back.changeColor(end_mouse_pos)
        end_back.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_back.checkForInput(end_mouse_pos):
                    main_menu_ita()
        
        pygame.display.update()

def lose_menu_eng()-> None:
    while True:
        SCREEN.fill("black")

        end_mouse_pos = pygame.mouse.get_pos()

        end_text = font.render("GAME OVER",True,"white")
        end_rect = end_text.get_rect(center=(640,260))
        SCREEN.blit(end_text,end_rect)

        end_back = Button(image=None, pos=(640, 460),                                                             # Bottone per tornare al menu principale
                            text_input="BACK", font=font,
                            base_color="white", 
                            hovering_color="red")
        
        end_back.changeColor(end_mouse_pos)
        end_back.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_back.checkForInput(end_mouse_pos):
                    main_menu_eng()
        
        pygame.display.update()

def lose_menu_ita()-> None:
    while True:
        SCREEN.fill("black")

        end_mouse_pos = pygame.mouse.get_pos()

        end_text = font.render("HAI PERSO!!!",True,"white")
        end_rect = end_text.get_rect(center=(640,260))
        SCREEN.blit(end_text,end_rect)

        end_back = Button(image=None, pos=(640, 460),                                                             # Bottone per tornare al menu principale
                            text_input="INDIETRO", font=font,
                            base_color="white", 
                            hovering_color="yellow")
        
        end_back.changeColor(end_mouse_pos)
        end_back.update(SCREEN)

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_back.checkForInput(end_mouse_pos):
                    main_menu_ita()
        
        pygame.display.update()


def placeLetter(letter, rand_word):
    space = 10
    word_space = 0
    while word_space < len(rand_word):
        if letter in word_split[word_space]:
            text_surf = font2.render(letter,True,"black")
            text_rect = text_surf.get_rect()
            text_rect.center = (((50)+space),(150))
            SCREEN.blit(text_surf, text_rect)
        word_space += 1
        space += 50

def easy_game_eng() -> None:
    global word_split
    rand_word = get_word("ee")
    rand_word_len = len(rand_word)
    print(rand_word)
    contprova = 0

    provaA = False
    provaB = False
    provaC = False
    provaD = False
    provaE = False
    provaF = False
    provaG = False
    provaH = False
    provaI = False
    provaJ = False
    provaK = False
    provaL = False
    provaM = False
    provaN = False
    provaO = False
    provaP = False
    provaQ = False
    provaR = False
    provaS = False
    provaT = False
    provaU = False
    provaV = False
    provaW = False
    provaX = False
    provaY = False
    provaZ = False

    nlett = 0
    for i in range(rand_word_len):
        if rand_word[i] not in rand_word[:i]:
            nlett += 1

    guess_lett = ''
    word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]
    
    while True:
        SCREEN.fill("white")

        counter = 0
        space = 10

        while counter < rand_word_len:                                                                              # Ciclo per stampare le lettere nascote della parola
            hidden = font2.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))                                                            # Posizione delle lettere nascoste
            SCREEN.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)                                                       # Rettangolo delle lettere

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:         
                    box_letter("a")
                    if guess_lett in rand_word:
                        provaA = True
                        contprova += 1
                if event.key == pygame.K_b:
                    box_letter("b")
                    if guess_lett in rand_word:
                        provaB = True
                        contprova += 1
                if event.key == pygame.K_c:
                    box_letter("c")
                    if guess_lett in rand_word:
                        provaC = True
                        contprova += 1
                if event.key == pygame.K_d:
                    box_letter("d")
                    if guess_lett in rand_word:
                        provaD = True
                        contprova += 1
                if event.key == pygame.K_e:
                    box_letter("e")
                    if guess_lett in rand_word:
                        provaE = True
                        contprova += 1
                if event.key == pygame.K_f:
                    box_letter("f")
                    if guess_lett in rand_word:
                        provaF = True
                        contprova += 1
                if event.key == pygame.K_g:
                    box_letter("g")
                    if guess_lett in rand_word:
                        provaG = True
                        contprova += 1
                if event.key == pygame.K_h:
                    box_letter("h")
                    if guess_lett in rand_word:
                        provaH = True
                        contprova += 1
                if event.key == pygame.K_i:
                    box_letter("i")
                    if guess_lett in rand_word:
                        provaI = True
                        contprova += 1
                if event.key == pygame.K_j:
                    box_letter("j")
                    if guess_lett in rand_word:
                        provaJ = True
                        contprova += 1
                if event.key == pygame.K_k:
                    box_letter("k")
                    if guess_lett in rand_word:
                        provaK = True
                        contprova += 1
                if event.key == pygame.K_l:
                    box_letter("l")
                    if guess_lett in rand_word:
                        provaL = True
                        contprova += 1
                if event.key == pygame.K_m:
                    box_letter("m")
                    if guess_lett in rand_word:
                        provaM = True
                        contprova += 1
                if event.key == pygame.K_n:
                    box_letter("n")
                    if guess_lett in rand_word:
                        provaN = True
                        contprova += 1
                if event.key == pygame.K_o:
                    box_letter("o")
                    if guess_lett in rand_word:
                        provaO = True
                        contprova += 1
                if event.key == pygame.K_p:
                    box_letter("p")
                    if guess_lett in rand_word:
                        provaP = True
                        contprova += 1
                if event.key == pygame.K_q:
                    box_letter("q")
                    if guess_lett in rand_word:
                        provaQ = True
                        contprova += 1
                if event.key == pygame.K_r:
                    box_letter("r")
                    if guess_lett in rand_word:
                        provaR = True
                        contprova += 1
                if event.key == pygame.K_s:
                    box_letter("s")
                    if guess_lett in rand_word:
                        provaS = True
                        contprova += 1
                if event.key == pygame.K_t:
                    box_letter("t")
                    if guess_lett in rand_word:
                        provaT = True
                        contprova += 1
                if event.key == pygame.K_u:
                    box_letter("u")
                    if guess_lett in rand_word:
                        provaU = True
                        contprova += 1
                if event.key == pygame.K_v:
                    box_letter("v")
                    if guess_lett in rand_word:
                        provaV = True
                        contprova += 1
                if event.key == pygame.K_w:
                    box_letter("w")
                    if guess_lett in rand_word:
                        provaW = True
                        contprova += 1
                if event.key == pygame.K_x:
                    box_letter("x")
                    if guess_lett in rand_word:
                        provaX = True
                        contprova += 1
                if event.key == pygame.K_y:
                    box_letter("y")
                    if guess_lett in rand_word:
                        provaY = True
                        contprova += 1
                if event.key == pygame.K_z:
                    box_letter("z")
                    if guess_lett in rand_word:
                        provaZ = True
                        contprova += 1

        if contprova == nlett:
            print(contprova)
            play_menu_eng()
        

        if provaA:
            placeLetter("a", rand_word)
        if provaB:
            placeLetter("b", rand_word)
        if provaC:
            placeLetter("c", rand_word)
        if provaD:
            placeLetter("d", rand_word)
        if provaE:
            placeLetter("e", rand_word)
        if provaF:
            placeLetter("f", rand_word)
        if provaG:
            placeLetter("g", rand_word)
        if provaH:
            placeLetter("h", rand_word)
        if provaI:
            placeLetter("i", rand_word)
        if provaJ:
            placeLetter("j", rand_word)
        if provaK:
            placeLetter("k", rand_word)
        if provaL:
            placeLetter("l", rand_word)
        if provaM:
            placeLetter("m", rand_word)
        if provaN:
            placeLetter("n", rand_word)
        if provaO:
            placeLetter("o", rand_word)
        if provaP:
            placeLetter("p", rand_word)
        if provaQ:
            placeLetter("q", rand_word)
        if provaR:
            placeLetter("r", rand_word)
        if provaS:
            placeLetter("s", rand_word)
        if provaT:
            placeLetter("t", rand_word)
        if provaU:
            placeLetter("u", rand_word)
        if provaV:
            placeLetter("v", rand_word)
        if provaW:
            placeLetter("w", rand_word)
        if provaX:
            placeLetter("x", rand_word)
        if provaY:
            placeLetter("y", rand_word)
        if provaZ:
            placeLetter("z", rand_word)
                               
        pygame.display.update()

def med_game_eng() -> None:
    global word_split
    rand_word = get_word("em")
    rand_word_len = len(rand_word)
    print(rand_word)


    provaA = False
    provaB = False
    provaC = False
    provaD = False
    provaE = False
    provaF = False
    provaG = False
    provaH = False
    provaI = False
    provaJ = False
    provaK = False
    provaL = False
    provaM = False
    provaN = False
    provaO = False
    provaP = False
    provaQ = False
    provaR = False
    provaS = False
    provaT = False
    provaU = False
    provaV = False
    provaW = False
    provaX = False
    provaY = False
    provaZ = False



    guess_lett = ''
    word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]
    
    while True:
        SCREEN.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:                                                                              # Ciclo per stampare le lettere nascote della parola
            hidden = font2.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))                                                            # Posizione delle lettere nascoste
            SCREEN.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)                                                       # Rettangolo delle lettere

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:         
                    box_letter("a")
                    if guess_lett in rand_word:
                        provaA = True
                if event.key == pygame.K_b:
                    box_letter("b")
                    if guess_lett in rand_word:
                        provaB = True
                if event.key == pygame.K_c:
                    box_letter("c")
                    if guess_lett in rand_word:
                        provaC = True
                if event.key == pygame.K_d:
                    box_letter("d")
                    if guess_lett in rand_word:
                        provaD = True
                if event.key == pygame.K_e:
                    box_letter("e")
                    if guess_lett in rand_word:
                        provaE = True
                if event.key == pygame.K_f:
                    box_letter("f")
                    if guess_lett in rand_word:
                        provaF = True
                if event.key == pygame.K_g:
                    box_letter("g")
                    if guess_lett in rand_word:
                        provaG = True
                if event.key == pygame.K_h:
                    box_letter("h")
                    if guess_lett in rand_word:
                        provaH = True
                if event.key == pygame.K_i:
                    box_letter("i")
                    if guess_lett in rand_word:
                        provaI = True
                if event.key == pygame.K_j:
                    box_letter("j")
                    if guess_lett in rand_word:
                        provaJ = True
                if event.key == pygame.K_k:
                    box_letter("k")
                    if guess_lett in rand_word:
                        provaK = True
                if event.key == pygame.K_l:
                    box_letter("l")
                    if guess_lett in rand_word:
                        provaL = True
                if event.key == pygame.K_m:
                    box_letter("m")
                    if guess_lett in rand_word:
                        provaM = True
                if event.key == pygame.K_n:
                    box_letter("n")
                    if guess_lett in rand_word:
                        provaN = True
                if event.key == pygame.K_o:
                    box_letter("o")
                    if guess_lett in rand_word:
                        provaO = True
                if event.key == pygame.K_p:
                    box_letter("p")
                    if guess_lett in rand_word:
                        provaP = True
                if event.key == pygame.K_q:
                    box_letter("q")
                    if guess_lett in rand_word:
                        provaQ = True
                if event.key == pygame.K_r:
                    box_letter("r")
                    if guess_lett in rand_word:
                        provaR = True
                if event.key == pygame.K_s:
                    box_letter("s")
                    if guess_lett in rand_word:
                        provaS = True
                if event.key == pygame.K_t:
                    box_letter("t")
                    if guess_lett in rand_word:
                        provaT = True
                if event.key == pygame.K_u:
                    box_letter("u")
                    if guess_lett in rand_word:
                        provaU = True
                if event.key == pygame.K_v:
                    box_letter("v")
                    if guess_lett in rand_word:
                        provaV = True
                if event.key == pygame.K_w:
                    box_letter("w")
                    if guess_lett in rand_word:
                        provaW = True
                if event.key == pygame.K_x:
                    box_letter("x")
                    if guess_lett in rand_word:
                        provaX = True
                if event.key == pygame.K_y:
                    box_letter("y")
                    if guess_lett in rand_word:
                        provaY = True
                if event.key == pygame.K_z:
                    box_letter("z")
                    if guess_lett in rand_word:
                        provaZ = True
        if provaA:
            placeLetter("a", rand_word)
        if provaB:
            placeLetter("b", rand_word)
        if provaC:
            placeLetter("c", rand_word)
        if provaD:
            placeLetter("d", rand_word)
        if provaE:
            placeLetter("e", rand_word)
        if provaF:
            placeLetter("f", rand_word)
        if provaG:
            placeLetter("g", rand_word)
        if provaH:
            placeLetter("h", rand_word)
        if provaI:
            placeLetter("i", rand_word)
        if provaJ:
            placeLetter("j", rand_word)
        if provaK:
            placeLetter("k", rand_word)
        if provaL:
            placeLetter("l", rand_word)
        if provaM:
            placeLetter("m", rand_word)
        if provaN:
            placeLetter("n", rand_word)
        if provaO:
            placeLetter("o", rand_word)
        if provaP:
            placeLetter("p", rand_word)
        if provaQ:
            placeLetter("q", rand_word)
        if provaR:
            placeLetter("r", rand_word)
        if provaS:
            placeLetter("s", rand_word)
        if provaT:
            placeLetter("t", rand_word)
        if provaU:
            placeLetter("u", rand_word)
        if provaV:
            placeLetter("v", rand_word)
        if provaW:
            placeLetter("w", rand_word)
        if provaX:
            placeLetter("x", rand_word)
        if provaY:
            placeLetter("y", rand_word)
        if provaZ:
            placeLetter("z", rand_word)
                               
        pygame.display.update()

def hard_game_eng() -> None:
    global word_split
    rand_word = get_word("eh")
    rand_word_len = len(rand_word)
    print(rand_word)


    provaA = False
    provaB = False
    provaC = False
    provaD = False
    provaE = False
    provaF = False
    provaG = False
    provaH = False
    provaI = False
    provaJ = False
    provaK = False
    provaL = False
    provaM = False
    provaN = False
    provaO = False
    provaP = False
    provaQ = False
    provaR = False
    provaS = False
    provaT = False
    provaU = False
    provaV = False
    provaW = False
    provaX = False
    provaY = False
    provaZ = False



    guess_lett = ''
    word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]
    
    while True:
        SCREEN.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:                                                                              # Ciclo per stampare le lettere nascote della parola
            hidden = font2.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))                                                            # Posizione delle lettere nascoste
            SCREEN.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)                                                       # Rettangolo delle lettere

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:         
                    box_letter("a")
                    if guess_lett in rand_word:
                        provaA = True
                if event.key == pygame.K_b:
                    box_letter("b")
                    if guess_lett in rand_word:
                        provaB = True
                if event.key == pygame.K_c:
                    box_letter("c")
                    if guess_lett in rand_word:
                        provaC = True
                if event.key == pygame.K_d:
                    box_letter("d")
                    if guess_lett in rand_word:
                        provaD = True
                if event.key == pygame.K_e:
                    box_letter("e")
                    if guess_lett in rand_word:
                        provaE = True
                if event.key == pygame.K_f:
                    box_letter("f")
                    if guess_lett in rand_word:
                        provaF = True
                if event.key == pygame.K_g:
                    box_letter("g")
                    if guess_lett in rand_word:
                        provaG = True
                if event.key == pygame.K_h:
                    box_letter("h")
                    if guess_lett in rand_word:
                        provaH = True
                if event.key == pygame.K_i:
                    box_letter("i")
                    if guess_lett in rand_word:
                        provaI = True
                if event.key == pygame.K_j:
                    box_letter("j")
                    if guess_lett in rand_word:
                        provaJ = True
                if event.key == pygame.K_k:
                    box_letter("k")
                    if guess_lett in rand_word:
                        provaK = True
                if event.key == pygame.K_l:
                    box_letter("l")
                    if guess_lett in rand_word:
                        provaL = True
                if event.key == pygame.K_m:
                    box_letter("m")
                    if guess_lett in rand_word:
                        provaM = True
                if event.key == pygame.K_n:
                    box_letter("n")
                    if guess_lett in rand_word:
                        provaN = True
                if event.key == pygame.K_o:
                    box_letter("o")
                    if guess_lett in rand_word:
                        provaO = True
                if event.key == pygame.K_p:
                    box_letter("p")
                    if guess_lett in rand_word:
                        provaP = True
                if event.key == pygame.K_q:
                    box_letter("q")
                    if guess_lett in rand_word:
                        provaQ = True
                if event.key == pygame.K_r:
                    box_letter("r")
                    if guess_lett in rand_word:
                        provaR = True
                if event.key == pygame.K_s:
                    box_letter("s")
                    if guess_lett in rand_word:
                        provaS = True
                if event.key == pygame.K_t:
                    box_letter("t")
                    if guess_lett in rand_word:
                        provaT = True
                if event.key == pygame.K_u:
                    box_letter("u")
                    if guess_lett in rand_word:
                        provaU = True
                if event.key == pygame.K_v:
                    box_letter("v")
                    if guess_lett in rand_word:
                        provaV = True
                if event.key == pygame.K_w:
                    box_letter("w")
                    if guess_lett in rand_word:
                        provaW = True
                if event.key == pygame.K_x:
                    box_letter("x")
                    if guess_lett in rand_word:
                        provaX = True
                if event.key == pygame.K_y:
                    box_letter("y")
                    if guess_lett in rand_word:
                        provaY = True
                if event.key == pygame.K_z:
                    box_letter("z")
                    if guess_lett in rand_word:
                        provaZ = True
        if provaA:
            placeLetter("a", rand_word)
        if provaB:
            placeLetter("b", rand_word)
        if provaC:
            placeLetter("c", rand_word)
        if provaD:
            placeLetter("d", rand_word)
        if provaE:
            placeLetter("e", rand_word)
        if provaF:
            placeLetter("f", rand_word)
        if provaG:
            placeLetter("g", rand_word)
        if provaH:
            placeLetter("h", rand_word)
        if provaI:
            placeLetter("i", rand_word)
        if provaJ:
            placeLetter("j", rand_word)
        if provaK:
            placeLetter("k", rand_word)
        if provaL:
            placeLetter("l", rand_word)
        if provaM:
            placeLetter("m", rand_word)
        if provaN:
            placeLetter("n", rand_word)
        if provaO:
            placeLetter("o", rand_word)
        if provaP:
            placeLetter("p", rand_word)
        if provaQ:
            placeLetter("q", rand_word)
        if provaR:
            placeLetter("r", rand_word)
        if provaS:
            placeLetter("s", rand_word)
        if provaT:
            placeLetter("t", rand_word)
        if provaU:
            placeLetter("u", rand_word)
        if provaV:
            placeLetter("v", rand_word)
        if provaW:
            placeLetter("w", rand_word)
        if provaX:
            placeLetter("x", rand_word)
        if provaY:
            placeLetter("y", rand_word)
        if provaZ:
            placeLetter("z", rand_word)
                               
        pygame.display.update()


def easy_game_ita() -> None:
    global word_split
    rand_word = get_word("ie")
    rand_word_len = len(rand_word)
    print(rand_word)


    provaA = False
    provaB = False
    provaC = False
    provaD = False
    provaE = False
    provaF = False
    provaG = False
    provaH = False
    provaI = False
    provaJ = False
    provaK = False
    provaL = False
    provaM = False
    provaN = False
    provaO = False
    provaP = False
    provaQ = False
    provaR = False
    provaS = False
    provaT = False
    provaU = False
    provaV = False
    provaW = False
    provaX = False
    provaY = False
    provaZ = False



    guess_lett = ''
    word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]
    
    while True:
        SCREEN.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:                                                                              # Ciclo per stampare le lettere nascote della parola
            hidden = font2.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))                                                            # Posizione delle lettere nascoste
            SCREEN.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)                                                       # Rettangolo delle lettere

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:         
                    box_letter("a")
                    if guess_lett in rand_word:
                        provaA = True
                if event.key == pygame.K_b:
                    box_letter("b")
                    if guess_lett in rand_word:
                        provaB = True
                if event.key == pygame.K_c:
                    box_letter("c")
                    if guess_lett in rand_word:
                        provaC = True
                if event.key == pygame.K_d:
                    box_letter("d")
                    if guess_lett in rand_word:
                        provaD = True
                if event.key == pygame.K_e:
                    box_letter("e")
                    if guess_lett in rand_word:
                        provaE = True
                if event.key == pygame.K_f:
                    box_letter("f")
                    if guess_lett in rand_word:
                        provaF = True
                if event.key == pygame.K_g:
                    box_letter("g")
                    if guess_lett in rand_word:
                        provaG = True
                if event.key == pygame.K_h:
                    box_letter("h")
                    if guess_lett in rand_word:
                        provaH = True
                if event.key == pygame.K_i:
                    box_letter("i")
                    if guess_lett in rand_word:
                        provaI = True
                if event.key == pygame.K_j:
                    box_letter("j")
                    if guess_lett in rand_word:
                        provaJ = True
                if event.key == pygame.K_k:
                    box_letter("k")
                    if guess_lett in rand_word:
                        provaK = True
                if event.key == pygame.K_l:
                    box_letter("l")
                    if guess_lett in rand_word:
                        provaL = True
                if event.key == pygame.K_m:
                    box_letter("m")
                    if guess_lett in rand_word:
                        provaM = True
                if event.key == pygame.K_n:
                    box_letter("n")
                    if guess_lett in rand_word:
                        provaN = True
                if event.key == pygame.K_o:
                    box_letter("o")
                    if guess_lett in rand_word:
                        provaO = True
                if event.key == pygame.K_p:
                    box_letter("p")
                    if guess_lett in rand_word:
                        provaP = True
                if event.key == pygame.K_q:
                    box_letter("q")
                    if guess_lett in rand_word:
                        provaQ = True
                if event.key == pygame.K_r:
                    box_letter("r")
                    if guess_lett in rand_word:
                        provaR = True
                if event.key == pygame.K_s:
                    box_letter("s")
                    if guess_lett in rand_word:
                        provaS = True
                if event.key == pygame.K_t:
                    box_letter("t")
                    if guess_lett in rand_word:
                        provaT = True
                if event.key == pygame.K_u:
                    box_letter("u")
                    if guess_lett in rand_word:
                        provaU = True
                if event.key == pygame.K_v:
                    box_letter("v")
                    if guess_lett in rand_word:
                        provaV = True
                if event.key == pygame.K_w:
                    box_letter("w")
                    if guess_lett in rand_word:
                        provaW = True
                if event.key == pygame.K_x:
                    box_letter("x")
                    if guess_lett in rand_word:
                        provaX = True
                if event.key == pygame.K_y:
                    box_letter("y")
                    if guess_lett in rand_word:
                        provaY = True
                if event.key == pygame.K_z:
                    box_letter("z")
                    if guess_lett in rand_word:
                        provaZ = True
        if provaA:
            placeLetter("a", rand_word)
        if provaB:
            placeLetter("b", rand_word)
        if provaC:
            placeLetter("c", rand_word)
        if provaD:
            placeLetter("d", rand_word)
        if provaE:
            placeLetter("e", rand_word)
        if provaF:
            placeLetter("f", rand_word)
        if provaG:
            placeLetter("g", rand_word)
        if provaH:
            placeLetter("h", rand_word)
        if provaI:
            placeLetter("i", rand_word)
        if provaJ:
            placeLetter("j", rand_word)
        if provaK:
            placeLetter("k", rand_word)
        if provaL:
            placeLetter("l", rand_word)
        if provaM:
            placeLetter("m", rand_word)
        if provaN:
            placeLetter("n", rand_word)
        if provaO:
            placeLetter("o", rand_word)
        if provaP:
            placeLetter("p", rand_word)
        if provaQ:
            placeLetter("q", rand_word)
        if provaR:
            placeLetter("r", rand_word)
        if provaS:
            placeLetter("s", rand_word)
        if provaT:
            placeLetter("t", rand_word)
        if provaU:
            placeLetter("u", rand_word)
        if provaV:
            placeLetter("v", rand_word)
        if provaW:
            placeLetter("w", rand_word)
        if provaX:
            placeLetter("x", rand_word)
        if provaY:
            placeLetter("y", rand_word)
        if provaZ:
            placeLetter("z", rand_word)
                               
        pygame.display.update()

def med_game_ita() -> None:
    global word_split
    rand_word = get_word("im")
    rand_word_len = len(rand_word)
    print(rand_word)


    provaA = False
    provaB = False
    provaC = False
    provaD = False
    provaE = False
    provaF = False
    provaG = False
    provaH = False
    provaI = False
    provaJ = False
    provaK = False
    provaL = False
    provaM = False
    provaN = False
    provaO = False
    provaP = False
    provaQ = False
    provaR = False
    provaS = False
    provaT = False
    provaU = False
    provaV = False
    provaW = False
    provaX = False
    provaY = False
    provaZ = False



    guess_lett = ''
    word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]
    
    while True:
        SCREEN.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:                                                                              # Ciclo per stampare le lettere nascote della parola
            hidden = font2.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))                                                            # Posizione delle lettere nascoste
            SCREEN.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)                                                       # Rettangolo delle lettere

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:         
                    box_letter("a")
                    if guess_lett in rand_word:
                        provaA = True
                if event.key == pygame.K_b:
                    box_letter("b")
                    if guess_lett in rand_word:
                        provaB = True
                if event.key == pygame.K_c:
                    box_letter("c")
                    if guess_lett in rand_word:
                        provaC = True
                if event.key == pygame.K_d:
                    box_letter("d")
                    if guess_lett in rand_word:
                        provaD = True
                if event.key == pygame.K_e:
                    box_letter("e")
                    if guess_lett in rand_word:
                        provaE = True
                if event.key == pygame.K_f:
                    box_letter("f")
                    if guess_lett in rand_word:
                        provaF = True
                if event.key == pygame.K_g:
                    box_letter("g")
                    if guess_lett in rand_word:
                        provaG = True
                if event.key == pygame.K_h:
                    box_letter("h")
                    if guess_lett in rand_word:
                        provaH = True
                if event.key == pygame.K_i:
                    box_letter("i")
                    if guess_lett in rand_word:
                        provaI = True
                if event.key == pygame.K_j:
                    box_letter("j")
                    if guess_lett in rand_word:
                        provaJ = True
                if event.key == pygame.K_k:
                    box_letter("k")
                    if guess_lett in rand_word:
                        provaK = True
                if event.key == pygame.K_l:
                    box_letter("l")
                    if guess_lett in rand_word:
                        provaL = True
                if event.key == pygame.K_m:
                    box_letter("m")
                    if guess_lett in rand_word:
                        provaM = True
                if event.key == pygame.K_n:
                    box_letter("n")
                    if guess_lett in rand_word:
                        provaN = True
                if event.key == pygame.K_o:
                    box_letter("o")
                    if guess_lett in rand_word:
                        provaO = True
                if event.key == pygame.K_p:
                    box_letter("p")
                    if guess_lett in rand_word:
                        provaP = True
                if event.key == pygame.K_q:
                    box_letter("q")
                    if guess_lett in rand_word:
                        provaQ = True
                if event.key == pygame.K_r:
                    box_letter("r")
                    if guess_lett in rand_word:
                        provaR = True
                if event.key == pygame.K_s:
                    box_letter("s")
                    if guess_lett in rand_word:
                        provaS = True
                if event.key == pygame.K_t:
                    box_letter("t")
                    if guess_lett in rand_word:
                        provaT = True
                if event.key == pygame.K_u:
                    box_letter("u")
                    if guess_lett in rand_word:
                        provaU = True
                if event.key == pygame.K_v:
                    box_letter("v")
                    if guess_lett in rand_word:
                        provaV = True
                if event.key == pygame.K_w:
                    box_letter("w")
                    if guess_lett in rand_word:
                        provaW = True
                if event.key == pygame.K_x:
                    box_letter("x")
                    if guess_lett in rand_word:
                        provaX = True
                if event.key == pygame.K_y:
                    box_letter("y")
                    if guess_lett in rand_word:
                        provaY = True
                if event.key == pygame.K_z:
                    box_letter("z")
                    if guess_lett in rand_word:
                        provaZ = True
        if provaA:
            placeLetter("a", rand_word)
        if provaB:
            placeLetter("b", rand_word)
        if provaC:
            placeLetter("c", rand_word)
        if provaD:
            placeLetter("d", rand_word)
        if provaE:
            placeLetter("e", rand_word)
        if provaF:
            placeLetter("f", rand_word)
        if provaG:
            placeLetter("g", rand_word)
        if provaH:
            placeLetter("h", rand_word)
        if provaI:
            placeLetter("i", rand_word)
        if provaJ:
            placeLetter("j", rand_word)
        if provaK:
            placeLetter("k", rand_word)
        if provaL:
            placeLetter("l", rand_word)
        if provaM:
            placeLetter("m", rand_word)
        if provaN:
            placeLetter("n", rand_word)
        if provaO:
            placeLetter("o", rand_word)
        if provaP:
            placeLetter("p", rand_word)
        if provaQ:
            placeLetter("q", rand_word)
        if provaR:
            placeLetter("r", rand_word)
        if provaS:
            placeLetter("s", rand_word)
        if provaT:
            placeLetter("t", rand_word)
        if provaU:
            placeLetter("u", rand_word)
        if provaV:
            placeLetter("v", rand_word)
        if provaW:
            placeLetter("w", rand_word)
        if provaX:
            placeLetter("x", rand_word)
        if provaY:
            placeLetter("y", rand_word)
        if provaZ:
            placeLetter("z", rand_word)
                               
        pygame.display.update()


def hard_game_ita() -> None:
    global word_split
    rand_word = get_word("ih")
    rand_word_len = len(rand_word)
    print(rand_word)


    provaA = False
    provaB = False
    provaC = False
    provaD = False
    provaE = False
    provaF = False
    provaG = False
    provaH = False
    provaI = False
    provaJ = False
    provaK = False
    provaL = False
    provaM = False
    provaN = False
    provaO = False
    provaP = False
    provaQ = False
    provaR = False
    provaS = False
    provaT = False
    provaU = False
    provaV = False
    provaW = False
    provaX = False
    provaY = False
    provaZ = False



    guess_lett = ''
    word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]
    
    while True:
        SCREEN.fill("white")

        game_mouse_pos = pygame.mouse.get_pos()

        counter = 0
        space = 10

        while counter < rand_word_len:                                                                              # Ciclo per stampare le lettere nascote della parola
            hidden = font2.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))                                                            # Posizione delle lettere nascoste
            SCREEN.blit(hidden, hidden_rect)
            space += 50
            counter += 1

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)                                                       # Rettangolo delle lettere

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:         
                    box_letter("a")
                    if guess_lett in rand_word:
                        provaA = True
                if event.key == pygame.K_b:
                    box_letter("b")
                    if guess_lett in rand_word:
                        provaB = True
                if event.key == pygame.K_c:
                    box_letter("c")
                    if guess_lett in rand_word:
                        provaC = True
                if event.key == pygame.K_d:
                    box_letter("d")
                    if guess_lett in rand_word:
                        provaD = True
                if event.key == pygame.K_e:
                    box_letter("e")
                    if guess_lett in rand_word:
                        provaE = True
                if event.key == pygame.K_f:
                    box_letter("f")
                    if guess_lett in rand_word:
                        provaF = True
                if event.key == pygame.K_g:
                    box_letter("g")
                    if guess_lett in rand_word:
                        provaG = True
                if event.key == pygame.K_h:
                    box_letter("h")
                    if guess_lett in rand_word:
                        provaH = True
                if event.key == pygame.K_i:
                    box_letter("i")
                    if guess_lett in rand_word:
                        provaI = True
                if event.key == pygame.K_j:
                    box_letter("j")
                    if guess_lett in rand_word:
                        provaJ = True
                if event.key == pygame.K_k:
                    box_letter("k")
                    if guess_lett in rand_word:
                        provaK = True
                if event.key == pygame.K_l:
                    box_letter("l")
                    if guess_lett in rand_word:
                        provaL = True
                if event.key == pygame.K_m:
                    box_letter("m")
                    if guess_lett in rand_word:
                        provaM = True
                if event.key == pygame.K_n:
                    box_letter("n")
                    if guess_lett in rand_word:
                        provaN = True
                if event.key == pygame.K_o:
                    box_letter("o")
                    if guess_lett in rand_word:
                        provaO = True
                if event.key == pygame.K_p:
                    box_letter("p")
                    if guess_lett in rand_word:
                        provaP = True
                if event.key == pygame.K_q:
                    box_letter("q")
                    if guess_lett in rand_word:
                        provaQ = True
                if event.key == pygame.K_r:
                    box_letter("r")
                    if guess_lett in rand_word:
                        provaR = True
                if event.key == pygame.K_s:
                    box_letter("s")
                    if guess_lett in rand_word:
                        provaS = True
                if event.key == pygame.K_t:
                    box_letter("t")
                    if guess_lett in rand_word:
                        provaT = True
                if event.key == pygame.K_u:
                    box_letter("u")
                    if guess_lett in rand_word:
                        provaU = True
                if event.key == pygame.K_v:
                    box_letter("v")
                    if guess_lett in rand_word:
                        provaV = True
                if event.key == pygame.K_w:
                    box_letter("w")
                    if guess_lett in rand_word:
                        provaW = True
                if event.key == pygame.K_x:
                    box_letter("x")
                    if guess_lett in rand_word:
                        provaX = True
                if event.key == pygame.K_y:
                    box_letter("y")
                    if guess_lett in rand_word:
                        provaY = True
                if event.key == pygame.K_z:
                    box_letter("z")
                    if guess_lett in rand_word:
                        provaZ = True
        if provaA:
            placeLetter("a", rand_word)
        if provaB:
            placeLetter("b", rand_word)
        if provaC:
            placeLetter("c", rand_word)
        if provaD:
            placeLetter("d", rand_word)
        if provaE:
            placeLetter("e", rand_word)
        if provaF:
            placeLetter("f", rand_word)
        if provaG:
            placeLetter("g", rand_word)
        if provaH:
            placeLetter("h", rand_word)
        if provaI:
            placeLetter("i", rand_word)
        if provaJ:
            placeLetter("j", rand_word)
        if provaK:
            placeLetter("k", rand_word)
        if provaL:
            placeLetter("l", rand_word)
        if provaM:
            placeLetter("m", rand_word)
        if provaN:
            placeLetter("n", rand_word)
        if provaO:
            placeLetter("o", rand_word)
        if provaP:
            placeLetter("p", rand_word)
        if provaQ:
            placeLetter("q", rand_word)
        if provaR:
            placeLetter("r", rand_word)
        if provaS:
            placeLetter("s", rand_word)
        if provaT:
            placeLetter("t", rand_word)
        if provaU:
            placeLetter("u", rand_word)
        if provaV:
            placeLetter("v", rand_word)
        if provaW:
            placeLetter("w", rand_word)
        if provaX:
            placeLetter("x", rand_word)
        if provaY:
            placeLetter("y", rand_word)
        if provaZ:
            placeLetter("z", rand_word)
                               
        pygame.display.update()


def main_menu_eng() -> None:                                                                                        # Funzione per il Menu Principale
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))                                                                             # Imposta il background

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
            button.update(SCREEN)                                                                                   # Aggiorna il bottone

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:                                                                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if quit_but.checkForInput(mouse_pos):               
                    pygame.quit()
                    sys.exit()                                                                                      # Se si preme il bottone QUIT chiude la finestra
                if stats_but.checkForInput(mouse_pos):
                    stats_menu_eng()                                                                                # Se si preme il bottone STATS apre il menu delle statistiche
                if play_but.checkForInput(mouse_pos):   
                    play_menu_eng()                                                                                 # Se si preme il bottone PLAY apre il menu di gioco
                if ita_but.checkForInput(mouse_pos):
                    main_menu_ita()

        pygame.display.update()                                                                                     # Aggiorna lo schermo

def main_menu_ita() -> None:                                                                                        # Funzione per il Menu Principale
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))                                                                             # Imposta il background

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
            button.update(SCREEN)                                                                                   # Aggiorna il bottone

        for event in pygame.event.get():                                                                            # Eventi
            if event.type == pygame.QUIT:                                                                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if quit_but.checkForInput(mouse_pos):                                                               # If the quit button is pressed 
                    pygame.quit()                                                                                   # Close the window
                    sys.exit()                                                                                      
                if stats_but.checkForInput(mouse_pos):                                                              # If the stats button is pressed
                    stats_menu_ita()                                                                                # Open the stats menu                                                                                   # Se si preme il bottone PLAY apre il menu di gioco
                if eng_but.checkForInput(mouse_pos):
                    main_menu_eng()
                if play_but.checkForInput(mouse_pos):
                    play_menu_ita()                                                                                 # Se si preme il bottone PLAY apre il menu di gioco

        pygame.display.update()                                                                                     # Aggiorna lo schermo

if __name__ == "__main__":  
    main_menu_eng()
    #lose_menu_eng()
    