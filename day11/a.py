import numpy
from collections import deque
from pprint import pprint

class Octopus:
    def __init__(self, x, y, energylevel):
        self.x = x
        self.y = y
        self.energylevel = energylevel
        self.neighbors = []

    def __str__(self):
        pass
        #return f"{self.x},{self.y}: {self.energylevel}"


file_path = "testinput.txt"
with open(file_path, 'r') as f:
    data = f.read()

cavern = [[None]*10]*10
pprint(cavern)

y = 0
for line in data.splitlines():
    print(line)
    if not line:
        break

    x = 0
    for char in line:
        cavern[y][x] = Octopus(x, y, int(char))
        x += 1
    y += 1

print()
for i in range(0, len(cavern)):
    for j in range(0, len(cavern[0])):
        print(cavern[i][j].energylevel, end='')
    print()

pprint(cavern)
