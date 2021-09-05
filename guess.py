#! /usr/bin/python2

from random import randrange

random_number = randrange(1, 10)

count = 0
while count < 3:
    guess = int(input("Enter a guess (1-10): "))
    if guess == random_number:
        print ("You win!")
        break
    count += 1
else:
    print ("You lose. The number was:", random_number)
