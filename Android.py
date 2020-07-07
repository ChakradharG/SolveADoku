import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'	#To suppress warnings thrown by tensorflow
import numpy as np
from cv2 import cv2
import pyautogui as pg
import Sudoku_Core as SC
import OCR


s = 522//9	#Size of board//9
fs = 20	#Size of the final image
numPos = {1: (90, 760),
		2: (175, 760),
		3: (260, 760),
		4: (345, 760),
		5: (430, 760),
		6: (90, 845),
		7: (175, 845),
		8: (260, 845),
		9: (345, 845)}


def getBoard():
	image = pg.screenshot(region=(5, 165, 522, 522))
	image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2GRAY)
	_,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

	pixels = image.flatten()
	#Checking if the background is white, and if so, inverting the background and the foreground
	if np.count_nonzero(pixels == 0) < np.count_nonzero(pixels == 255):
		_, image = cv2.threshold(baseIm, 127, 255, cv2.THRESH_BINARY_INV)

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
		posX = 35 + posX * 58
		posY = 195 + posY * 58
		pg.moveTo(posX, posY, 0.1)
		pg.click()
		pg.moveTo(numPos[v][0], numPos[v][1], 0.1)
		pg.click()


def main():	
	image = getBoard()
	readBoard(image)

	print('Got the board, now solving')
	SC.solve(0, 0)
	outputBoard()
	
	input('Press any key to exit')

if __name__ == '__main__':
	main()
