from tkinter import *
from tkinter import messagebox

import pyperclip as pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwd_generate():
    # Password Generator Project
    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'flashcards', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pws_letters = [random.choice(letters) for _ in range(nr_letters)]
    pws_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pws_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pws_number + pws_letters + pws_symbols

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)
    # print(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char
    entry_pwd.insert(0, password)

    # --- 當按下密碼生成按鈕後自動執行複製 ---
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pwd():
    web = entry_web.get()
    user = entry_user.get()
    pwd = entry_pwd.get()

    '''使用with可以不用每次輸入close
    f_pwd = open("pwd_manager.txt", "a")
    f_pwd.write(f"{entry_web.get()} | {entry_user.get()} | {entry_pwd.get()} \n")     
    f_pwd.close()
    '''

    # --- 若為空數據出現警告 ---
    if web and user and pwd:
        # 數據確認
        check_msg = messagebox.askokcancel(title=web, message=f"There are the details entered: \nEmail: {user}"
                                                              f"\nPassword: {pwd} \nIs it ok to save?")
        if check_msg:
            with open("pwd_manager.txt", "a") as data_file:
                data_file.write(f"{web} | {user} | {pwd}\n")
                # 刪除輸入框網站與密碼的內容
                entry_web.delete(0, END)
                entry_pwd.delete(0, END)
    else:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")

    # print check
    f_pwd = open("pwd_manager.txt", "r")
    print(f_pwd.read())


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

# ------ 第零行_設定圖片 ------ #
canvas = Canvas(width=200, height=200, highlightthickness=0)
# 導入番茄圖片
mypass_img = PhotoImage(file="logo.png")
# 顯示番茄圖片，並設定位置基本上為Canvas參數的一半即可置中
canvas.create_image(100, 100, image=mypass_img)
# 記得打包，才會出現圖片
canvas.grid(column=1, row=0)

# ------ 第一行-哪個網站 ------ #
label_web = Label(text="Website:", font=(FONT_NAME, 8))
label_web.grid(column=0, row=1)

# 輸入框
entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, columnspan=2, sticky="EW")

# ------ 第二行-輸入使用者 ------ #
label_user = Label(text="Email/Username:", font=(FONT_NAME, 8))
label_user.grid(column=0, row=2)

entry_user = Entry(width=35)
entry_user.insert(0, "angle52230@gmail")
entry_user.grid(column=1, row=2, columnspan=2, sticky="EW")

# ------ 第三行-生成密碼 ------ #
label_pwd = Label(text="Password:", font=(FONT_NAME, 8))
label_pwd.grid(column=0, row=3)

entry_pwd = Entry(width=24)
entry_pwd.grid(column=1, row=3, sticky="W")

button_pwd_generate = Button(text="Generate Password", command=pwd_generate)
button_pwd_generate.grid(column=2, row=3, sticky="EW")

# ------ 第四行-Add按鈕 ------ #
button_add = Button(width=36, text="Add", command=save_pwd)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

windows.mainloop()
