def calcDistance(values, startingPoint):
    distance = []
    for value in values:
        distance.append(triangular_number(abs(value - startingPoint)))

    return sum(distance)


def triangular_number(n):
    return n * (n + 1) // 2


def findBestDist(offset, distance):
    while True:
        d = calcDistance(values, startingPoint + offset)

        if d < distance:
            print(f"pos: {startingPoint + offset} has dist {d}")
            optimalPostion = startingPoint + offset
            distance = d
            offset -= 1
        else:
            break


file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

values = data.split(",")
values = list(map(int, values))

startingPoint = round(sum(values)/len(values))
firstDistance = calcDistance(values, startingPoint)
optimalPostion = startingPoint

# try smaller
offset = -1
findBestDist(offset, firstDistance)

# try bigger
offset = 1
findBestDist(offset, firstDistance)

print(calcDistance(values, optimalPostion))
