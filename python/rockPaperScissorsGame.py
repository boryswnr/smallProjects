import random


def game_time(p1, p2):
    beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    print('Computer chose ' + p2 + '.')
    if beats[p1] == p2:
        print('You win!')
    elif beats[p2] == p1:
        print('Computer wins!')
    else:
        print('Tie!')


def computers_choice():
    choices = ['rock', 'paper', 'scissors']
    p2 = random.choice(choices)
    return p2


def players_choice():
    playersChoice = ''
    while playersChoice not in possibleChoices:
        playersChoice = input("Pick your play: 'r' for rock, 'p' for paper or 's' for scissors \n")

    if playersChoice == 'p' or playersChoice == 'P':
        p1 = 'paper'
        print('You chose paper.')
    elif playersChoice == 'r' or playersChoice == 'R':
        p1 = 'rock'
        print('You chose rock.')
    elif playersChoice == 's' or playersChoice == 'S':
        p1 = 'scissors'
        print('You chose scissors.')
    return p1

possibleChoices = ['p', 'P', 'r', 'R', 's', 'S']

print('Welcome to the game of rock, paper, scissors!\n')

while True:
    game_time(players_choice(), computers_choice())
    print('Do you want to play again?')
    playAgain = input("Answer 'y' for 'yes'\n")
    if playAgain == 'y' or playAgain == 'Y':
        continue
    else:
        print('Ok. Bye!')
        break
