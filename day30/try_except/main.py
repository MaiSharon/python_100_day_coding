import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

""" 使用while處理
hi = True
while hi:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("This not words. Try a agine")
    else:
        print(output_list)
        hi = False
 """


# 使用函數循環處理異常
def fix_not_error():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("This not words. Try a again")
        fix_not_error()
    else:
        print(output_list)


fix_not_error()

