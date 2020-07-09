import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'	#To suppress warnings thrown by tensorflow
import numpy as np
from cv2 import cv2
import Sudoku_Core as SC
import OCR
from ppadb.client import Client
import serial
from time import sleep

# device = Client(host='127.0.0.1', port=5037).devices()[0]	#Android device connection through ADB
serialPort = serial.Serial(
	port = 'COM8', baudrate = 9600, 
	bytesize = 8, timeout = 2, 
	stopbits = serial.STOPBITS_ONE)	#Serial communication with arduino


s = 711//9	#Size of board//9
fs = 20	#Size of the final image


def getBoard():
	with open('Screen.png', 'wb') as file:
		file.write(device.screencap())	#Taking a screenshot

	image = cv2.imread('Screen.png', 0)[257:968, 4:715]
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
	serialPort.write(bytes(f'{len(SC.moves)}\n', 'ascii'))
	for ((posY, posX), v) in SC.moves.items():
		serialPort.write(bytes(f'{posX}{posY}{v}\n', 'ascii'))
		print(f'{posX}{posY}{v}')
		sleep(1)


def main():	
	# image = getBoard()
	# readBoard(image)

	print('Got the board, now solving')
	# SC.solve(0, 0)
	SC.moves = {(8, 8): 2, (8, 7): 4, (8, 6): 6, (8, 5): 1, (8, 4): 3, (8, 3): 5, (8, 2): 8, (8, 1): 7, (8, 0): 9}
	outputBoard()
	
	input('Press any key to exit')

if __name__ == '__main__':
	main()
