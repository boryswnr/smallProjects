import random

drawings = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

wordBank = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


def draw_word():
    return random.choice(wordBank)


chosenWord = list(draw_word())

hashedWord = ["_" for i in list(chosenWord)]

triesCounter = 0

for i in range(7):
    print(*hashedWord)
    guessedLetter = input("Type in single letter you think is in the word and confirm with 'enter':\n")
    if guessedLetter in chosenWord:
        instances = [x for x, z in enumerate(chosenWord) if z == guessedLetter]
        for j in instances:
            hashedWord[j] = guessedLetter
    else:
        print(drawings[triesCounter])
        triesCounter += 1





print(chosenWord)
print(hashedWord)
print(*hashedWord)

