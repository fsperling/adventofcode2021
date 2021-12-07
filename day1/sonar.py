
file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

lines = data.split()
increments = 0

for index in range(1, len(lines)-3):
    print(f'sweep: {index+1} is {lines[index+1]} deep')
    print(f'sweep: {index} is {lines[index]} deep')
    window1 = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
    window2 = int(lines[index+1]) + int(lines[index+2]) + int(lines[index+3])
    if ((window2 - window1) > 0):
        increments += 1

print(f'there were {increments} increments')
