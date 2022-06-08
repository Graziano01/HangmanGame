from tkinter import *
import sqlite3
from db.database import Database

root = Tk()
root.title('Menù v0.1')
root.geometry('1600x900')

lab = Label(root, text='The Hangman Game!', font=('Georgia', 40))
lab.pack(side='top')

# Start button
start_button = Button(root, text='Start', font=('Georgia', 15), width=10, height=3) # todo: add command function
start_button.pack(side='right', padx=10, pady=10)

# TODO: Register and Login function

root.mainloop()