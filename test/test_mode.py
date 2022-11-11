import random
import pytest


def test_fast_eng():
    lang = "eng"
    assert type(fast(lang)) == str
    lang = "ita"
    assert type(fast(lang)) == str

def test_get_word_easy_eng():
    lang = "eng"
    assert type(get_word_easy(lang)) == str
    lang = "ita"
    assert type(get_word_easy(lang)) == str

def test_get_word_med_eng():
    lang = "eng"
    assert type(get_word_med(lang)) == str
    lang = "ita"
    assert type(get_word_med(lang)) == str

def test_get_word_hard_eng():
    lang = "eng"
    assert type(get_word_hard(lang)) == str
    lang = "ita"
    assert type(get_word_hard(lang)) == str


def fast(lang: str) -> str:
    if lang == "eng":
        words = []
        with open("assets/wordlistengCompleto.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word
    elif lang == "ita":
        words = []
        with open("assets/wordlistitaCompleto.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word

def get_word_easy(lang: str) -> str:
    if lang == "eng":
        words = []
        with open("assets/wordlistengCorte.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word
    elif lang == "ita":
        words = []
        with open("assets/wordlistitaCorte.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word

def get_word_med(lang: str) -> str:
    if lang == "eng":
        words = []
        with open("assets/wordlistengMedie.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word
    elif lang == "ita":
        words = []
        with open("assets/wordlistitaMedie.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word

def get_word_hard(lang: str) -> str:
    if lang == "eng":
        words = []
        with open("assets/wordlistengLunghe.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word
    elif lang == "ita":
        words = []
        with open("assets/wordlistitaLunghe.txt", "r") as f:
            for line in f:
                word = line.rstrip("\n")
                words.append(word)
            rand_word = random.choice(words)
        return rand_word