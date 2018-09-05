import random
import math
import time

def boxCheck(xLoc, yLoc, boxSize):
	return (xLoc // boxSize) * boxSize, (yLoc // boxSize) * boxSize

def printBoard(board, size):
	for b in range(size): #print final board
		for c in range(size):
			if c > 0 and (c+1) % math.sqrt(size) == 0 and c < size - 1:
				print(board[b][c], end=' | ')
			elif c == size - 1:
				print(board[b][c])
			else:
				print(board[b][c], end=' ')
		if b > 0 and (b+1) % math.sqrt(size) == 0 and b < size - 1:
			print('------+-------+------')

digits = [x+1 for x in range(9)]

def generateBoard(digits):
	startTime = time.time()
	gameBoard = [[-1 for x in range(9)] for x in range(9)]
	#digits = [x+1 for x in range(9)]
	size = len(digits)
	x, y = 0, 0
	totalCollisions = 0

	while x < size:
		index = 0 #index of digits list
		random.shuffle(digits)

		while y < size:
			collisions = 0

			#for a in range(size): #prints every addition to board
				#print(gameBoard[a]) 
			
			if (time.time() - startTime) > 0.01:
				return 'nuts' #it broke, gotta retry

			i, j = boxCheck(x, y, math.sqrt(size)) #which 'box' you're currently in

			column = [gameBoard[num][y] for num in range(size)]
			row = [gameBoard[x][num] for num in range(size)]
			box = [gameBoard[int(i+num)][int(j+dum)] for num in range(int(math.sqrt(size))) for dum in range(int(math.sqrt(size)))]

			while digits[(y+index) % size] in column or digits[(y+index) % size] in row or digits[(y+index) % size] in box: 
			#checks if number can be placed there
				totalCollisions += 1
				collisions += 1
				index += 1

				if collisions == size: #means we've iterated through all
				#digits and none fit (due to random chance)
					for e in range(size):
						gameBoard[x][e] = -1 #reset row we're on

					y = 0 
					random.shuffle(digits)
					break
					
			if collisions != size: #fixes some bug i forget lol
				gameBoard[x][y] = digits[(y+index) % size]
				y += 1

		y = 0
		x += 1

	printBoard(gameBoard, size)
	return gameBoard
		
	#print("--- %s seconds ---" % (time.time() - startTime))
	#print(totalCollisions, 'collisions')

def isRemovable(element, digits):
	return None

def removeElements(board, digits):
	size = len(digits)
	for x in range(size):
		for y in range(size):
			i, j = boxCheck(x, y, math.sqrt(size))

			column = [board[num][y] for num in range(size)]
			row = [board[x][num] for num in range(size)]
			box = [board[int(i+num)][int(j+dum)] for num in range(int(math.sqrt(size))) for dum in range(int(math.sqrt(size)))]

			if len(column) == size or len(row) == size or len(box) == size:
				board[x][y] = " "

	print('\n')
	printBoard(board, size)
	return board

board = 'nuts'
while board == 'nuts':
	board = generateBoard(digits)

removeElements(board, digits)