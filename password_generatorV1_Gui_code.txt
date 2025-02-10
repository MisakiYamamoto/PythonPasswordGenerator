# imports
import string
import secrets
from tkinter import *
import pyperclip

root = Tk()
root.title('PwdGenV1')
root.geometry('378x100')
root.configure(bg='#1c1c1c')

passvar = StringVar()

def copy():
    password = passvar.get()
    pyperclip.copy(f'{password}')
    # print(f'copied {password}')

def password():
    CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    PASSWORD = ''.join(secrets.choice(CHARACTERS) for _ in range(lenght_var.get()))
    # print('generated ' + PASSWORD)
    password_line.delete(0, END)
    password_line.insert(0, PASSWORD)
    passvar.set(f'{PASSWORD}')
    # password_line.config(show='#')

def toggle_state():
    if hide_var.get():
        password_line.config(show="*")
        # print('changed state to hide')
    else:
        password_line.config(show="")
        # print('changed state to show')

lenght_var = IntVar()
var = StringVar()
# LENGHT = str(input(""))
password_copy_btn = Button(root, text='Copy', command=copy)
password_create_btn = Button(root, text='Create', command=password)
password_line = Entry(root, width=21, font=10, textvariable=passvar)
password_lenght = Entry(root, width=5, font=10, textvariable=lenght_var)
# lenght_label = Label(root, text="LENGHT").pack()

hide_var = BooleanVar()
hide_checkbox = Checkbutton(root, text="hide", variable=hide_var, command=toggle_state)

hide_checkbox.pack(anchor="w" ,side='left', padx=0)
password_copy_btn.pack(side='left', padx=0)
password_create_btn.pack(side='left', padx=0)
password_lenght.pack(side='left', padx=1)
password_line.pack(side='left', padx=1)

root.protocol('WM_DELETE_WINDOW')

root.mainloop()