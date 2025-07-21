import random as r

ESC = '\x1b'
RED_FG    = ESC + '[31m'
GREEN_FG  = ESC + '[32m'
YELLOW_FG = ESC + '[33m'
WHITE_FG  = ESC + '[37m'

def checkword (answer, user, correct_count):
    ogcc = correct_count
    my_dict = {}
    for char in answer:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    for i in range(5):
        if user[i] in my_dict:
            if user[i] == answer[i]:
                print(GREEN_FG + user[i] + WHITE_FG + "", end = "")
                correct_count += 1
                my_dict[user[i]] =- 1
            else:
                if my_dict[user[i]] > 0:
                    print(YELLOW_FG + user[i] + WHITE_FG + "", end = "")
                else:
                    print(RED_FG + user[i] + WHITE_FG + "", end = "")
        else:
            print(RED_FG + user[i] + WHITE_FG + "", end = "")
    print(WHITE_FG + "")
    return correct_count-ogcc
            
def main():
    print("red chars are wrong letters, yellow chars are int he wrong spot, green chars are in the correct position")
    correct = False
    wordList = []

    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()
            wordList.append(word)

    guessWord = wordList[r.randint(0, len(wordList)-1)]
    i = 0
    correctNum = 0
    while i < 6:
        print(" ")
        guess = str(input("Enter your guess for this wordle game:\t"))
        while guess not in wordList:
            print("")
            print("Please use one of the valid words!")
            print("")
            guess = str(input("Enter your guess for this wordle game:\t"))
        print("")
        correctNum = checkword(guessWord, guess, correctNum)
        if correctNum > 4:
            correct = True
            break
        i = i + 1
    print("")
    if correct:
        print('Well done!')
    else:
        print(f"The correct word was: {guessWord}!")
        print('Try again! run "wordle.py"')
    

main()

# from colorama import Fore
# print(Fore.RED + 'some red text')
#print(Style.RESET_ALL)
