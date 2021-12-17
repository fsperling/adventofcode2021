from collections import deque

file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
matching = {"(": ")", "[": "]", "{": "}", "<": ">"}
score = 0

for line in data.splitlines():
    stack = deque()

    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            start = stack.pop()
            if matching[start] != char:
                if char == ")":
                    score += 3
                elif char == "]":
                    score += 57
                elif char == "}":
                    score += 1197
                elif char == ">":
                    score += 25137
                break

print(score)
