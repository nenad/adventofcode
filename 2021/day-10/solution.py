from typing import List
from santa_helpers.reader import read

def solution(lines: List[str]) -> None:
    corrupted_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    incomplete_scores = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    matches = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    incomplete_lines = []
    sum = 0
    for line in lines:
        stack = []
        for i, char in enumerate(line):
            if char in corrupted_scores:
                if stack[-1] == matches[char]:
                    stack.pop()
                else:
                    sum += corrupted_scores[char]
                    break
            else:
                stack.append(char)

            if i == len(line) - 1 and stack:
                incomplete_lines.append(stack)
                break
    
    print(sum)
    sums = []
    for line in incomplete_lines:
        reversed = line[::-1]
        sum = 0
        for char in reversed:
            sum = (sum*5) + incomplete_scores[char]

        sums.append(sum)

    sums.sort()
    print(sums[round(len(sums)/2)])

data = read('input', str.strip)

solution(data)
