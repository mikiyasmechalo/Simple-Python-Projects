from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox
import pyperclip

WIDTH = 39
email_list = ["mikiyasmechalo70@gmail.com", "mikiyasmechalo5@gmail.com", "mikeme362@gmail.com",
              "mikiyas.mechalo@aastustudent.edu.et"]
last_email_option_row = 2
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list += password_letters
    password_list += password_symbols
    password_list += password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():  # updated with exception handling
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message='Please dont leave any fields empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} '
                                                              f'\nPassword: {password} \nIs it okay to save?')
        if is_ok:
            with open('data.txt', mode='a') as data:
                data.write(f'{website} | {email} | {password}\n')

                password_entry.delete(0, END)
                website_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
# window.minsize(500, 300)
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_name_label = Label(text='Website:')
website_name_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=last_email_option_row + 3)

website_entry = Entry(width=WIDTH)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=WIDTH)
email_entry.grid(column=1, row=last_email_option_row + 2, columnspan=2)
email_entry.insert(END, 'mikiyasmechalo70@gmail.com')  # END - end of the text , 0 - in the beginning
password_entry = Entry(width=21)
password_entry.grid(column=1, row=last_email_option_row + 3)

generate_button = Button(text='generate password', command=generate_password)
generate_button.grid(column=2, row=last_email_option_row + 3)
add_button = Button(text='add', command=add_password, width=33)
add_button.grid(column=1, row=last_email_option_row + 4, columnspan=2)


def email_used(event):
    email_entry.delete(0, END)
    email_entry.insert(0, listbox.get(listbox.curselection()))


listbox = Listbox(height=4, width=WIDTH)
for item in email_list:
    listbox.insert(email_list.index(item), item)
listbox.bind("<<ListboxSelect>>", email_used)
listbox.grid(column=1, row=2, columnspan=2)


window.mainloop()
