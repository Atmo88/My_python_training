# simple rock, paper scissors game
# asks both player for their choices and prints who is the winner
# when quiting the game, it prints out overall score
#
# Autho: Atmo88

def playerwins(winner): # prints the winner and adds score to overall score
  print("Player " + winner + " wins, congratulations!")
  wins[winner] +=1

win = {"P":"R","R":"S","S":"P"} # returns a value that you beat with your choice
wins = {"A":0,"B": 0} # initial score
choice = {"A": "", "B" : ""} # saves players' choices

while True:
  for player in ["A", "B"]: # asks each player to enter their choice
    choice[player] = input("Player " + player + " please enter you choice. 'P' for paper, 'S' for scissors, 'R' for rock: ") 
  if (any(x not in win for x in choice.values())): # input validation
    print("Invalid input")
  elif choice["A"] == choice["B"]:
    print("It's a draw, play again")
  else:
    playerwins("A" if win[choice["A"]] == choice["B"] else "B") # finds the winner and calls playerwins
  if input("\nPress enter to play again, type N/n to quit:\n") in ["N", "n"]: # asks whether to continue or quit
    print("\nOverall score is:\nPlayer A: " + str(wins["A"]) + "\nPlayer B: " + str(wins["B"]))
    break