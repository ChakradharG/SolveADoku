import Sudoku_Core as SC


def func1():
	import Chrome
	Chrome.main()

def func2():
	import Android
	Android.main()

def func3():
	import Arduino
	Arduino.main()

def func4():
	import Webcam
	Webcam.main()

def func5():
	for i in range(9):
		SC.board[i] = [int(x) for x in input().split()]

	print('Got the board, now solving')
	SC.solve(0, 0)
	for i in SC.board:
		print(*i)


ch = input('''Welcome to Sudoku Solver. What would you like to do?
1. Solve a board on Sudoku.com (using Selenium)
2. Solve a board on Android (using Scrcpy)
3. Solve a board on Android (using Arduino)
4. Solve a board on webcam
5. Solve a board passed through the terminal
''')

exec(f'func{ch}()')
