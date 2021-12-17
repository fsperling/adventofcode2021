file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

count1478 = 0
for line in data.splitlines():
    input = line.split("|")
    digits = input[1].split()

    for digit in digits:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            count1478 += 1

print(count1478)
