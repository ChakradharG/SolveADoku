import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'	#To suppress warnings thrown by tensorflow
from time import sleep
import numpy as np
from cv2 import cv2
import pyautogui as pg
from selenium import webdriver as wd
import Sudoku_Core as SC
import OCR


s = 496//9	#Size of board//9
fs = 20	#Size of the final image
numPos = {1: (940, 370),
		2: (1050, 370),
		3: (1160, 370),
		4: (940, 460),
		5: (1050, 460),
		6: (1160, 460),
		7: (940, 550),
		8: (1050, 550),
		9: (1160, 550)}


def getBoard():
	pg.hotkey('win', 'UP')
	pg.click(460, 220)	#Changing the difficulty to expert
	pg.click(460, 370)
	sleep(2)
	pg.click(390, 280)
	sleep(1)
	image = pg.screenshot(region=(364, 254, 496, 496))
	image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2GRAY)
	_,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

	return image


def readBoard(image):
	for i in range(9):
		for j in range(9):
			subImage = image[i*s + 2: (i+1)*s - 2, j*s + 2: (j+1)*s - 2]	#(+2, -2) is a hack to remove border contours
			contour, _ = cv2.findContours(subImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			if contour != []:
				(x, y, w, h) = cv2.boundingRect(contour[0])
				img = cv2.resize(subImage[y: y+h, x: x+w], (fs, fs), interpolation=cv2.INTER_AREA)				
			else:
				img = np.zeros((fs,fs), dtype='uint8')
			SC.board[i][j] = OCR.model.predict(img.reshape(1, fs, fs, 1)).argmax()


def outputBoard():
	for ((posY, posX), v) in SC.moves.items():
		posX = 390 + posX * 55
		posY = 280 + posY * 55
		pg.click(posX, posY)
		# pg.click(numPos[v])	#To use the numpad on the webpage
		pg.typewrite(str(v))	#To send numbers from the keyboard


def main():
	driver = wd.Chrome()
	driver.get('https://sudoku.com')
	sleep(2)
	
	image = getBoard()
	readBoard(image)
	print('Got the board, now solving')
	SC.solve(0, 0)
	outputBoard()
	
	input('Press any key to exit')
	driver.close()

if __name__ == '__main__':
	main()
