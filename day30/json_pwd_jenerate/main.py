import json
from tkinter import *
from tkinter import messagebox

import pyperclip as pyperclip

FONT_NAME = "Courier"


# ---------------------------- Search ------------------------------------------- #
def search_pwd():
    web = entry_web.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="No Data File Found")
    else:
        """ 使用get()的方式 
        find_web = data.get(web)
        if find_web:
            email = find_web.get("email")
            pwd = find_web.get("password")
            messagebox.showinfo(title=web, message=f"Email:{email}\n"
                                                    f"password:{pwd}")
        else:
            messagebox.showerror(title="Oops!", message="No details for the website exists")
        """
        if web in data:
            email = data[web]["email"]
            pwd = data[web]["password"]
            print(email, pwd)
            messagebox.showinfo(title=web, message=f"Email:{email}\n"
                                                   f"password:{pwd}")
        else:
            messagebox.showerror(title="Oops!", message="No details for the website exists")
    finally:
        # 刪除輸入框網站的內容
        entry_web.delete(0, END)


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

    password = "".join(password_list)

    pwd_not_empty = entry_pwd.get()
    if pwd_not_empty:
        entry_pwd.delete(0, END)

    entry_pwd.insert(0, password)

    # --- 當按下密碼生成按鈕後自動執行複製 ---
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pwd():
    web = entry_web.get()
    email = entry_user.get()
    pwd = entry_pwd.get()
    new_data = {
        web: {
            "email": email,
            "password": pwd,
        }
    }

    # --- 若為空數據出現警告 ---
    if web and email and pwd:
        # 數據確認
        check_msg = messagebox.askokcancel(title=web, message=f"There are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {pwd} \nIs it ok to save?")
    # --- 若不為空數據出現則儲存數據 ---
        if check_msg:

            try:
                with open("data.json", "r") as data_file:
                    # 讀取舊數據
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # 新增文件並寫入輸入框數據
                    json.dump(new_data, data_file, indent=4)
            else:
                # 更新json數據json.update() 把 new_data (輸入框的內容)字典中的鍵值對合併到 data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # 寫入更新後的數據
                    json.dump(data, data_file, indent=4)
            finally:
                # 刪除輸入框網站與密碼的內容
                entry_web.delete(0, END)
                entry_pwd.delete(0, END)
    else:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")


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

# ------ 第一行-哪個網站與搜尋 ------ #
label_web = Label(text="Website:", font=(FONT_NAME, 8))
label_web.grid(column=0, row=1)

# 輸入框
entry_web = Entry(width=24)
entry_web.grid(column=1, row=1, columnspan=2, sticky="W")

button_Search = Button(text="Search", command=search_pwd)
button_Search.grid(column=2, row=1, sticky="EW")

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
