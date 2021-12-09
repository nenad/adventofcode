from typing import List
from santa_helpers.reader import read


def solution1(matrix: List[List[int]]) -> None:
    h = len(matrix)
    w = len(matrix[0])
    low_numbers = 0

    for i in range(h):
        for j in range(w):
            lower_count = 0
            num = matrix[i][j]

            # Left side
            if j == 0 or num < matrix[i][j-1]:
                lower_count += 1

            # Right side
            if j == w-1 or num < matrix[i][j+1]:
                lower_count += 1

            # Top side
            if i == 0 or num < matrix[i-1][j]:
                lower_count += 1

            # Bottom side
            if i == h-1 or num < matrix[i+1][j]:
                lower_count += 1

            if lower_count == 4:
                low_numbers += num + 1

    print(low_numbers)


def solution2(matrix: List[List[int]]) -> None:
    h = len(matrix)
    w = len(matrix[0])

    visited = [[0] * w for _ in range(h)]

    queue = []
    total_basins = []
    for i in range(h):
        for j in range(w):
            if visited[i][j]:
                continue

            if matrix[i][j] == 9:
                continue

            basin = 0
            queue.append([i, j])
            while len(queue) > 0:
                x, y = queue.pop(0)

                if visited[x][y]:
                    continue

                visited[x][y] = 1
                basin += 1

                if x > 0 and not visited[x-1][y]:
                    if matrix[x-1][y] != 9:
                        queue.append([x-1, y])

                if x < h-1 and not visited[x+1][y]:
                    if matrix[x+1][y] != 9:
                        queue.append([x+1, y])

                if y > 0 and not visited[x][y-1]:
                    if matrix[x][y-1] != 9:
                        queue.append([x, y-1])

                if y < w-1 and not visited[x][y+1]:
                    if matrix[x][y+1] != 9:
                        queue.append([x, y+1])

            if basin:
                total_basins.append(basin)

    col = 1
    for n in sorted(total_basins)[-3:]:
        col *= n
    print(col)


def get_input(line: str) -> List[int]:
    return [int(i) for i in [c for c in line.strip()]]


data = read('input', get_input)

solution1(data)
solution2(data)
