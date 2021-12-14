import sys
from pprint import pprint

class Board:
    def __init__(self):
        self.columns = []
        self.rows = []
        self.column_sums = []
        self.row_sums = []

    def __repr__(self):
        return "'Board: " + "','".join(map(str, self.columns)) + "'"

## import numbers and boards
file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

lines = data.splitlines()
numbers = lines[0].split(',')
numbers = list(map(int, numbers))
boards = []
b = None
for line in lines[1:]:
    if line == "":
        if b:
            boards.append(b)
        b = Board()
        continue
    b.columns.append(list(map(int, line.split())))
boards.append(b)

## create rows
for board in boards:
    for i in range(0, len(board.columns[0])):
        board.rows.append([ row[i] for row in board.columns ])

## calculate sums
for board in boards:
    for i in range(0, len(board.columns)):
        board.column_sums.append(sum(board.columns[i]))
    for i in range(0, len(board.rows)):
        board.row_sums.append(sum(board.rows[i]))

## draw numbers
for number in numbers:
    for board in boards[:]:
        board_removed = False
        for i in range(0, len(board.columns[0])):
            if number in board.columns[i]:
                board.column_sums[i] -= number
                if board.column_sums[i] == 0:
                    if(len(boards) > 1):
                        boards.remove(board)
                        board_removed = True
                        break
                    print(number * sum(board.column_sums))
                    sys.exit(0)
        if not board_removed:
            for i in range(0, len(board.rows[0])):
                if number in board.rows[i]:
                    board.row_sums[i] -= number
                    if board.row_sums[i] == 0:
                        if(len(boards) > 1):
                            boards.remove(board)
                            break
                        print(number * sum(board.column_sums))
                        sys.exit(0)
        board_removed = False
