import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Here we go!!!
a = [0,1,2]
user = int(input("enter your choice from 0, 1 or 2: "))
computer = random.choice(a)
if computer == 0:
  print("computer choice is rock" + rock)
elif computer == 1:
  print("computer choice is paper" + paper)
else:
  print("computer choice is scissors" + scissors)



if user == 0:
  print("your choice is rock" + rock)
elif computer == 1:
  print("your choice is paper" + paper)
else:
  print("your choice is scissors" + scissors)

if computer == 0 and user == 0:
  print("tie")
elif computer == 0 and user == 1:
  print("YOU WIN")
elif computer == 0 and user == 2:
  print("YOU LOOSE")
elif computer == 1 and user == 0:
  print("YOU LOOSE")
elif computer == 1 and user == 1:
  print("tie")
elif computer == 1 and user == 2:
  print("YOU WIN")
elif computer == 2 and user == 0:
  print("YOU WIN")
elif computer == 2 and user == 1:
  print("YOU LOOSE")
elif computer == 2 and user == 2:
  print("tie")
else: 
  print("INVALID!")
