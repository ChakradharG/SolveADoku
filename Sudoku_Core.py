board = [[0 for i in range(9)] for j in range(9)]

#Entering the Board
def input_b():
    for i in range(9):
        board[i] = [int(x) for x in input().split()]

#Displaying the Board
def print_b():
    for i in range(9):
        print(*board[i])

#List Check
def check(d):
    x = d.count(0)
    for i in range(x):
        d.remove(0)
    for j in d:
        if d.count(j)>1:
            return False
    return True

#Check Row
def check_row(r):
    return check(board[r][:])

#Check Column
def check_column(c):
    column = []
    for i in range(9):
        column.append(board[i][c])
    return check(column)

#Check Box
def check_box(r,c):
    box = []
    for i in range(r,r+3):
        for j in range(c,c+3):
            box.append(board[i][j])
    return check(box)

#Placing a Number on the Board
def update(r,c):
    i,j = r,c
    while i < 9:
        while j < 9:
            if board[i][j] == 0:
                for x in range(1,10):
                    board[i][j] = x
                    if check_row(i) and check_column(j) and check_box(i-i%3,j-j%3):
                        if update(i,j):
                            break
                else:
                    board[i][j] = 0
                    return False
                return True
            j += 1
        i += 1
        j = 0
    return True

#Main Function
def main():
    input_b()
    if update(0,0):
        print_b()
    else:
        print('No Solution :(')

#Driver Function
if __name__ == '__main__':
    main()
