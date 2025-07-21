import random as r

ESC = '\x1b'
RED_FG    = ESC + '[31m'
GREEN_FG  = ESC + '[32m'
YELLOW_FG = ESC + '[33m'
WHITE_FG  = ESC + '[37m'

#takes the solution, user's guess, and how many letters were previously correctly guess
def checkword (answer, guess, correct_count):
    #original correct count
    ogcc = correct_count

    #track frequency of letters in the answer
    my_dict = {}
    for char in answer:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

    
    for i in range(5):
        if guess[i] in my_dict:
            #in wordle, correctly guessed letters are green
            if guess[i] == answer[i]:
                print(GREEN_FG + guess[i] + WHITE_FG + "", end = "")
                correct_count += 1
                my_dict[guess[i]] =- 1
            else:
                #correct letters but wrong position are yellow
                if my_dict[guess[i]] > 0:
                    print(YELLOW_FG + guess[i] + WHITE_FG + "", end = "")
                #or else the letter doesn't belong, print it red
                else:
                    print(RED_FG + guess[i] + WHITE_FG + "", end = "")
        #case for the letter not being in the word
        else:
            print(RED_FG + guess[i] + WHITE_FG + "", end = "")
    print(WHITE_FG + "")

    #returns # of correctly guessed letters, 5 being satifactory
    return correct_count-ogcc
            
def main():
    print("red chars are wrong letters, yellow chars are int he wrong spot, green chars are in the correct position")
    correct = False
    wordList = []

    #get word lsit from an official repo
    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()
            wordList.append(word)

    guessWord = wordList[r.randint(0, len(wordList)-1)]

    attempts = 1
    correctNum = 0
    #no more than 6 guesses in the original game of wordle
    while attempts <= 6:
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
        attempts += 1
    print("")
    if correct:
        print('Well done!')
    else:
        print(f"The correct word was: {guessWord}!")
        print('Try again! run "python wordle.py"')
    

main()