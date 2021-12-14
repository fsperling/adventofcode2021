import queue
from pprint import pprint


def isLowpoint(col, row):
    # print(f"col: {col} : row {row} : value: {basin[col][row]}")
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

def findNeighborPoints(point, basinPoints, queue):
    row = point['row']
    col = point['col']

    if(row != 0 and (basin[col][row-1] < 9) and {'row': row-1, 'col': col} not in basinPoints):  #Left
        queue.put({'row': row-1, 'col': col})
        basinPoints.append({'row': row-1, 'col': col})
    if(col != 0 and basin[col-1][row] < 9 and {'row': row, 'col': col-1} not in basinPoints):  #Top
        queue.put({'row': row, 'col': col-1})
        basinPoints.append({'row': row, 'col': col-1})
    if(col != len(basin)-1 and basin[col+1][row] < 9 and {'row': row, 'col': col+1} not in basinPoints):  #Right
        queue.put({'row': row, 'col': col+1})
        basinPoints.append({'row': row, 'col': col+1})
    if(row != len(basin[0])-1 and basin[col][row+1] < 9 and {'row': row+1, 'col': col} not in basinPoints):  #Bottom
        queue.put({'row': row+1, 'col': col})
        basinPoints.append({'row': row+1, 'col': col})


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
            # print(f"found lowpoint at {col, row, basin[col][row]}")
            lowpoints.append({"row": row, "col": col})

print(lowpoints)

basinSizes = []

for lowpoint in lowpoints:
    basinPoints = []
    basinSearch = queue.Queue()
    basinSearch.put(lowpoint)

    while(basinSearch.qsize() > 0):
        nextPoint = basinSearch.get()
        print(f"now {nextPoint}")
        findNeighborPoints(nextPoint, basinPoints, basinSearch)
        print(f"{lowpoint} - {basinSearch} - {basinPoints}")

    basinSizes.append(len(basinPoints))
    print(len(basinPoints))

basinSizes.sort()
print(basinSizes[-1] * basinSizes[-2] * basinSizes[-3])
