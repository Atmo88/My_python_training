# input a number and the code tells you whether it's prime or not
# enter any of these "q", "quit", "exit", "cancel" to cancel the program
#
# Author: Atmo88

def isPrime(num):
  if num == 1:  # 1 is not prime by definition
    prime = False
  elif num%2==0: # any even number is not prime
    prime = False
  else:
    prime = True # assumes the number to be prime until it finds a divisor
    for i in range (3,num//2,2): # 1,2 covered above, not necessary to check numbers higher than 
      if num%i == 0:             # a half as the result won't be an integer, odd nums can't be
        prime = False            # divided (/) by an even no, hence step = 2
        break
  return prime

def printPrime(boolPrime):  # prints info acording to the "primeness" of input number
  if boolPrime:
    descriptor = ""
  else:
    descriptor = "not"
  print("This number is", descriptor, "a prime number")

while True:
  entered = input("Enter a number or whether you want to quit :")
  if entered in ["q", "quit", "exit", "cancel"]: # if any of these inputed, shuts down the programm
    break
  else:
    printPrime(isPrime(int(entered)))
