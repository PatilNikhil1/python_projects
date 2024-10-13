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

# user input
a = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

# print shape as per user input 
if a == 0:
    print(rock)
elif a == 1:
    print(paper)
elif a == 2:
    print(scissors)
else:
    print('You typed an invalid number, you lose!')

# show computer
print('Computer chose:')

# creating list
b = [rock,paper,scissors]

# showing computer input 
c = random.choice(b)
print(c)


# printing result as per condition
if  a == 0 and c == rock:
    print("It's a draw")
elif  a == 1 and c == paper:
    print("It's a draw")
elif  a == 2 and c == scissors:
    print("It's a draw")

elif  a == 0 and c == paper:
    print('You lose')
elif a == 1 and c == scissors:
    print('You lose')
elif a == 2 and c == rock:
    print('You lose')

elif a == 0 and c == scissors:
    print('You win!')
elif a == 1 and c == rock:
    print('You win!')
elif a == 2 and c == paper:
    print('You win!')

