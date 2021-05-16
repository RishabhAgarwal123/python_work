from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


def generate_random_word():
    # word = random.choice(list(english_french.items()))
    # canvas.itemconfig(converted_language, text=word[1])
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_background, image=front_img)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(converted_language, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_background, image=back_image)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(converted_language, text=current_card['English'], fill='white')


def known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv('./data/words_to_learn.csv', index=False)
    generate_random_word()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
# english_french = {row.English: row.French for(index, row) in data.iterrows()}


# Create Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Get Image
front_img = PhotoImage(file='./images/card_front.png')
back_image = PhotoImage(file='./images/card_back.png')
# Create Image
canvas_background = canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text="", fill='black', font=('Ariel', 40, 'italic'))
converted_language = canvas.create_text(400, 263, text="", fill='black', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Button
wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_random_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)

generate_random_word()
window.mainloop()
