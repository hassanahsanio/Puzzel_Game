# -*- coding: utf-8 -*-
"""Week2(Hassan_ahsan).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZchgCDv1IR2rhvxC5zqWujQmjlCs-2uW

Code with positions as index numbers of List.
"""

print('Intial Postions:-')
positions = '[ 0,   1,   2,   3,   4,   5,   6 ]'
frogs = ['B','B','B','-','G','G','G']
print(frogs)
print(positions)
while 1 :
    #Users input
    print('Press q to quit else or r to reset\nEnter position of piece:')
    pos = input()
    #Validating the moves
    valid_moves = set('qQrR0123456')
    if pos in valid_moves :
      if pos.lower() == 'q':
        print('You have Quitted the Game\nYou Lose')
        break
      elif pos.lower() == 'r':
        pos2=0
        print("Current Positions:-")
        print(positions)
        frogs = ['B','B','B','-','G','G','G']
        print(frogs)
        print('\n')
        continue
      else:
        pos = int(pos)
    else:
      print('Invalid Move\n')
      continue
    #Validating if the current position has frog
    if frogs[pos] == '-':
      print('Invalid Move\n')
      continue
    pos2=0  #Variable is initialized
    if frogs[pos] == 'B':
      if (pos+1) <= 6 and frogs[pos+1] == '-':
        pos2 = pos + 1
      elif pos + 2 <= 6 and frogs[pos + 2] == '-' and frogs[pos + 1] == 'G':
        pos2 = pos + 2
      elif pos + 2 <= 6 and frogs[pos + 2] == '-' and frogs[pos + 1] == 'B':
        pos2 = pos + 2
      else:
        print('Invalid Move\n')
        continue
    elif frogs[pos] == 'G':
      if pos - 1 >= 0 and frogs[pos - 1] == '-':
        pos2 = pos - 1
      elif pos - 2 >= 0 and frogs[pos - 2] == '-' and frogs[pos - 1] == 'B':
        pos2 = pos - 2
      elif pos - 2 >= 0 and frogs[pos - 2] == '-' and frogs[pos - 1] == 'G':
        pos2 = pos - 2
      else:
        print('Invalid Move\n')
        continue

    print('\nCurrent Positions:-')

    frogs[pos], frogs[pos2] = frogs[pos2], frogs[pos]  #Swapping
    print(positions)
    print(frogs)
    print('\n')

    #Condition for winning the game
    if frogs == ['G', 'G', 'G', '-', 'B', 'B', 'B']:
      print(positions)
      print(frogs)
      print("You Win!")
      break

"""Code with positions which are user understandable i.e Easy to understand by avoiding Zero"""

print('Intial Postions:-')
positions = "[ 1,   2,   3,   4,   5,   6,   7 ]"
frogs = ['B','B','B','-','G','G','G']
print(frogs)
print(positions)
while 1 :
    #Users Input
    print('Press q to quit else (or) r to reset\nEnter position of piece:')
    pos = input()
    #Validating the moves
    valid_moves = set('qQrR1234567')
    if pos in valid_moves :
      if pos.lower() == 'q':
        print('You have Quitted the Game\nYou Lose')
        break
      elif pos.lower() == 'r':
        pos2=0
        print("Current Positions:-")
        print(positions)
        frogs = ['B','B','B','-','G','G','G']
        print(frogs)
        print('\n')
        continue
      else:
        pos = int(pos)
    else:
      print('Invalid Move\n')
      continue
    #Validating if the current position has frog
    if frogs[pos-1] == '-':
      print('Invalid Move\n')
      continue
    #Variable is Initialized
    pos2=0
    if frogs[pos-1] == 'B':
      if pos <= 6 and frogs[pos] == '-':
        pos2 = pos
      elif pos + 1 <= 6 and frogs[pos + 1] == '-' and frogs[pos] == 'B':
        pos2 = pos + 1
      elif pos + 1 <= 6 and frogs[pos + 1] == '-' and frogs[pos] == 'G':
        pos2 = pos + 1
      else:
        print('Invalid Move\n')
        continue
    elif frogs[pos-1] == 'G':
      if pos - 2 >= 0 and frogs[pos - 2] == '-':
        pos2 = pos - 2
      elif pos - 3 >= 0 and frogs[pos - 3] == '-' and frogs[pos - 2] == 'G':
        pos2 = pos - 3
      elif pos - 3 >= 0 and frogs[pos - 3] == '-' and frogs[pos - 2] == 'B':
        pos2 = pos - 3
      else:
        print('Invalid Move\n')
        continue

    print("\nCurrent Positions:-")

    #Swapping
    frogs[pos-1], frogs[pos2] = frogs[pos2], frogs[pos-1]
    print(positions)
    print(frogs)
    print('\n')

    #Conditon for winning the game
    if frogs == ['G', 'G', 'G', '-', 'B', 'B', 'B']:
      print(positions)
      print(frogs)
      print("You Win!")
      break