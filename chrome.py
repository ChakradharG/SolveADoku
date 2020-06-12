from time import sleep
import numpy as np
from cv2 import cv2
import pyautogui as pg
from selenium import webdriver as wd
import Sudoku_Core as SC


numPos = {1: (940, 370),	#@@
		2: (1050, 370),
		3: (1160, 370),
		4: (940, 460),
		5: (1050, 460),
		6: (1160, 460),
		7: (940, 550),
		8: (1050, 550),
		9: (1160, 550)}


def getBoard():
	pg.hotkey('win', 'UP')	#@@
	pg.click(390, 280)	#@@
	sleep(1)
	image = pg.screenshot()
	image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2GRAY)[252:752, 362:862]	#@@

	return image


def readBoard(image):
	cv2.imwrite('hello.png', image)	#!!
	cv2.waitKey(0)
	for i in range(9):
		n = [int(x) for x in input().split()]
		SC.board[i] = n[:]


def outputBoard():
	for ((posY, posX), v) in SC.moves.items():
		posX = 390 + posX * 55	#@@
		posY = 280 + posY * 55
		pg.click(posX, posY)
		pg.click(numPos[v])


def main():
	driver = wd.Chrome()
	driver.get('https://sudoku.com')
	sleep(3)	#@@

	image = getBoard()
	readBoard(image)
	SC.solve(0, 0)
	outputBoard()
	
	while True:	#!!
		pass
	wd.close()

if __name__ == '__main__':
	main()
