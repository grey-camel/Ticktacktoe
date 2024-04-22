#!/bin/python3
from random import randrange



board = [['1','2','3'],
	 ['4','5','6'],
	 ['7','8','9']]


def display_board(board):
	for row in board:
		print("+-------+-------+-------+")
		print("|       |       |       |")
		print("|   " + "   |   ".join(row) + "   |")
		print("|       |       |       |")
	print("+-------+-------+-------+")	

def make_list_of_free_fields(board):
	free_fields = []
	for row in board:
		for column in row:
			if column != "X" and column != "0":
				freetup = (board.index(row), row.index(column))
				free_fields.append(freetup)
			
	return free_fields
	

def enter_move(board):
	while True:
		user_move = str(input("Enter whhich box you wish to select: "))	
		change_made = False
		for row in board:
			for column in row:
				if user_move == column and user_move != "0" and column != "0" and column != "X":
					board[board.index(row)][row.index(column)] = "0"
					change_made = True
		if change_made:
			return board
		else:
			print('Invalid input, please try again.')
			

def draw_move(board):
	status_check = make_list_of_free_fields(board)
	print(status_check)
	center = (1,1)
	if center in status_check:
		board[1][1] = "X"
		return board
	
	while True:
		comp_move = randrange(0,len(status_check))
		change_mode = False
		drawingmove = status_check[comp_move]
		if drawingmove != ('x','x'):
			board[drawingmove[0]][drawingmove[1]] = "X" 
			return board
			
def victory(board, sign):
	space = make_list_of_free_fields(board)
	free = len(space)
	if free >=1:
		if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
			if sign == "0":
				print("You have won!")

				return False
			elif sign == "X":
				print("The Computer has won, sorry.")

				return False
		if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
			if sign == "0":
				print("You have won!")

				return False
			elif sign == "X":
				print("The Computer has won, sorry.")

				return False	
		if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
			if sign == "0":
				print("You have won!")

				return False
			elif sign == "X":
				print("The Computer has won, sorry.")

				return False
		if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
			if sign == "0":
				print("You have won!")

				return False
			elif sign == "X":
				print("The Computer has won, sorry.")

				return False
		if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
			if sign == "0":
				print("You have won!")

				return False
			elif sign == "X":
				print("The Computer has won, sorry.")

				return False
		if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
			if sign == "0":
				print("You have won!")

				return False
			elif sign == "X":
				print("The Computer has won, sorry.")

				return False
		if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
			if sign == "0":
				print("You have won!")

				return False
			elif sign == "X":
				print("The Computer has won, sorry.")
				
				return False
		if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
			if sign == "0":
				print("You have won!")
				
				return False
			elif sign == "X":
				print("The Computer has won, sorry.")
				
				return False
	elif free == 0:
		print("The Game is Tied!")
		return False
	else:
		return True



print("Welcome to ticktacktoe, lets begin")
while True:

	draw_move(board)
	display_board(board)

	if victory(board, "0") == False or victory(board, "X") == False:
		display_board(board)
		break
	enter_move(board)
	if victory(board, "0") == False or victory(board, "X") == False:
		display_board(board)
		break
	else:
		continue
