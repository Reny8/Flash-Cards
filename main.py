from tkinter import *
from tkinter import ttk
RED = "#92140C"
GREEN = "#003E1F"
BACKGROUND = "#808080"

# WINDOW SETTINGS
window = Tk()
window.title("Flash Cards")
window.config(padx=60, pady=60, bg=BACKGROUND)


# ANSWER SIDE OF THE INDEX CARD
canvas = Canvas(width=768, height=450)
front_card_img = PhotoImage(file="images/back_card_img.png")
canvas.create_image(384, 230, image=front_card_img)
canvas.create_text(384, 230, text="Answer", font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=3)

separator = ttk.Separator(window, orient='horizontal')
# BUTTONS

# WRONG ANSWER BUTTON
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image)
wrong_button.grid(row=1, column=0)

# RIGHT ANSWER BUTTON
check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image)
right_button.grid(row=1, column=2)

# FLIP THE CARD BUTTON
flip_image = PhotoImage(file="images/flip.png")
flip_button = Button(image=flip_image)
flip_button.grid(row=1,column=1)

window.mainloop()
