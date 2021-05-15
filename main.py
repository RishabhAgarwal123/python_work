from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    # global randomPassword
    # for num in range(nr_letters):
    #     randomPassword = randomPassword + random.choice(letters)
    # for num in range(nr_symbols):
    #     randomPassword = randomPassword + random.choice(symbols)
    # for num in range(nr_numbers):
    #     randomPassword = randomPassword + random.choice(numbers)
    # randomPassword = ''.join(random.sample(randomPassword, len(randomPassword)))
    # for char in password_list:
    #     randomPassword = randomPassword + char
    randomPassword = ''.join(password_list)
    pyperclip.copy(randomPassword)
    password_entry.insert(0, randomPassword)
    # print(randomPassword)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 and len(password) > 0:
        user_data = f'{website} | {email} | {password}'
        valid = messagebox.askokcancel(title=website, message=f'These are details entered: \n{user_data}')
        if valid:
            with open('user data.txt', mode='a') as file:
                file.write(user_data + '\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title='oops', message='Do not leave any field empty')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('PASSWORD MANAGER')
window.config(padx=50, pady=50)

# Create Canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Creating Labels
website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

# Input User Data
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'rishabh@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Creating Button
generate_password = Button(text='Generate', command=generate_password)
generate_password.grid(column=2, row=3)

add = Button(text='Add', width=36, command=save)
add.grid(column=1, row=4, columnspan=2)
window.mainloop()
