import queue

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

    left = {'row': row-1, 'col': col}
    if(row != 0 and (basin[col][row-1] < 9) and left not in basinPoints):
        queue.put(left)
        basinPoints.append(left)

    top = {'row': row, 'col': col-1}
    if(col != 0 and basin[col-1][row] < 9 and top not in basinPoints):
        queue.put(top)
        basinPoints.append(top)

    right = {'row': row, 'col': col+1}
    if(col != len(basin)-1 and basin[col+1][row] < 9 and right not in basinPoints):
        queue.put(right)
        basinPoints.append(right)

    bottom = {'row': row+1, 'col': col}
    if(row != len(basin[0])-1 and basin[col][row+1] < 9 and bottom not in basinPoints):
        queue.put(bottom)
        basinPoints.append(bottom)


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
            lowpoints.append({"row": row, "col": col})

basinSizes = []

for lowpoint in lowpoints:
    basinPoints = []
    basinSearch = queue.Queue()
    basinSearch.put(lowpoint)

    while(basinSearch.qsize() > 0):
        nextPoint = basinSearch.get()
        findNeighborPoints(nextPoint, basinPoints, basinSearch)

    basinSizes.append(len(basinPoints))

basinSizes.sort()
print(basinSizes[-1] * basinSizes[-2] * basinSizes[-3])
