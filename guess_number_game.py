# in this code there's a random number between 1 and 9
# your task is to guess the number, with each guess you get a hint whether you are over, under or right dead on the money
# type in "exit" to quit the game and you get your total score of correct hits
# enjoy!
#
# Author: Atmo88

\import random

toGuess = random.randint(1, 9) # initial no. to be guessed
noOfGuesses = 0
playersGuess = None

while True: # gives hints until guessed correctly, then plays again
  playersGuess = input("Please, enter a value between 1 and 9: ")
  if playersGuess == "exit" or not playersGuess: # "exit" or nothing typed in quits the game
    break
  elif playersGuess == str(toGuess):  # if guessed correctly 
    print("Yap, thats the way!!\n")  
    noOfGuesses += 1                  # increases no. of total guesses
    toGuess = random.randint(1, 9)    # and sets new no. to be guessed
  elif int(playersGuess) < toGuess:
    print("Nope, thats too low :(") # gives hints whether the guess is high/low
  else:
    print("Yay, thats over")
print("You got",noOfGuesses,"hits.") # when quiting game, prints amount of total correct guessed
