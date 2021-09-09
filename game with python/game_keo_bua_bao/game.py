import random

def play():
    computer = random.choice(["keo","bua","bao"])
    player = input("Choice keo hoac bua hoac bao: ")
    if computer == player:
        print("It \'s a tie !")
    if is_win(player,computer):
        print("Yeah. You win!")
    else:
        print("You lost!")

def is_win(player,computer):
    if ((player == "keo" and computer == "bao") or (player == "bao" and computer == "bua") or (player == "bua" and computer == "keo")):
        return True
    return False

play()