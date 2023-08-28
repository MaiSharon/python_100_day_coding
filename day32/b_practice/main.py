##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import os
import random
import datetime as dt
import smtplib
import pandas as pd

# 信件資料
MY_EMAIL = "you-email"
EMAIL_PASSWORD ="pwd"

# 今天是幾月幾號
now = dt.datetime.now()
today = (now.month, now.day)

# 確認今天有沒有人生日
data = pd.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row.to_dict() for (index, row) in data.iterrows()}

# 若有人生日
if today in birthday_dict:
    # 提取壽星名字和信箱
    name = birthday_dict[today]["name"]
    email = birthday_dict[today]["email"]

    # 隨機選擇1張生日祝賀信件
    letter_list = os.listdir("letter_templates")
    pick_one_letter = ''.join(random.choices(letter_list))

    # 修改信件[NAME]為壽星名字
    with open(f"letter_templates/{pick_one_letter}",mode="r") as f:
        letter = f.read()
        birthday_letter = letter.replace("[NAME]", name)

    # 寄信
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        # 信件訊息填入鼓勵的話
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject: HBD My Friend\n\n {birthday_letter}")
        connection.close()
        # 確認寄出的信件內容
        print(f"SEND EMAIL \n\n {birthday_letter}")
