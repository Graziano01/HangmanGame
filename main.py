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

    while True:
        SCREEN.fill("white")

        rand_word_len = len(rand_word)
        print(rand_word)
        contprova = 0
        text_box_num = 0 
        text_box_space = 0
        
        guess_lett = ''
        word_split = [rand_word[i:i+1] for i in range(0, len(rand_word), 1)]

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
        
        pygame.display.update()
            

def placeLetter(letter, rand_word):
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


if __name__ == "__main__":
    main_menu_eng()