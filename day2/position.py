file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

lines = data.splitlines()

position = 0
depth = 0
aim = 0

for line in lines:
    (command, distance) = line.split(" ")
    distance = int(distance)
    if("forward" == command):
        position += distance
        depth += distance * aim
    elif("up" == command):
        aim -= distance
    elif("down" == command):
        aim += distance

print(f'final depth {depth}')
print(f'final position {position}')
print(f'final aim {aim}')
print(f'together {position*depth}')
