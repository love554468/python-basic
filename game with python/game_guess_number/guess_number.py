import random
def guess_num(x):
    ran_num = random.randint(1,x)
    guess = -1
    while guess != ran_num:
        guess = int(input('Please enter the number you guess:'))
        print(guess)
        if guess > ran_num:
            print("Wrong! Too high.")
        if guess < ran_num:
            print("Wrong! Too low.")
    print(f"Congrate u have find number random {ran_num}")
# guess_num(10)

def computer_guess(x):
    low = 1
    high = x
    guess = random.randint(low,high)
    feedback = ''
    while feedback!='c':
        feedback = input(f"The number {guess} to low (l), too high (h), correct (c): ")
        if feedback=='h':
            guess -=1
        if feedback=='l':
            guess +=1
    print(f"Congrate u! The number is {guess}")

computer_guess(10)

    
