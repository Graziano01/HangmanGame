import random

def fast_eng():
    words = []
    with open("assets/wordlistengCompleto.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_easy_eng():
    words = []
    with open("assets/wordlistengCorte.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_med_eng():
    words = []
    with open("assets/wordlistengMedie.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_hard_eng():
    words = []
    with open("assets/wordlistengLunghe.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def fast_ita():
    words = []
    with open("assets/wordlistitaCompleto.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_easy_ita():
    words = []
    with open("assets/wordlistitaCorte.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_med_ita():
    words = []
    with open("assets/wordlistengMedie.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_hard_ita():
    words = []
    with open("assets/wordlistengLunghe.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word