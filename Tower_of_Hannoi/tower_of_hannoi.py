'''
Author: Varun Subramanya
Date: March 15 2019

Keywords: Classes, Objects, Stacks, Linear Datastructures, Problem Solving.

'''








from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
right_stack = Stack("Right")
middle_stack = Stack("Middle")

stacks.append(left_stack)
stacks.append(right_stack)
stacks.append(middle_stack)

#print(stacks)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
  for disk in range(num_disks, 0, -1):
    left_stack.push(disk)
  left_stack.print_items()
    

num_optimal_moves = (2**num_disks) - 1 
print ("\nThe fastest you can solve this game is in {} moves". format(num_optimal_moves))
 
#Get User Input
def get_input():
  
  choices = [stack.get_name[0] for stack in stacks]
  
  while True:
    
    for i in range(len(stacks)):
      
      
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}". format(letter, name))
      user_input = input("")
      if user_input in choices:
        
        
        for i in range(len(stacks)):
          
          return 	stacks[i]

        #Play the Game
'''
num_user_moves = 0

while right_size.get_size() != num_disks:
  
  print ("n\n\n....Current Stacks...")
  for stack in stacks:
    stack.print_items()
    
  while True:
    print ("\n Which Stack do you want to move from?\n")
    from_stack = get_input()
    print("\n Which stack do you want to move to?\n")
    to_stack = get_input()
    
    if from_size.get_size() == 0:
      print("n\n Invalid Move. Try Again")
    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break 
    else:
      print("\n\n Invalid Move. Try again")
      
print("\n\n You completed the game in {0} moves, and the optimal number of moves is {1}". format(num_moves, num_optimal_moves))
'''

    