from __future__ import print_function

print("Command Line Tic Tac Toe")
board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def printBoard():
	print("")
	for i in range(3):
		for j in range(3):
			print(board[i][j], end="")
			if j < 2:
				print("|", end="")
		# print("")
		if i < 2:
			print("\n-----")
		else:
			print("\n")

def game():
	printBoard()
	while True:
		playerTurn("X")
		playerTurn("O")

def playerTurn(player):
	free = True
	row = vetInput(player, "row")
	col = vetInput(player, "column")
	free = spaceIsFree(row, col)
	while free == False:
		print("Space is occupied!")
		row = vetInput(player, "row")
		col = vetInput(player, "column")
		free = spaceIsFree(row, col)
	board[row-1][col-1] = player
	printBoard()
	if isThreeInRow(player):
		print("{} player wins!".format(player))
		exit()
	elif isCatsGame():
		print("Cat's game!")
		exit()


def vetInput(player, the_type):
	n = raw_input("{} player {}: ".format(player, the_type))
	n = int(n)
	while n == None:
		print("Invalid {}!".format(the_type))
		n = raw_input("{} player {}: ".format(player, the_type))
		n = int(row)
	while numIsValid(n) == False:
		print("Invalid {}!".format(the_type))
		n = raw_input("{} player {}: ".format(player, the_type))
	return n

def spaceIsFree(x, y):
	if board[x-1][y-1] == " ":
		return True
	return False

def numIsValid(n):
	if n < 1 or n > 3:
		return False
	return True

def isThreeInRow(player):
	return horizontalCheck(player) or verticalCheck(player) or diagonalCheck(player)

def diagonalCheck(player):
	return (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (board[0][2] == player and board[1][1] == player and board[2][0] == player)

def horizontalCheck(player):
	return horizontalCheckRecursive(2, 2, player) or horizontalCheckRecursive(1, 2, player) or horizontalCheckRecursive(0, 2, player)

def horizontalCheckRecursive(row, col, player):
	if col == -1:
		return True
	if board[row][col] == player:
		return horizontalCheckRecursive(row, col-1, player)
	else:
		return False

def verticalCheck(player):
	return verticalCheckRecursive(2, 2, player) or verticalCheckRecursive(2, 1, player) or verticalCheckRecursive(2, 0, player)

def verticalCheckRecursive(row, col, player):
	if row == -1:
		return True
	if board[row][col] == player:
		return verticalCheckRecursive(row-1, col, player)
	else:
		return False

def isCatsGame():
	if " " not in board[0] and " " not in board[1] and " " not in board[2]:
		return True
	return False

game()
