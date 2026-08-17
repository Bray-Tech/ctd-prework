import random

#Below is my code for a simple rock, paper, scissors game.
#Game introduction
print('Welcome to the friendly, programmed game of ROSHAMBO!')

print('The rules to the game are simple:')

print('- Rock beats scissors (rock breaks it).')
print('- Scissors beat paper (scissors cut it).')
print('- Paper beats rock (paper covers it).')
print('- If both players show the same sign, it is a tie.')

#Ask user input
user_input = input('Choose between rock, paper, or scissors!')

if user_input == 'rock' or user_input == 'r' or user_input == 'R' or user_input == 'Rock':
	player_move = 'Rock'
elif user_input == 'scissors' or user_input == 's' or user_input == 'S' or user_input == 'Scissors':
	player_move = 'Scissors'
elif user_input == 'paper' or user_input == 'p' or user_input == 'P' or user_input == 'Paper':
	player_move = 'Paper'
else:
	print('Response not valid, rerun program and try again.')
	quit()
	
#Choose from list
choices = ['Rock', 'Paper', 'Scissors']
cpu_move = random.choice(choices)

#Assign game result to variable
if player_move == 'Rock' and cpu_move == 'Rock':
	Result = 0
elif player_move == 'Rock' and cpu_move == 'Scissors':
	Result = 1
elif player_move == 'Rock' and cpu_move == 'Paper':
	Result = -1
elif player_move == 'Scissors' and cpu_move == 'Scissors':
	Result = 0
elif player_move == 'Scissors' and cpu_move == 'Paper':
	Result = 1
elif player_move == 'Scissors' and cpu_move == 'Rock':
	Result = -1
elif player_move == 'Paper' and cpu_move == 'Paper':
	Result = 0
elif player_move == 'Paper' and cpu_move == 'Rock':
	Result = 1
elif player_move == 'Paper' and cpu_move == 'Scissors':
	Result = -1
	
#Result output
if Result == -1:
	print(f'The computer threw {cpu_move} and you threw {player_move}.')
	print('CPU has won.. better luck next time')
elif Result == 0:
	print(f'The computer threw {cpu_move} and you threw {player_move}.')
	print('The result is a tie')
elif Result == 1:
	print(f'The computer threw {cpu_move} and you threw {player_move}.')
	print('Congratulations! You win!!')
