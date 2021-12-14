from typing import Dict, List
from santa_helpers.reader import read
from operator import itemgetter


def solution(points, splits):
    for axis, fold_val in splits:
        new_points = set()
        for x, y in points:
            point = {'x': x, 'y': y}
            if point[axis] > fold_val:
                point[axis] = 2*fold_val - point[axis]

            new_points.add((point['x'], point['y']))
        points = new_points

    # As the points are a list of tuples, the comparison looks
    # for the first element in the tuple. At the end, the first
    # element of the tuple is returned. Same goes for the second one.
    w = max(points, key=itemgetter(0))[0] + 1
    h = max(points, key=itemgetter(1))[1] + 1

    for y in range(h):
        for x in range(w):
            if (x, y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print()


def get_data(line: str):
    line = line.strip()
    if line.startswith('fold'):
        axis, val = line.split('=')
        axis = axis[-1]
        splits.append((axis, int(val)))
        pass
    elif line.strip() == '':
        return
    else:
        x, y = line.split(',')
        points.add((int(x), int(y)))


points = set()
splits = []
read('input', get_data)

solution(points, splits)
