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
    global lang
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
    global lang
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
    global lang
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
                    word = get_word_easy_eng()
                    game(word)
                if medium_but.checkForInput(play_mouse_pos):
                    word = get_word_med_eng()
                    game(word)
                if hard_but.checkForInput(play_mouse_pos):
                    word = get_word_hard_eng()
                    game(word)

        pygame.display.update()

### Difficulty Select Menu ITA ###
def play_menu_ita() -> None:
    global lang
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
                    word = get_word_easy_ita()
                    game(word)
                if medium_but.checkForInput(play_mouse_pos):
                    word = get_word_med_ita()
                    game(word)
                if hard_but.checkForInput(play_mouse_pos):
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
                if provaB == False:
                    if event.key == pygame.K_b:
                        guess_lett = 'b'
                        if guess_lett in rand_word:
                            provaB = True
                            contprova += 1
                if provaC == False:
                    if event.key == pygame.K_c:
                        guess_lett = 'c'
                        if guess_lett in rand_word:
                            provaC = True
                            contprova += 1
                if provaD == False:
                    if event.key == pygame.K_d:
                        guess_lett = 'd'
                        if guess_lett in rand_word:
                            provaD = True
                            contprova += 1
                if provaE == False:
                    if event.key == pygame.K_e:
                        guess_lett = 'e'
                        if guess_lett in rand_word:
                            provaE = True
                            contprova += 1
                if provaF == False:
                    if event.key == pygame.K_f:
                        guess_lett = 'f'
                        if guess_lett in rand_word:
                            provaF = True
                            contprova += 1
                if provaG == False: 
                    if event.key == pygame.K_g:
                        guess_lett = 'g'
                        if guess_lett in rand_word:
                            provaG = True
                            contprova += 1 
                if provaH == False:
                    if event.key == pygame.K_h:
                        guess_lett = 'h'
                        if guess_lett in rand_word:
                            provaH = True
                            contprova += 1
                if provaI == False:
                    if event.key == pygame.K_i:
                        guess_lett = 'i'
                        if guess_lett in rand_word:
                            provaI = True
                            contprova += 1
                if provaJ == False:
                    if event.key == pygame.K_j:
                        guess_lett = 'j'
                        if guess_lett in rand_word:
                            provaJ = True
                            contprova += 1 
                if provaK == False:
                    if event.key == pygame.K_k:
                        guess_lett = 'k'
                        if guess_lett in rand_word:
                            provaK = True
                            contprova += 1
                if provaL == False: 
                    if event.key == pygame.K_l:
                        guess_lett = 'l'
                        if guess_lett in rand_word:
                            provaL = True
                            contprova += 1 
                if provaM == False:
                    if event.key == pygame.K_m:
                        guess_lett = 'm'
                        if guess_lett in rand_word:
                            provaM = True
                            contprova += 1 
                if provaN == False:
                    if event.key == pygame.K_n:
                        guess_lett = 'n'
                        if guess_lett in rand_word:
                            provaN = True
                            contprova += 1 
                if provaO == False:
                    if event.key == pygame.K_o:
                        guess_lett = 'o'
                        if guess_lett in rand_word:
                            provaO = True
                            contprova += 1
                if provaP == False: 
                    if event.key == pygame.K_p:
                        guess_lett = 'p'
                        if guess_lett in rand_word:
                            provaP = True
                            contprova += 1 
                if provaQ == False:
                    if event.key == pygame.K_q:
                        guess_lett = 'q'
                        if guess_lett in rand_word:
                            provaQ = True
                            contprova += 1 
                if provaR == False:
                    if event.key == pygame.K_r:
                        guess_lett = 'r'
                        if guess_lett in rand_word:
                            provaR = True
                            contprova += 1
                if provaS == False: 
                    if event.key == pygame.K_s:
                        guess_lett = 's'
                        if guess_lett in rand_word:
                            provaS = True
                            contprova += 1 
                if provaT == False:
                    if event.key == pygame.K_t:
                        guess_lett = 't'
                        if guess_lett in rand_word:
                            provaT = True
                            contprova += 1 
                if provaU == False:
                    if event.key == pygame.K_u:
                        guess_lett = 'u'
                        if guess_lett in rand_word:
                            provaU = True
                            contprova += 1
                if provaV == False: 
                    if event.key == pygame.K_v:
                        guess_lett = 'v'
                        if guess_lett in rand_word:
                            provaV = True
                            contprova += 1 
                if provaW == False:
                    if event.key == pygame.K_w:
                        guess_lett = 'w'
                        if guess_lett in rand_word:
                            provaW = True
                            contprova += 1 
                if provaX == False:
                    if event.key == pygame.K_x:
                        guess_lett = 'x'
                        if guess_lett in rand_word:
                            provaX = True
                            contprova += 1 
                if provaY == False:
                    if event.key == pygame.K_y:
                        guess_lett = 'y'
                        if guess_lett in rand_word:
                            provaY = True
                            contprova += 1 
                if provaZ == False:
                    if event.key == pygame.K_z:
                        guess_lett = 'z'
                        if guess_lett in rand_word:
                            provaZ = True
                            contprova += 1 

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
    global lang
    #global rand_word
    while True:
        SCREEN.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        if lang == "eng":
            end_text = FONT.render("YOU WIN!!!",True,"white")
            end_rect = end_text.get_rect(center=(640, 80))
            SCREEN.blit(end_text,end_rect)
            #word_text = FONT.render("The word was: " + rand_word, True, "white")
            #word_rect = word_text.get_rect(center=(640, 200))
            #SCREEN.blit(word_text, word_rect)
            end_back = Button(image=None, pos=(150, 670),
                            text_input="BACK", font=FONT,
                            base_color="white", 
                            hovering_color="green")
        elif lang == "ita":
            end_text = FONT.render("HAI VINTO!!!",True,"white")
            end_rect = end_text.get_rect(center=(640, 80))
            SCREEN.blit(end_text,end_rect)
            #word_text = FONT.render("La parola era: " + rand_word, True, "white")
            #word_rect = word_text.get_rect(center=(640, 200))
            #SCREEN.blit(word_text, word_rect)
            end_back = Button(image=None, pos=(200, 670),
                            text_input="INDIETRO", font=FONT,
                            base_color="white", 
                            hovering_color="green")

        end_back.changeColor(mouse_pos)
        end_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_back.checkForInput(mouse_pos):
                    main_menu_eng()

        pygame.display.update()   

def place_letter(letter, rand_word):
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

#def box_letter():

if __name__ == "__main__":
    main_menu_eng()