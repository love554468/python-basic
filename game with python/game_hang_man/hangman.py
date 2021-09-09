from word import words
import random
import string 

# print(random.choice(words))
#

def get_valid_word(Words):
    word = " "
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    print(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    live = 3
    while len(word_letter) and live:
        print("="*20)
        # print gues and used_letter 
        print("Nhung chu may vua doan nay: "," ".join(used_letters))
        khong_biet_dat_ten_bien_tn = [letter if letter in used_letters else "-" for letter in word]
        print("processing game: ","".join(khong_biet_dat_ten_bien_tn))
        print("")
        user_letter = input("Please guess a letter from word: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                print("Ya dung roi ne !")
                word_letter.remove(user_letter)
            else:
                print("wrong! rat tiec sai mie roi !")
                live-=1
        elif user_letter in used_letters:
            print("may vua doan xong! Lai chon lai ngu a!")
            live-=1
        else:
            live-=1
            print("invalid character!")
    if not len(word_letter):
        print("yeah dung het mie roi nha suong!")
    else:
        print("Ngu the doan toan sai a")


# print(get_valid_word(words))
hangman()

