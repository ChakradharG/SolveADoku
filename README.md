# Sudoku-Core
A sudoku solver offering multiple ways of solving boards. The core algorithm to solve the board works on a DFS (Depth First Seach) algorithm using recurssion.

## 1. Chrome
Open up sudoku.com and solve a board. Requires Selenium and chrome webdriver.

## 2. Android
Mirror android screen using scrcpy and solve a board in [Sudoku app](https://play.google.com/store/apps/details?id=ee.dustland.android.dustlandsudoku&hl=en). Requires Scrcpy and an android device with usb debugging enabled.

## 3. Terminal
Pass a board through the terminal and display the solution in the terminal. This code takes in 9 lines of 9 integers, each with blanks represented as 0.


## Requirements:
* opencv-python
* pyautogui
* selenium
* tensorflow
* keras
* chrome webdriver
* scrcpy

<br>

(Note: You may need to change the positions of mouse clicks depending upon resolution and position of buttons on screen)