import random
from tkinter import *
import pandas


class FlashyApp:
    def __init__(self):
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.FONT_NAME = "Ariel"

        # 導入CSV文件
        try:
            self.data = pandas.read_csv("data/unknown_word.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("data/french_words.csv")
        finally:
            self.flashcards = self.data.to_dict(orient="records")

        # 當前卡片題目
        self.current_card = {}

        # 視窗初始化
        self.windows = Tk()
        self.main_windows()
        self.flip_timer = self.windows.after(3000, self.flip_card)  # 等三秒後翻面解答答案，此功能較為特別會排在mainloop()之後執行
        self.initialize_canvas_and_buttons()  # 創建初始化畫布與導入圖片
        self.next_card()  # 首先更新正面卡片題目
        self.windows.mainloop()

    def main_windows(self):
        """主程式視窗初始化設定"""
        self.windows.title("Flashy")
        self.windows.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)

    def initialize_canvas_and_buttons(self):
        """初始化畫布和按鈕"""
        self.canvas = Canvas(width=800, height=526, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.img_front = PhotoImage(file="images/card_front.png")
        self.img_back = PhotoImage(file="images/card_back.png")
        self.img_right = PhotoImage(file="images/right.png")
        self.img_wrong = PhotoImage(file="images/wrong.png")
        self.card_front = self.canvas.create_image(400, 263, image=self.img_front)
        self.card_title = self.canvas.create_text(400, 150, text="", font=(self.FONT_NAME, 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=(self.FONT_NAME, 40, "bold"))
        self.canvas.grid(column=0, row=0, columnspan=2)
        btn_unknown = Button(width=100, image=self.img_wrong, relief="flat", bg=self.BACKGROUND_COLOR,
                             command=self.next_card)
        btn_unknown.grid(column=0, row=1)
        btn_learned = Button(width=100, image=self.img_right, relief="flat", bg=self.BACKGROUND_COLOR,
                             command=self.remove_learned_card)
        btn_learned.grid(column=1, row=1)

    def flip_card(self):
        """背面卡片答案"""
        self.canvas.itemconfig(self.card_front, image=self.img_back)
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_card["English"], fill="white")

    def next_card(self):
        """卡片題目更新"""
        self.windows.after_cancel(self.flip_timer)  # 若三秒內按下一張卡片則取消三秒延遲
        self.current_card = random.choice(self.flashcards)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_card["French"], fill="black")
        self.canvas.itemconfig(self.card_front, image=self.img_front)
        self.flip_timer = self.windows.after(3000, self.flip_card)

    def remove_learned_card(self):
        """刪除已經學會的卡片"""
        self.flashcards.remove(self.current_card)
        new_learn_data = pandas.DataFrame(self.flashcards)
        new_learn_data.to_csv("data/unknown_word.csv", index=False)
        self.next_card()  # 繼續更新卡片


if __name__ == "__main__":
    FlashyApp()
