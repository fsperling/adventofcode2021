def isLowpoint(col, row):
    isLow = True
    if(row != 0 and basin[col][row-1] <= basin[col][row]):  #Left
        isLow = False
    if(col != 0 and basin[col-1][row] <= basin[col][row]):  #Top
        isLow = False
    if(col != len(basin)-1 and basin[col+1][row] <= basin[col][row]):  #Right
        isLow = False
    if(row != len(basin[0])-1 and basin[col][row+1] <= basin[col][row]):  #Bottom
        isLow = False
    return isLow

from pprint import pprint
file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

basin = []

for line in data.split():
    basin.append([int(x) for x in str(line)])

lowpoints = []

for col in range(0, len(basin)):
    for row in range(0, len(basin[0])):
        if isLowpoint(col, row):
            lowpoints.append(basin[col][row])

print(sum(lowpoints) + len(lowpoints))
