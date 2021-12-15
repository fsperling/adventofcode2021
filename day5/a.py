from pprint import pprint

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "Line from: " + str(self.start) + " to " + str(self.end)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P-{self.x},{self.y}"

def lineDiagonal(start, end):
    return start.x != end.x and start.y != end.y

def lineVertical(start, end):
    return start.x == end.x

def lineHorizontal(start, end):
    return start.y == end.y


file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

lineCoords = []

for inputline in data.splitlines():
    parts = inputline.split(' ')
    xy1 = parts[0].split(',')
    startPoint = Point(int(xy1[0]), int(xy1[1]))
    xy2 = parts[2].split(',')
    endPoint = Point(int(xy2[0]), int(xy2[1]))
    lineCoords.append(Line(startPoint, endPoint))

ventCoords = {}

for coords in lineCoords:
    if lineDiagonal(coords.start, coords.end):
        pass
        #print(f"discard diagonal line: {coords}")
    elif lineHorizontal(coords.start, coords.end):
        print(f"horizontal line: {coords}")
        start = 0
        end = 0
        if(coords.start.x > coords.end.x):
            start = coords.end.x
            end = coords.start.x
        else:
            start = coords.start.x
            end = coords.end.x
        for i in range(start, end+1):
            if(ventCoords.get(f'P{i}{coords.start.y}')):
                print(f"point: {i},{coords.start.y} already exists: VENT")
                ventCoords[f'P{i}{coords.start.y}'] += 1
            else:
                ventCoords[f'P{i}{coords.start.y}'] = 1
                print(f"adding point: {i},{coords.start.y}")

    elif lineVertical(coords.start, coords.end):
        print(f"vertical line: {coords}")
        start = 0
        end = 0
        if(coords.start.y > coords.end.y):
            start = coords.end.y
            end = coords.start.y
        else:
            start = coords.start.y
            end = coords.end.y
        for i in range(start, end+1):
            if(ventCoords.get(f'P{coords.start.x}{i}')):
                print(f"point: {coords.start.x},{i} already exists: VENT")
                ventCoords[f'P{coords.start.x}{i}'] += 1
            else:
                ventCoords[f'P{coords.start.x}{i}'] = 1
                print(f"adding point: {coords.start.x},{i}")


print(len(ventCoords))

countToAvoid = 0
for value in ventCoords.values():
    if value > 1:
        countToAvoid += 1
print(countToAvoid)

print("not the right solution :-/")
