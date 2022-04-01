import random
from hangmanAssets import wordBank, drawings

chosenWord = list(random.choice(wordBank))
hashedWord = ["_" for i in chosenWord]
failedTries = 0
numOfRounds = 1
triedLetters = []

print("Category: animals.")

# The game itself
while failedTries != 7:
    print(f"|||||||||||\n||ROUND {numOfRounds}||\n|||||||||||")
    print("Tried letters:")
    print(*triedLetters, sep=", ")
    print(*hashedWord)
    guessedLetter = input("Type in single letter you think is in the word and confirm with 'enter':\n").lower()
    if guessedLetter in triedLetters:
        print("You already tried that one.")
        continue
    else:
        triedLetters.append(guessedLetter)
    if guessedLetter in chosenWord:
        instances = [x for x, z in enumerate(chosenWord) if z == guessedLetter]
        for j in instances:
            hashedWord[j] = guessedLetter
    else:
        print(drawings[failedTries])
        failedTries += 1
    numOfRounds += 1
    if "_" not in hashedWord:
        break

if failedTries == 7:
    print("Sorry, you lost.")
    print("You were looking for a word", "".join(chosenWord))
else:
    print(*hashedWord)
    print("GG, you've won.")
