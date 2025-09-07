#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["thing 1", "thing 2", "thing 3", "thing 4", "thing 5", "thing 6", "thing 7", "thing 8", "thing 9", "thing 10", "thing 11", "thing 12"]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length
  
  r = int(r) #cut off any decimal values

  print(r)
  response = answers[r]
  print(response)
if __name__ == '__main__':
  main()
