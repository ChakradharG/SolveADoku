# SolveADoku
A sudoku solver offering multiple ways of solving boards. The core algorithm to solve the board works on a DFS (Depth First Search) algorithm using recursion.

<br>

## Getting Started
* Clone this repository
* Install the required modules (pip install -r ```Requirements.txt```)
* Download the chrome (or the browser of your choice) webdriver and save it into the same directory as the code
* Download scrcpy on your PC and turn on USB Debugging on your Android Device (So as to mirror your phone's screen on your PC)
* Run ```SolveADoku.py```

<br>

## How to Use
* Run ```SolveADoku.py```and select any of the avaiable options to solve a board
* **Chrome**: Opens up [sudoku.com](https://sudoku.com) using selenium and solves a board
* **Android**: Mirrors android screen using scrcpy and solves a board in the [Sudoku app](https://play.google.com/store/apps/details?id=com.easybrain.sudoku.android&hl=en_IN)
* **Terminal**: Takes a board through the terminal and displays the solution in the terminal. This code takes in 9 lines of 9 integers, each with blanks represented as 0

(Note: You might need to change the positions of mouse clicks depending upon the resolution and position of buttons on screen)
