#! /usr/bin/python2

import os
import random

board = []

## COLOR CODE
# CYAN   = '\033[0;36m'
# RED    = '\033[0;31m'
# WHITE  = '\033[1;37m'
# PURPLE = '\033[0;35m'
# GREEN  = '\033[0;32m'
# RESET  = '\033[0m'


def print_board(board):
    for row in board:
        print (" ".join(row))


def random_row(board):
    return random.randint(0,len(board)-1)


def random_col(board):
    return random.randint(0,len(board[0])-1)


for x in range(0,5):
    board.append(["\033[0;36mO\033[0m"] * 5)

os.system('clear')
print ("Let's play Battleship!")
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

#This prints the ship's location:
#print (ship_row)
#print (ship_col)

turn = 0

while turn < 4:
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        os.system('clear')
        print ("\033[0;32m"+"Congratulations! You sunk my battleship!"+"\033[0m")
        board[guess_row][guess_col] = "\033[0;31mX\033[0m"
        print_board(board)
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            os.system('clear')
            print ("\033[0;34m"+"Oops, that's not even in the ocean."+"\033[0m")
            print_board(board)
        elif (board[guess_row][guess_col] == "\033[1;37m-\033[0m"):
            os.system('clear')
            print ("\033[0;33m"+"You guessed that one already."+"\033[0m")
            print_board(board)
        elif turn == 3:
            os.system('clear')
            print ("\033[0;31m"+"Game Over."+"\033[0m")
            board[guess_row][guess_col] = "\033[1;37m-\033[0m"
            board[ship_row][ship_col] = "\033[0;35mS\033[0m"
            print_board(board)
            break
        else:
            os.system('clear')
            print ("\033[0;34m"+"You missed my battleship!"+"\033[0m")
            board[guess_row][guess_col] = "\033[1;37m-\033[0m"
            print_board(board)
            turn += 1
