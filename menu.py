from tkinter import *
import sqlite3
#import time

"""
FIX:
login e register bug
---background---
"""

root = Tk()
root.title('Menù v0.1')

width = 1600    
height = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# Background image
image = PhotoImage(file="hangman.png")
labImage = Label(root, image=image)
labImage.place(x=0, y=0)

lab = Label(root, text='The Hangman Game!', font=('Georgia', 40), bg="#ffffff")
lab.pack(side='top')

USERNAME = StringVar()
PASSWORD = StringVar()

def Database():
        global conn, curs
        # Connect database
        conn = sqlite3.connect("database.db")
        curs = conn.cursor()
        # Execute query
        curs.execute("CREATE TABLE IF NOT EXISTS `user` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, score INTEGER)")

def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('Georgia', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('Georgia', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('Georgia', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('Georgia', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('Georgia', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('Georgia', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
     
def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(RegisterFrame, text="Username:", font=('Georgia', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('Georgia', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_result2 = Label(RegisterFrame, text="", font=('Georgia', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('Georgia', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('Georgia', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('Georgia', 18), width=35, command=Register)
    btn_login.grid(row=6, columnspan=2, pady=20)

def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        curs.execute("SELECT * FROM `user` WHERE `username` = ?", (USERNAME.get(),))
        if curs.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            curs.execute("INSERT INTO `user` (username, password) VALUES(?, ?)", (str(USERNAME.get()), str(PASSWORD.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        curs.close()
        conn.close()

def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        curs.execute("SELECT * FROM `user` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if curs.fetchone() is not None:
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result1.config(text="You Successfully Login", fg="blue")
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")

# Start button
start_button = Button(root, text='Start', font=('Georgia', 15), width=10, height=3) # TODO: add command function
start_button.pack(side='right', padx=10, pady=10)

# Register button
register_button = Button(root, text='Register', font=('Georgia', 15), width=10, height=3, command=RegisterForm)
register_button.pack(side='right', padx=10, pady=10)
# Login button
login_button = Button(root, text='Login', font=('Georgia', 15), width=10, height=3, command=LoginForm)
login_button.pack(side='right', padx=10, pady=10)

root.mainloop()