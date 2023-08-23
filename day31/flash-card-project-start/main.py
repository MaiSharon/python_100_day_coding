import random
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}

# 下次打開將從不知道的字卡(刪除已學會的字卡)開始
try:
    data = pandas.read_csv("data/unknown_word.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    flashcards = data.to_dict(orient="records")
else:
    flashcards = data.to_dict(orient="records")


def next_card():
    global current_card  # 保持正面跟背面使用同一組字典
    global flip_timer    # 抓取外面的全局變量的3sec延遲，供應取消延遲(after_cancel)使用

    # 當典籍"正確" 或 "不知道" 按鈕後 則取消3sec的延遲翻面
    windows.after_cancel(flip_timer)

    current_card = random.choice(flashcards)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_front, image=img_front)

    # 再更新變量新的3sec延遲
    flip_timer = windows.after(3000, flip_card)


def is_learned_card():
    flashcards.remove(current_card)
    print(len(flashcards))  # check word count
    remove_learned_card = pandas.DataFrame(flashcards)
    remove_learned_card.to_csv("data/unknown_word.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_front, image=img_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# window set
windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 3sec flip card
flip_timer = windows.after(3000, flip_card)

# canvas init and import img
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")

# card set
card_front = canvas.create_image(400, 263, image=img_front)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
btn_unknown = Button(width=100, image=img_wrong, relief="flat", bg=BACKGROUND_COLOR, command=next_card)
btn_unknown.grid(column=0, row=1)

btn_learned = Button(width=100, image=img_right, relief="flat", bg=BACKGROUND_COLOR, command=is_learned_card)
btn_learned.grid(column=1, row=1)


next_card()

windows.mainloop()


