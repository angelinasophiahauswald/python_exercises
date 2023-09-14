import random

def guessing_number(num, ran):
    num = int(num)
    if num == ran:
        print("Correct.")
        print("Do you want to play again? Either type YES or NO")
        another_round = input()
        if another_round == "YES":
            new_ran = random.randint(0,100)
            iniciate_game(new_ran)
        elif another_round == "NO":
            print("Bye bye.")
            exit()
        else:
            print("You didn't say YES or NO, exiting the game.")
            exit()
    elif num < ran:
        return "Number was too low."
    elif num > ran:
        return "Number was too high."
    else:
        return "weird"

def iniciate_game(ran):
    for i in range(0,5):
        print("Guess a number")
        num = input()
        print(guessing_number(num, 3))

if __name__ == "__main__":
    ran = random.randint(0,100)
    iniciate_game(ran)
    