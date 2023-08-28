import smtplib
import random
import datetime as dt


MY_EMAIL = "ppp300a@gmail.com"
EMAIL_PASSWORD ="walcfmofpheqikjh"

def monday_blue_line():
    """隨機選取一則鼓勵的話"""
    with open("quotes.txt", mode="r") as file:
        file_list = file.readlines()
        random_pick_line = random.choice(file_list)
        return random_pick_line


now = dt.datetime.now()
weekday = now.weekday()
is_monday = 6

if weekday == is_monday:
    # 選擇一段鼓勵的話
    fighting_text = monday_blue_line()
    # 發送信件
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
    # 信件訊息填入鼓勵的話
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="ppp300a@yahoo.com.tw",
                        msg=f"Subject: Monday Motivation\n\n{fighting_text}")
    connection.close()
    # 確認寄出的信件內容
    print(fighting_text)




