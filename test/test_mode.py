import random
import pytest


def test_fast_eng():
    assert type(fast_eng()) == str

def test_get_word_easy_eng():
    assert type(get_word_easy_eng()) == str

def test_get_word_med_eng():
    assert type(get_word_med_eng()) == str

def test_get_word_hard_eng():
    assert type(get_word_hard_eng()) == str

def test_fast_ita():
    assert type(fast_ita()) == str

def test_get_word_easy_ita():
    assert type(get_word_easy_ita()) == str

def test_get_word_med_ita():
    assert type(get_word_med_ita()) == str

def test_get_word_hard_ita():
    assert type(get_word_hard_ita()) == str


def fast_eng() -> str:
    words = []
    with open("assets/wordlistengCompleto.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_easy_eng() -> str:
    words = []
    with open("assets/wordlistengCorte.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_med_eng() -> str:
    words = []
    with open("assets/wordlistengMedie.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_hard_eng() -> str:
    words = []
    with open("assets/wordlistengLunghe.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def fast_ita() -> str:
    words = []
    with open("assets/wordlistitaCompleto.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_easy_ita() -> str:
    words = []
    with open("assets/wordlistitaCorte.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_med_ita() -> str:
    words = []
    with open("assets/wordlistitaMedie.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word

def get_word_hard_ita() -> str:
    words = []
    with open("assets/wordlistitaLunghe.txt", "r") as f:
        for line in f:
            word = line.rstrip("\n")
            words.append(word)
        rand_word = random.choice(words)
    return rand_word