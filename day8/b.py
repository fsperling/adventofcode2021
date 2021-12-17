from pprint import pprint

def removeChars(orig, chars):
    for ch in chars:
        if ch in orig:
            orig = orig.replace(ch, '')
    return orig


def decode(patterns):
    map = {}
    for pattern in patterns:
        if len(pattern) == 2:
            map[pattern] = 1
            one = pattern
        elif len(pattern) == 3:
            map[pattern] = 7
        elif len(pattern) == 4:
            map[pattern] = 4
            four = pattern
        elif len(pattern) == 7:
            map[pattern] = 8

    fiveSegments = [p for p in patterns if(len(p) == 5)]
    sixSegments = [p for p in patterns if(len(p) == 6)]

    for number in sixSegments:
        if(len(removeChars(number,four)) == 2):
            map[number] = 9
            nine = number
            sixSegments.remove(number)

    for number in sixSegments:
        if(len(removeChars(number, one)) == 4):
            map[number] = 0
            sixSegments.remove(number)

    map[sixSegments[0]] = 6

    for number in fiveSegments:
        if(len(removeChars(number, one)) == 3):
            map[number] = 3
            fiveSegments.remove(number)

    for number in fiveSegments:
        if(len(removeChars(number, nine)) == 0):
            map[number] = 5
            fiveSegments.remove(number)

    map[fiveSegments[0]] = 2
    return map


file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

sum = 0
for line in data.splitlines():
    input = line.split("|")
    signalpatterns = input[0].split()
    digits = input[1].split()

    signalpatterns = [''.join(sorted(str)) for str in signalpatterns]
    digits = [''.join(sorted(str)) for str in digits]

    numbermap = decode(signalpatterns)
    number = numbermap[digits[0]] * 1000 + numbermap[digits[1]] * 100 + numbermap[digits[2]] * 10 + numbermap[digits[3]]
    sum += number

print(sum)
