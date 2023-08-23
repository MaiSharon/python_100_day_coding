import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

# 番茄中四個循環
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # 停住倒數
    windows.after_cancel(timer)
    # 歸回開始畫面
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_ok.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    print(timer)
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # 分鐘:　秒除以60只求整數
    count_min = math.floor(count / 60)
    # 秒數: 總秒除以分鐘(60秒)求餘數
    count_sec = count % 60
    print(count_sec)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # canvas組件更新方式與 label 不同
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # 1000 毫秒（1秒）後調用 count_down 函數，並將 count - 1 作為參數傳遞給該函數
        ## after 方法返回一個 id，你可以使用此 id 來取消待定的定時器
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_count = math.floor(reps / 2)
        for _ in range(work_count):
            mark += "✓"
        label_ok.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# 導入番茄圖片
tomato_img = PhotoImage(file="tomato.png")
# 顯示番茄圖片，記得打包
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# 倒數計時並更新 canvas
# conut_down(5)

# label
label_timer = Label(text="Timer", font=(FONT_NAME, 36), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_ok = Label(font=(FONT_NAME, 16), fg=GREEN, bg=YELLOW)
label_ok.grid(column=1, row=3)

# Button
button_start = Button(text="Start", font=(FONT_NAME, 10), command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

windows.mainloop()
