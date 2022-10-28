import pygame, sys
from button import Button
from mode import *
from dbase import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hangman Game") 

BACKGROUND = pygame.image.load("assets/img.png")
FONT = pygame.font.SysFont("Arial", 80, bold=True)
FONT2 = pygame.font.SysFont("Arial", 60, bold=True)

### TEST DB ###
#test = "prova2"
#score = 0
#Dbase(dbase="hangman.db").insert(test, score)
#a = Dbase(dbase="hangman.db").view()
#print(a)
###############

### English Main Menu ###
def main_menu_eng() -> None:
    global lang, diff
    diff = 0
    lang = "eng"
    while True:

        SCREEN.blit(BACKGROUND, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        quick_but = Button(image=pygame.image.load("assets/rect1.png"),
                    pos=(950, 80), text_input="QUICK GAME", font=FONT,
                    base_color="black", hovering_color="red")

        play_but = Button(image=pygame.image.load("assets/rect2.png"),
                    pos=(950, 190), text_input="PLAY", font=FONT,
                    base_color="black", hovering_color="red")

        stats_but = Button(image=pygame.image.load("assets/rect.png"),
                    pos=(950, 300), text_input="STATS", font=FONT,
                    base_color="black", hovering_color="red")

        quit_but = Button(image=pygame.image.load("assets/rect2.png"),
                    pos=(950, 410), text_input="QUIT", font=FONT,
                    base_color="black", hovering_color="red")

        ita_but = Button(image=pygame.image.load("assets/ita.png"),
                    pos=(40, 40), text_input="", font=FONT,
                    base_color="black", hovering_color="red")

        for button in [play_but, stats_but, quit_but, ita_but, quick_but]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_but.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if play_but.checkForInput(mouse_pos):
                    play_menu_eng()
                if stats_but.checkForInput(mouse_pos):
                    stats_menu_eng()
                if ita_but.checkForInput(mouse_pos):
                    main_menu_ita()
                if quick_but.checkForInput(mouse_pos):
                    word = fast_eng()
                    game(word)

        pygame.display.update()

### Italian Main Menu ###
def main_menu_ita() -> None:
    global lang, diff
    diff = 0
    lang = "ita"
    while True:

        SCREEN.blit(BACKGROUND, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        quick_but = Button(image=pygame.image.load("assets/rect1.png"),
                    pos=(930, 80), text_input="PARTITA RAPIDA", font=FONT,
                    base_color="black", hovering_color="red")

        play_but = Button(image=pygame.image.load("assets/rect2.png"),
                    pos=(930, 190), text_input="GIOCA", font=FONT,
                    base_color="black", hovering_color="red")

        stats_but = Button(image=pygame.image.load("assets/rect1.png"),
                    pos=(930, 300), text_input="STATISTICHE", font=FONT,
                    base_color="black", hovering_color="red")

        quit_but = Button(image=pygame.image.load("assets/rect2.png"),
                    pos=(930, 410), text_input="ESCI", font=FONT,
                    base_color="black", hovering_color="red")

        eng_but = Button(image=pygame.image.load("assets/eng.png"),
                    pos=(40, 40), text_input="", font=FONT,
                    base_color="black", hovering_color="red")

        for button in [play_but, stats_but, quit_but, eng_but, quick_but]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_but.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if play_but.checkForInput(mouse_pos):
                    play_menu_ita()
                if stats_but.checkForInput(mouse_pos):
                    stats_menu_ita()
                if eng_but.checkForInput(mouse_pos):
                    main_menu_eng()
                if quick_but.checkForInput(mouse_pos):
                    word = fast_ita()
                    game(word)

        pygame.display.update()

### Difficulty Select Menu ENG ###
def play_menu_eng() -> None:
    global lang, diff
    diff = 0
    lang = "eng"
    while True:
        
        SCREEN.fill("black")

        play_mouse_pos = pygame.mouse.get_pos()

        play = FONT.render("SELECT THE DIFFICULTY", True, "orange")
        play_rect = play.get_rect(center=(640, 100))
        SCREEN.blit(play, play_rect)

        easy_but = Button(image=None, pos=(640, 250),
                            text_input="EASY", font=FONT,
                            base_color="white",
                            hovering_color="red")
        medium_but = Button(image=None, pos=(640,360),
                            text_input="MEDIUM", font=FONT,
                            base_color="white",
                            hovering_color="red")
        hard_but = Button(image=None, pos=(640, 470),
                            text_input="HARD", font=FONT,
                            base_color="white",
                            hovering_color="red")

        play_back = Button(image=None, pos=(140, 650),
                            text_input="BACK", font=FONT, 
                            base_color="white", 
                            hovering_color="green")

        for button in [easy_but, medium_but, hard_but, play_back]:
            button.changeColor(play_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu_eng()
                if easy_but.checkForInput(play_mouse_pos):
                    diff = 1
                    word = get_word_easy_eng()
                    game(word)
                if medium_but.checkForInput(play_mouse_pos):
                    diff = 2
                    word = get_word_med_eng()
                    game(word)
                if hard_but.checkForInput(play_mouse_pos):
                    diff = 3
                    word = get_word_hard_eng()
                    game(word)

        pygame.display.update()

### Difficulty Select Menu ITA ###
def play_menu_ita() -> None:
    global lang, diff
    diff = 0
    lang = "ita"
    while True:
        SCREEN.fill("black")

        play_mouse_pos = pygame.mouse.get_pos()

        play = FONT.render("SELEZIONA LA DIFFICOLTA'", True, "orange")
        play_rect = play.get_rect(center=(640, 100))
        SCREEN.blit(play, play_rect)

        easy_but = Button(image=None, pos=(640, 250),
                            text_input="FACILE", font=FONT,
                            base_color="white",
                            hovering_color="red")
        medium_but = Button(image=None, pos=(640,360),
                            text_input="MEDIO", font=FONT,
                            base_color="white",
                            hovering_color="red")
        hard_but = Button(image=None, pos=(640, 470),
                            text_input="DIFFICILE", font=FONT,
                            base_color="white",
                            hovering_color="red")

        play_back = Button(image=None, pos=(230, 650),
                            text_input="INDIETRO", font=FONT, 
                            base_color="white", 
                            hovering_color="green")

        for button in [easy_but, medium_but, hard_but, play_back]:
            button.changeColor(play_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu_ita()
                if easy_but.checkForInput(play_mouse_pos):
                    diff = 1
                    word = get_word_easy_ita()
                    game(word)
                if medium_but.checkForInput(play_mouse_pos):
                    diff = 2
                    word = get_word_med_ita()
                    game(word)
                if hard_but.checkForInput(play_mouse_pos):
                    diff = 3
                    word = get_word_hard_ita()
                    game(word)

        pygame.display.update()

### Stats Menu ENG
def stats_menu_eng() -> None:
    while True:
        SCREEN.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        stats_text = FONT.render("STATS SCREEN", True, "white")
        stats_rect = stats_text.get_rect(center=(640, 80))
        SCREEN.blit(stats_text, stats_rect)

        stats_back = Button(image=None, pos=(150, 670),
                        text_input="BACK", font=FONT,
                        base_color="white",
                        hovering_color="green")

        stats_back.changeColor(mouse_pos)
        stats_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stats_back.checkForInput(mouse_pos):
                    main_menu_eng()

        pygame.display.update()

### Stats Menu Ita
def stats_menu_ita() -> None:

    while True:
        SCREEN.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        stats_text = FONT.render("SCHERMO STATISTICHE", True, "white")
        stats_rect = stats_text.get_rect(center=(640, 80))
        SCREEN.blit(stats_text, stats_rect)

        stats_back = Button(image=None, pos=(200, 670),
                        text_input="INDIETRO", font=FONT,
                        base_color="white",
                        hovering_color="green")

        stats_back.changeColor(mouse_pos)
        stats_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stats_back.checkForInput(mouse_pos):
                    main_menu_ita()

        pygame.display.update()

def game(rand_word: str) -> None:
    global word_split
    global text_box_num, text_box_space

    contprova = 0
    life = 11

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

    nlett = 0
    for i in range(rand_word_len):
        if rand_word[i] not in rand_word[:i]:
            nlett += 1

    text_box_num = 0 
    text_box_space = 0
        
    guess_lett = ''
    word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]

    while True:
        SCREEN.fill("white")

        counter = 0
        space = 10

        pygame.draw.rect(SCREEN, "black", [50,300,550,350],2)

        while counter < rand_word_len:
            hidden = FONT2.render("_", True, "black")
            hidden_rect = hidden.get_rect()
            hidden_rect.center = (((50) + space), (150))
            SCREEN.blit(hidden, hidden_rect)
            space += 50
            counter += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if provaA == False:
                    if event.key == pygame.K_a:
                        guess_lett = 'a'
                        if guess_lett in rand_word:
                            provaA = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaB == False:
                    if event.key == pygame.K_b:
                        guess_lett = 'b'
                        if guess_lett in rand_word:
                            provaB = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaC == False:
                    if event.key == pygame.K_c:
                        guess_lett = 'c'
                        if guess_lett in rand_word:
                            provaC = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaD == False:
                    if event.key == pygame.K_d:
                        guess_lett = 'd'
                        if guess_lett in rand_word:
                            provaD = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaE == False:
                    if event.key == pygame.K_e:
                        guess_lett = 'e'
                        if guess_lett in rand_word:
                            provaE = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaF == False:
                    if event.key == pygame.K_f:
                        guess_lett = 'f'
                        if guess_lett in rand_word:
                            provaF = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaG == False: 
                    if event.key == pygame.K_g:
                        guess_lett = 'g'
                        if guess_lett in rand_word:
                            provaG = True
                            contprova += 1 
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaH == False:
                    if event.key == pygame.K_h:
                        guess_lett = 'h'
                        if guess_lett in rand_word:
                            provaH = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaI == False:
                    if event.key == pygame.K_i:
                        guess_lett = 'i'
                        if guess_lett in rand_word:
                            provaI = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaJ == False:
                    if event.key == pygame.K_j:
                        guess_lett = 'j'
                        if guess_lett in rand_word:
                            provaJ = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaK == False:
                    if event.key == pygame.K_k:
                        guess_lett = 'k'
                        if guess_lett in rand_word:
                            provaK = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaL == False: 
                    if event.key == pygame.K_l:
                        guess_lett = 'l'
                        if guess_lett in rand_word:
                            provaL = True
                            contprova += 1 
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaM == False:
                    if event.key == pygame.K_m:
                        guess_lett = 'm'
                        if guess_lett in rand_word:
                            provaM = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40 
                if provaN == False:
                    if event.key == pygame.K_n:
                        guess_lett = 'n'
                        if guess_lett in rand_word:
                            provaN = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaO == False:
                    if event.key == pygame.K_o:
                        guess_lett = 'o'
                        if guess_lett in rand_word:
                            provaO = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaP == False: 
                    if event.key == pygame.K_p:
                        guess_lett = 'p'
                        if guess_lett in rand_word:
                            provaP = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40 
                if provaQ == False:
                    if event.key == pygame.K_q:
                        guess_lett = 'q'
                        if guess_lett in rand_word:
                            provaQ = True
                            contprova += 1 
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaR == False:
                    if event.key == pygame.K_r:
                        guess_lett = 'r'
                        if guess_lett in rand_word:
                            provaR = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaS == False: 
                    if event.key == pygame.K_s:
                        guess_lett = 's'
                        if guess_lett in rand_word:
                            provaS = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaT == False:
                    if event.key == pygame.K_t:
                        guess_lett = 't'
                        if guess_lett in rand_word:
                            provaT = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaU == False:
                    if event.key == pygame.K_u:
                        guess_lett = 'u'
                        if guess_lett in rand_word:
                            provaU = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaV == False: 
                    if event.key == pygame.K_v:
                        guess_lett = 'v'
                        if guess_lett in rand_word:
                            provaV = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaW == False:
                    if event.key == pygame.K_w:
                        guess_lett = 'w'
                        if guess_lett in rand_word:
                            provaW = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaX == False:
                    if event.key == pygame.K_x:
                        guess_lett = 'x'
                        if guess_lett in rand_word:
                            provaX = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40
                if provaY == False:
                    if event.key == pygame.K_y:
                        guess_lett = 'y'
                        if guess_lett in rand_word:
                            provaY = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40 
                if provaZ == False:
                    if event.key == pygame.K_z:
                        guess_lett = 'z'
                        if guess_lett in rand_word:
                            provaZ = True
                            contprova += 1
                        if guess_lett not in rand_word:
                            life -= 1
                            text_box_num += 1
                            text_box_space += 40

        if life == 10:
            pygame.draw.rect(SCREEN, "black", [650, 640, 400, 10])
        elif life == 9:
            pygame.draw.rect(SCREEN, "black", [650, 540, 400, 10])       #750, 640, 10, 400
        elif life == 8:
            # aggiungi disegno
            print("c") # cancella
        elif life == 7:
            # aggiungi disegno
            print("D") # cancella
        elif life == 6:
            # aggiungi disegno
            print("aaa") # cancella
        elif life == 5:
            # aggiungi disegno
            print("aaa") # cancella
        elif life == 4:
            # aggiungi disegno
            print("aaa") # cancella
        elif life == 3:
            # aggiungi disegno
            print("aaa") # cancella
        elif life == 2:
            # aggiungi disegno
            print("aaa") # cancella
        elif life == 1:
            # aggiungi disegno
            print("aaa") # cancella
        elif life == 0:
            lost_menu()

        if contprova == nlett:
            print(contprova)
            win_menu()

        if provaA:
            place_letter("a", rand_word)
        if provaB:
            place_letter("b", rand_word)
        if provaC:
            place_letter("c", rand_word)
        if provaD:
            place_letter("d", rand_word)
        if provaE:
            place_letter("e", rand_word)
        if provaF:
            place_letter("f", rand_word)
        if provaG:
            place_letter("g", rand_word)
        if provaH:
            place_letter("h", rand_word)
        if provaI:
            place_letter("i", rand_word)
        if provaJ:
            place_letter("j", rand_word)
        if provaK:
            place_letter("k", rand_word)
        if provaL:
            place_letter("l", rand_word)
        if provaM:
            place_letter("m", rand_word)
        if provaN:
            place_letter("n", rand_word)
        if provaO:
            place_letter("o", rand_word)
        if provaP:
            place_letter("p", rand_word)
        if provaQ:
            place_letter("q", rand_word)
        if provaR:
            place_letter("r", rand_word)
        if provaS:
            place_letter("s", rand_word)
        if provaT:
            place_letter("t", rand_word)
        if provaU:
            place_letter("u", rand_word)
        if provaV:
            place_letter("v", rand_word)
        if provaW:
            place_letter("w", rand_word)
        if provaX:
            place_letter("x", rand_word)
        if provaY:
            place_letter("y", rand_word)
        if provaZ:
            place_letter("z", rand_word) 

        pygame.display.update()

def win_menu()-> None:
    global lang, diff
    user_text = ""
    INPUT_RECT = pygame.Rect(450, 370, 370, 40)
    NAME_FONT = pygame.font.SysFont("Arial", 30, bold=True)
    counter = 0
    #global rand_word
    while True:
        SCREEN.fill("white")

        mouse_pos = pygame.mouse.get_pos()

        if lang == "eng":
            end_text = FONT.render("YOU WIN!!!", True, "red")
            end_rect = end_text.get_rect(center=(640, 80))
            SCREEN.blit(end_text,end_rect)
            name_text = FONT.render("ENTER YOUR NAME", True, "black")
            name_rect = name_text.get_rect(center=(640, 250))
            SCREEN.blit(name_text, name_rect)
            pygame.draw.rect(SCREEN, "black", INPUT_RECT, 2)
            text_surf = NAME_FONT.render(user_text, True, "black")
            text_rect = text_surf.get_rect(center=(INPUT_RECT.centerx, INPUT_RECT.centery))
            SCREEN.blit(text_surf, text_rect)
            enter_but = Button(image=None,
                            pos=(640, 440),                                                               
                            text_input="ENTER", font=NAME_FONT,
                            base_color="black",
                            hovering_color="red")
            #word_text = FONT.render("The word was: " + rand_word, True, "black")
            #word_rect = word_text.get_rect(center=(640, 200))
            #SCREEN.blit(word_text, word_rect)
            
        elif lang == "ita":
            end_text = FONT.render("HAI VINTO!!!",True,"red")
            end_rect = end_text.get_rect(center=(640, 80))
            SCREEN.blit(end_text,end_rect)
            name_text = FONT.render("INSERISCI IL TUO NOME", True, "black")
            name_rect = name_text.get_rect(center=(640, 250))
            SCREEN.blit(name_text, name_rect)
            pygame.draw.rect(SCREEN, "black", INPUT_RECT, 2)
            text_surf = NAME_FONT.render(user_text, True, "black")
            text_rect = text_surf.get_rect(center=(INPUT_RECT.centerx, INPUT_RECT.centery))
            SCREEN.blit(text_surf, text_rect)
            enter_but = Button(image=None,
                            pos=(640, 440),                                                               
                            text_input="INVIO", font=NAME_FONT,
                            base_color="black",
                            hovering_color="red")
            #word_text = FONT.render("La parola era: " + rand_word, True, "black")
            #word_rect = word_text.get_rect(center=(640, 200))
            #SCREEN.blit(word_text, word_rect)

        for botton in [enter_but]:
            botton.changeColor(mouse_pos)
            botton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if enter_but.checkForInput(mouse_pos):
                    if Dbase(dbase="hangman.db").search(name=user_text):
                        db_name = user_text
                        db_score = Dbase(dbase="hangman.db").search(name=user_text)[0][1]
                        if diff == 0 or diff == 1:
                            db_score += 100
                        elif diff == 2:
                            db_score += 150
                        elif diff == 3:
                            db_score += 200
                        Dbase(dbase="hangman.db").update(name=user_text, score=db_score)
                        main_menu_eng()
                    else:
                        db_name = user_text
                        if diff == 0 or diff == 1:
                            db_score = 100
                        elif diff == 2:
                            db_score = 150
                        elif diff == 3:
                            db_score = 200
                        Dbase(dbase="hangman.db").insert(db_name, db_score)
                        main_menu_eng()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                    counter -= 1
                else:
                    user_text += event.unicode
                    counter += 1

        pygame.display.update()

def lost_menu() -> None:
    global lang
    while True:
        SCREEN.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        if lang == "eng":
            lose_text = FONT.render("YOU LOSE!", True, "red")
            lose_rect = lose_text.get_rect(center=(640, 80))
            SCREEN.blit(lose_text, lose_rect)
            tryagain_text = FONT.render("TRY AGAIN!", True, "yellow")
            tryagain_rect = tryagain_text.get_rect(center = (640, 300))
            SCREEN.blit(tryagain_text,tryagain_rect)
            back_but = Button(image=None,
                            pos=(200, 670),                                                               
                            text_input="BACK", font=FONT,
                            base_color="white",
                            hovering_color="red")

        elif lang == "ita":
            lose_text = FONT.render("HAI PERSO!", True, "red")
            lose_rect = lose_text.get_rect(center=(640, 80))
            SCREEN.blit(lose_text, lose_rect)
            tryagain_text = FONT.render("PROVA DI NUOVO!", True, "yellow")
            tryagain_rect = tryagain_text.get_rect(center = (640, 300))
            SCREEN.blit(tryagain_text,tryagain_rect)
            back_but = Button(image=None,
                            pos=(230, 670),                                                               
                            text_input="INDIETRO", font=FONT,
                            base_color="white",
                            hovering_color="red")

        for botton in [back_but]:
            botton.changeColor(mouse_pos)
            botton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_but.checkForInput(mouse_pos):
                    main_menu_eng()

        pygame.display.update()

def place_letter(letter, rand_word) -> None:
    space = 10
    word_space = 0
    while word_space < len(rand_word):
        if letter in word_split[word_space]:
            text_surf = FONT2.render(letter, True, "black")
            text_rect = text_surf.get_rect()
            text_rect.center = (((50) + space), (150))
            SCREEN.blit(text_surf, text_rect)
        word_space += 1
        space += 50

def box_letter(letter: chr) -> None:
    global text_box_num, text_box_space
    if text_box_num <= 5:
        lett = FONT2.render(letter, True, "black")
        lett_rect = lett.get_rect()
        lett_rect.center = (((90) + text_box_space), (350))
        SCREEN.blit(lett, lett_rect)

if __name__ == "__main__":
   # main_menu_eng()
   lang = "ita"
   lost_menu()