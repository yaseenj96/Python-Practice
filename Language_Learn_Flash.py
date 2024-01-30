BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
import pandas
import random
TITLE_FONT = ("Arial",40,"italic")
WORD_FONT=("Arial",60,"bold")

##----------- FLASH CARD FUNCTIONALITY -----------------------##

translation = {}

def flip_card():
    english_word=translation["English"]
    canvas.itemconfig(front, image=card_back)
    canvas.itemconfig(title,text='English',fill='white')
    canvas.itemconfig(word,text=english_word,fill='white')


def generate_new_word(widget):
    try:
        with open('./data/words_to_learn.csv') as file:
            data = pandas.read_csv(file)
            fdf = pandas.DataFrame(data).to_dict(orient="records")
    except FileNotFoundError:
        with open('./data/words_to_learn.csv','w') as file:
            data = pandas.read_csv('./data/french_words.csv')
            french_dataframe = pandas.DataFrame(data)
            fdf = french_dataframe.to_dict(orient="records")
            french_dataframe.to_csv(file, index=False)
    finally:
        print("function triggered by ", widget)
        global translation, flip_timer
        window.after_cancel(flip_timer)
        translation = random.choice(fdf)
        french_word = translation['French']
        canvas.itemconfig(word, text=french_word,fill='green')
        canvas.itemconfig(title,text='French',fill='green')
        canvas.itemconfig(front,image=card_front)
        flip_timer = window.after(3000,flip_card)
        if widget == right_button:
            fdf.remove(translation)
            with open('./data/words_to_learn.csv', 'w') as file:
                french_dataframe = pandas.DataFrame.from_dict(fdf)
                french_dataframe.to_csv(file, index=False)



##------------GUI----------------##
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right, highlightthickness=0)
right_button.config(command= lambda obj=right_button : generate_new_word(obj))
wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.config(command= lambda obj=wrong_button : generate_new_word(obj))
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)

#Front Card
front = canvas.create_image(400,263, image=card_front)
canvas.grid(row=0,column=0,columnspan=2)
#Title Label
title = canvas.create_text(400,150,text="Title", font=TITLE_FONT)
word = canvas.create_text(400,263,text="Word",font=WORD_FONT)
#Wrong
wrong_button.grid(row=1,column=0)
#Right
right_button.grid(row=1,column=1)



window.mainloop()
