import cv2
import os
import numpy as np


s = 496//9	#Size of board//9
fs = 25	#Size of the final image


def readIm(name):
	images = [[0 for i in range(9)] for j in range(9)]
	image = cv2.imread(name, 0)
	_,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
	subImage = np.zeros((s, s), dtype='uint8')
	
	for i in range(9):
		for j in range(9):
			subImage = image[i*s + 2: (i+1)*s - 2, j*s + 2: (j+1)*s - 2]	#(+2, -2) is a hack to remove border contours
			contour, _ = cv2.findContours(subImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			if contour != []:
				(x, y, w, h) = cv2.boundingRect(contour[0])
				if h > 2 and w > 2:	#Hack to remove border contours
					img = cv2.resize(subImage[y: y+h, x: x+w], (fs, fs), interpolation=cv2.INTER_AREA)
				else:
					img = np.zeros((fs,fs), dtype='uint8')					
			else:
				img = np.zeros((fs,fs), dtype='uint8')
			images[i][j] = img
	return images


def main():
	log = open('yLog.txt', 'w')
	cnt = 0
	for i in range(5):
		board = []
		for n in range(9):
			board.append([int(x) for x in input().split()])
		images = readIm(f'{i}.png')
		for j in range(9):
			for k in range(9):
				cv2.imwrite(f'{i}_{9*j + k}.png', images[j][k])
				log.write(f'{i}_{9*j + k}.png~{board[j][k]}\n')
				cnt += 1
	print(cnt)


main()
