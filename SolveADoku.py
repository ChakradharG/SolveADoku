import Sudoku_Core as SC


def func1():
	import Browser
	Browser.main()

def func2():
	import Android
	Android.main()

def func3():
	for i in range(9):
		SC.board[i] = [int(x) for x in input().split()]

	print('Got the board, now solving')
	SC.solve(0, 0)
	for i in SC.board:
		print(*i)


ch = input('''Welcome to Sudoku Solver. What would you like to do?
1. Solve a board on Sudoku.com (using Selenium)
2. Solve a board on Android (using Scrcpy)
3. Solve a board passed through the terminal
''')

if ch in [1, 2, 3]:
	exec(f'func{ch}()')
