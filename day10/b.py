from collections import deque
from pprint import pprint

file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
matching = {"(": ")", "[": "]", "{": "}", "<": ">"}

scores = []

for line in data.splitlines():
    stopline = False
    score = 0
    stack = deque()

    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            start = stack.pop()
            if matching[start] != char:
                stopline = True
                break

    if stopline:
        continue

    while(stack):
        char = stack.pop()
        missing = matching[char]
        score *= 5

        if missing == ")":
            score += 1
        elif missing == "]":
            score += 2
        elif missing == "}":
            score += 3
        elif missing == ">":
            score += 4

    scores.append(score)

scores.sort()
print(scores[round(len(scores)/2)])
