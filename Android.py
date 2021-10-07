import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'	#To suppress warnings thrown by tensorflow
from time import sleep
import numpy as np
from cv2 import cv2
import pyautogui as pg
import Sudoku_Core as SC
import OCR


s = 513//9	#Size of board//9
fs = 25	#Size of the final image


def getBoard():
	pg.click(266, 740)
	sleep(1)
	pg.click(266, 930)	#Changing the difficulty to expert
	sleep(2)

	image = pg.screenshot(region=(10, 187, 513, 513))
	image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2GRAY)
	_,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

	return image


def readBoard(image):
	for i in range(9):
		for j in range(9):
			subImage = image[i*s + 3: (i+1)*s - 3, j*s + 3: (j+1)*s - 3]	#(+3, -3) is a hack to remove border contours
			contour, _ = cv2.findContours(subImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			if contour != []:
				(x, y, w, h) = cv2.boundingRect(contour[0])
				img = cv2.resize(subImage[y: y+h, x: x+w], (fs, fs), interpolation=cv2.INTER_AREA)				
			else:
				img = np.zeros((fs,fs), dtype='uint8')
			SC.board[i][j] = OCR.model.predict(img.reshape(1, fs, fs, 1)).argmax()


def outputBoard():
	for ((posY, posX), v) in SC.moves.items():
		posX = 42 + posX * 57
		posY = 216 + posY * 57
		pg.moveTo(posX, posY, 0.1)
		pg.click()

		# vX = 42 + 55*(v-1)
		# vY = 843
		# pg.moveTo(vX, vY, 0.1)	#To use the numpad in the app
		# pg.click()
		pg.typewrite(str(v))	#To send numbers from the keyboard


def main():	
	image = getBoard()
	readBoard(image)

	print('Got the board, now solving')
	if SC.solve(0, 0):
		outputBoard()
	else:
		print('Couldn\'t solve')
	
	input('Press any key to exit')

if __name__ == '__main__':
	main()
