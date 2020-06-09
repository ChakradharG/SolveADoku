def checkList(l):
	numCnt = {0:0}
	for i in l:
		numCnt[i] = numCnt.get(i, 0) + 1
	del numCnt[0]
	for i in numCnt.values():
		if i > 1:
			return False
	return True


def checkRow(r):
	return checkList(board[r][:])


def checkCol(c):
	column = []
	for i in range(9):
		column.append(board[i][c])
	return checkList(column)


def checkBox(r,c):
	box = []
	for i in range(r,r+3):
		for j in range(c,c+3):
			box.append(board[i][j])
	return checkList(box)


def solve(r,c):
	i,j = r,c
	while i < 9:
		while j < 9:
			if board[i][j] == 0:
				for x in range(1,10):
					board[i][j] = x
					if checkRow(i) and checkCol(j) and checkBox(i-i%3,j-j%3):
						if solve(i,j):
							break
				else:
					board[i][j] = 0
					return False
				return True
			j += 1
		i += 1
		j = 0
	return True
