# In this code a user enters some number and it outputs a triangle where the base consists of entered numbers
# and each member in the row above is a sum of two bottom ones (kinda reversed Pascal's triangle with your personal values).
# It is calculated from the top according to member's row (index from 0, descending) and position (index from 0, left to right)
#
# You can see the formula in this repo, name of the img is same as this script's
#
# Author: Atmo88

import math
nums = [int(x) for x in input("Enter numbers, space separated:").split()] # asks user for input, splits number to a list
print(nums) 

def calculateMember(row, position): # calculates each member acording to it's row and position + prints it
  member = 0
  for i in range(row+1): 
  	koeficient = math.factorial(row)/(math.factorial(row-i)*math.factorial(i))
  	member += koeficient*nums[(int(position)+i)]
  return int (member)

for row in reversed(range(len(nums))): # iterating each row, starts on top with descending order
  print(row * "\t", end="") # prints white space at beginning of the row to format triangle
  for position in range(len(nums) - row): # iterating each position, from left, indexing from 0
    member = calculateMember(row, position)
    print(member, "\t\t", end=" ")
  print("\n")# EOL to jump to another row