import random
import string
from tkinter import *
import pyperclip

BACKGROUND_COLOR = "#f1f3f9"

root = Tk()
root.title('PwdGenV1')
root.geometry('300x300')
root.configure(bg=BACKGROUND_COLOR)
root.resizable(False, False)
passvar = StringVar()

def toggle_state():
    if hide_var.get():
        password_line.config(show="*")
        print('changed state to hide')
    else:
        password_line.config(show="")
        print('changed state to show')

def copy():
    password1 = passvar.get()
    pyperclip.copy(f'{password1}')
    print(f'copied {password1}')

def password():
    characters = ""

    if lowercase_letters.get():
        characters += string.ascii_lowercase
    if uppercase_letters.get():
        characters += string.ascii_uppercase
    if numbers.get():
        characters += string.digits
    if special_symbols.get():
        characters += string.punctuation

    password2 = ''.join(random.choice(characters) for _ in range(lenght_var.get()))
    print('generated ' + password2)
    password_line.delete(0, END)
    password_line.insert(0, password2)
    passvar.set(f'{password2}')

lowercase_letters = BooleanVar()
lowercase_letters.set(True)

uppercase_letters = BooleanVar()
uppercase_letters.set(True)

numbers = BooleanVar()
numbers.set(True)

special_symbols = BooleanVar()
special_symbols.set(True)


lenght_var = IntVar()
lenght_var.set(16)

var = StringVar()

lowercase_checkbox = Checkbutton(root, width=10, bg=BACKGROUND_COLOR, text="Klein", variable=lowercase_letters)

uppdercase_checkbox = Checkbutton(root, width=10, bg=BACKGROUND_COLOR, text="Groß",  variable=uppercase_letters)

digits_checkbox = Checkbutton(root, width=10, bg=BACKGROUND_COLOR, text="Zahlen", variable=numbers)

punctuation_checkbox = Checkbutton(root, width=10, bg=BACKGROUND_COLOR, text="Zeichen", variable=special_symbols)

password_copy_btn = Button(root, width=10, bg=BACKGROUND_COLOR, text='Copy', command=copy)

password_create_btn = Button(root, width=10, bg=BACKGROUND_COLOR, text='Create', command=password)

password_line = Entry(root, width=20, font=10, bg=BACKGROUND_COLOR, textvariable=passvar)

password_lenght = Entry(root, width=10, font=10, bg=BACKGROUND_COLOR, textvariable=lenght_var)

hide_var = BooleanVar()
hide_checkbox = Checkbutton(root, width=10, bg=BACKGROUND_COLOR, text="hide", variable=hide_var, command=toggle_state)

lenght_label = Label(root, width=10, bg=BACKGROUND_COLOR, text="Länge")

lenght_label.pack()
password_lenght.pack()

lowercase_checkbox.pack()
uppdercase_checkbox.pack()
digits_checkbox.pack()
punctuation_checkbox.pack()

hide_checkbox.pack()
password_create_btn.pack()
password_line.pack()
password_copy_btn.pack()

root.protocol('WM_DELETE_WINDOW')
root.mainloop()