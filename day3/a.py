file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

lines = data.split()
digits = len(lines[0])
mostcommon = ""
leastcommon = ""

for digit in range(0, digits):
    ones = 0
    zeroes = 0
    for i in range(0, len(lines)-1):
        print(f"line {i}")
        if("1" == lines[i][digit]):
            ones += 1
        if("0" == lines[i][digit]):
            zeroes += 1

    print(f"ones {ones}")
    print(f"zeroes {zeroes}")

    if(ones > zeroes):
        mostcommon += "1"
        leastcommon += "0"
    else:
        leastcommon += "1"
        mostcommon += "0"

print(f"most: {mostcommon} or {int(mostcommon, 2)}")
print(f"least: {leastcommon} or {int(leastcommon, 2)}")
print(f"power consumption: {int(mostcommon, 2) * int(leastcommon, 2)}")
