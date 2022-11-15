from tkinter import *
from tkinter import ttk
import pandas
import random

# COLORS USED
BACKGROUND = "#6C7D47"
NAVY = "#324A5F"

# FUNCTIONALITY
data = pandas.read_csv("data/french_words.csv")
cards = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(cards)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    return current_card

def flip_card():
    canvas.itemconfig(card_title, text="English", fill=NAVY)
    canvas.itemconfig(card_word, text= value["English"], fill=NAVY)


# WINDOW SETTINGS
window = Tk()
window.title("Flash Cards")
window.config(padx=60, pady=60, bg=BACKGROUND)

# ANSWER SIDE OF THE INDEX CARD
canvas = Canvas(width=768, height=450)
card_image = PhotoImage(file="images/card.png")
canvas_image = canvas.create_image(384, 230, image=card_image)
card_title = canvas.create_text(384, 115, text="", font=("Arial", 20, "italic"))
card_word = canvas.create_text(384, 230, text="", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

separator = ttk.Separator(window, orient='horizontal')
# BUTTONS

# WRONG ANSWER BUTTON
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, borderwidth=0, bg=BACKGROUND, command=next_card)
wrong_button.grid(row=1, column=0)

# RIGHT ANSWER BUTTON
check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, borderwidth=0, bg=BACKGROUND, command=next_card)
right_button.grid(row=1, column=2)

# FLIP THE CARD BUTTON
flip_image = PhotoImage(file="images/flip.png")
flip_button = Button(image=flip_image, borderwidth=0, bg=BACKGROUND, command=flip_card)
flip_button.grid(row=1,column=1)

# RUN APP
value = next_card()
window.mainloop()
