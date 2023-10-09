from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_english.csv")
    lang_dict = original_data.to_dict(orient="records")
else:
    lang_dict = data.to_dict(orient="records")

word_dict = {}


def next_card():
    global word_dict, flip_timer
    window.after_cancel(flip_timer)
    word_dict = random.choice(lang_dict)
    word_in_french = word_dict["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word_in_french, fill="black")
    canvas.itemconfig(card_background, image=front_img)
    window.after(3000, func=flip_card)

def flip_card():
    word_in_english = word_dict["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word_in_english, fill="white")
    canvas.itemconfig(card_background,image=back_img)


def is_known():
    lang_dict.remove(word_dict)
    data = pandas.DataFrame(lang_dict)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR),

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")

card_background = canvas.create_image(410, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="right.png")
right_btn = Button(image=right_img, command=is_known)
right_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="wrong.png")
wrong_btn = Button(image=wrong_img, command=next_card)
wrong_btn.grid(column=0, row=1)

next_card()


window.mainloop()
