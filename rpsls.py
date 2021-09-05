#! /usr/bin/python2

import random


def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissor'
    else:
        print number, "is not a valid number!"
    return name


def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissor':
        number = 4
    else:
        print name, "is not a valid name!"
    return number


def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5)
    winner = (player_number - comp_number) % 5

    if winner == 0:
        winner = "Player and computer tie!\n"
    elif winner == 1:
        winner = "Player wins!\n"
    elif winner == 2:
        winner = "Player wins!\n"
    elif winner == 3:
        winner = "Computer wins!\n"
    else:
        winner = "Computer wins!\n"

    comp_number = number_to_name(comp_number)

    print "Player chooses", name
    print "Computer chooses", comp_number
    print winner


## test your code
#rpsls("rock")
#rpsls("spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissor")

print ("Rock Paper Scissor Lizard Spock")
player_input = raw_input("Your choice: ")
player_choice = player_input.lower()
rpsls(player_choice)
