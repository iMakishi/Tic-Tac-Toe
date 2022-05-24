' -------------------- Tic Tac Toe by Maximiliano E.Lutz (iMakishi.) -------------------- '

# Imports -------------------------------------------------- #

import os
import sys
import time
import datetime

from gameArt import gameTitle
from gameArt import gameBoardLayout

from gameText import aboutText
from gameText import helpText

# Side Functions -------------------------------------------------- #

def EXITCountdown(x): # Exit program timer
    total_seconds = x
    while total_seconds > -1:
        timer = datetime.timedelta(seconds = total_seconds)
        print("Exiting in", timer, end = '\r')
        time.sleep(1)
        total_seconds -= 1
    sys.exit()

def RESTART(): # Restart feature.
    restart = input("\n" + "Would you like to go again? (Y/N): > ")
    if restart == "y" or restart == "Y":
        for key in boardKeys:
            gameBoard[key] = " "
        os.system('cls')
        game() # Main Function | Change this line when using this function in other scripts.
    if restart == "n" or restart == "N":
        print("\n" + "Okay. Until next time!")
        timer = 5
        EXITCountdown(int(timer))
    if restart == "" or restart != "y" or restart != "Y" or restart != "n" or restart != "N" or restart.isdigit():
        if restart == "":
            print("\n" + "Input is required to procede.")
        elif restart != "y" or restart != "Y" or restart != "n" or restart != "N":
            if restart.isdigit():
                print("\n" + "Input of numerical type is not accepted." + "\n" + "Please try again.")
            else:
                print("\n" + "Input provided is not accepted." + "\n" + "Please try again.")

        RESTART()

# Parameters -------------------------------------------------- #

exclusiveWords = ["exit", "help", "about"]

gameBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

boardKeys = []

for key in gameBoard:
    boardKeys.append(key)

# GAME Logic -------------------------------------------------- #

def game():
    print(gameTitle)
    print("\033[4mTip: Use the numpad, on the right side of your keyboard, as a guide to play.\033[0m\n")

    turn = 'X'
    count = 0

    for i in range(9):
        gameBoardLayout(gameBoard)

        print("\nIt's your turn Player " + "\033[4m" + turn + "\033[0m")

        move = input("Move to which place?: > ")
        print("")

        while move == "" or move.isalpha() or len(move) > 1:
            if move == "":
                print("\033[4mERROR!\033[0m" + ": Input must be filled to continue.\n")
            if move.isalpha():
                if move in exclusiveWords:
                    if move == "about":
                        print(aboutText)
                    if move == "help":
                        print(helpText)
                    if move == "exit":
                        timer = 5
                        EXITCountdown(int(timer))
                else:
                    print("\033[4mERROR!\033[0m" + ": Alphabetical inputs not allowed.\n")
            if len(move) > 1:
                print("\033[4mERROR!\033[0m" + ": Input length is limited to 1 character only.\n")

            move = input("Move to which place?: > ")
            print("")
        else:
            if gameBoard[move] == ' ':
                gameBoard[move] = turn
                count += 1
            else:
                print("That position is already filled.\n")
                continue

            if count >= 5:
                # Horizontal top
                if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

                # Horizontal middle
                elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

                # Horizontal bottom
                elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

                # Vertical left
                elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

                # Vertical center
                elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

                # Vertical right
                elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

                # Diagonal
                elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

                # Diagonal
                elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ':
                    gameBoardLayout(gameBoard)
                    print("\n" + "\033[4mGAME OVER!\033[0m" + "\n")
                    print("~~~~~ Player " + turn + " won. ~~~~~")
                    break

            if count == 9:
                gameBoardLayout(gameBoard)
                print("\n\033[4mGAME OVER!\033[0m")
                print("It's a Tie!")

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'    

    RESTART()

# Logic RUN -------------------------------------------------- #

if __name__ == '__main__':
    game()