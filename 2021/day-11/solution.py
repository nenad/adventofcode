from typing import List
from santa_helpers.reader import read


def solution(matrix: List[List[int]]) -> None:
    h = len(matrix)
    w = len(matrix[0])
    flashes = 0

    cycle = 0
    while True:
        already_flashed = {}
        flash_queue = []
        # Bump every octopus
        for i in range(h):
            for j in range(w):
                matrix[i][j] += 1
                if matrix[i][j] > 9:
                    already_flashed[f'{i},{j}'] = True
                    flash_queue.append([i, j])

        while flash_queue:
            if len(already_flashed) == w*h:
                print("Solution 2:", cycle+1)
                return

            flashes += 1
            i, j = flash_queue.pop(0)
            matrix[i][j] = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    x = i+ii
                    y = j+jj
                    key = f'{x},{y}'
                    if key in already_flashed:
                        continue

                    if x >= 0 and x < h and y >= 0 and y < w:
                        matrix[x][y] += 1
                        if matrix[x][y] > 9 and key not in already_flashed:
                            already_flashed[key] = True
                            flash_queue.append([x, y])

        cycle += 1
        if cycle == 100:
            print("Solution 1:", flashes)


def str_list(line: str) -> List[int]:
    return [int(char) for char in line.strip()]


data = read('input', str_list)

solution(data)
