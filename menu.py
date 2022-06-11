from tkinter import *
from db.database import *

root = Tk()
root.title('Menù v0.1')
root.geometry('1600x900')
root.resizable(FALSE, FALSE)

lab = Label(root, text='The Hangman Game!', font=('Georgia', 40))
lab.pack(side='top')

USERNAME = StringVar()
PASSWORD = StringVar()

# Start button
start_button = Button(root, text='Start', font=('Georgia', 15), width=10, height=3) # TODO: add command function
start_button.pack(side='right', padx=10, pady=10)

# Register button
register_button = Button(root, text='Register', font=('Georgia', 15), width=10, height=3, command=Register)
register_button.pack(side='right', padx=10, pady=10)
# Login button
login_button = Button(root, text='Login', font=('Georgia', 15), width=10, height=3, command=Login)
login_button.pack(side='right', padx=10, pady=10)

# TODO: add register and login form

root.mainloop()