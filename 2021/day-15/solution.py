from heapq import heapify, heappop, heappush
from types import WrapperDescriptorType
from typing import List, Tuple
from santa_helpers.reader import read
from queue import PriorityQueue
import sys


class Node:
    def __init__(self, x: int, y: int, weight: int) -> 'Node':
        self.x = x
        self.y = y
        self.weight = weight
        self.prev = None
        self.visited = False
        self.distance = sys.maxsize
        self.neighbors = []

    def set_neighbors(self, data_matrix: List[List['Node']]) -> None:
        if self.x-1 >= 0:
            self.neighbors.append(data_matrix[self.x-1][self.y])
        if self.y-1 >= 0:
            self.neighbors.append(data_matrix[self.x][self.y-1])
        if self.x+1 < len(data_matrix):
            self.neighbors.append(data_matrix[self.x+1][self.y])
        if self.y+1 < len(data_matrix):
            self.neighbors.append(data_matrix[self.x][self.y+1])

    def __repr__(self) -> str:
        extra = ''
        if self.prev:
            extra = f'; ({self.prev.x},{self.prev.y}) = {self.distance}'
        return f'({self.x},{self.y}): {self.weight}' + extra

    def __str__(self) -> str:
        return self.__repr__()

    def __lt__(self, other: 'Node'):
        return self.distance < other.distance


def solution(matrix: List[List[Node]]):
    start = matrix[0][0]
    start.distance = 0
    end = matrix[len(matrix[0])-1][len(matrix)-1]

    queue = [start]
    heapify(queue)

    while queue:
        current = heappop(queue)
        current.visited = True

        for node in current.neighbors:
            if node.visited:
                continue
            new_dist = current.distance + node.weight
            if new_dist < node.distance:
                node.distance = new_dist
                node.prev = current
                heappush(queue, node)

    print(end.distance)


def str_to_list(line: str) -> List[Node]:
    line = line.strip()
    return [int(x) for x in line]


data = read('input', str_to_list)
matrix = [[None] * len(data[0]) for _ in range(len(data))]
for x in range(len(data)):
    for y in range(len(data[0])):
        matrix[x][y] = Node(x, y, data[x][y])

new_matrix = []
size = len(matrix)
for x in range(size * 5):
    row = []
    for y in range(size * 5):
        x_add = int(x / size)
        y_add = int(y / size)
        orig_node = matrix[x % size][y % size]
        carry = 1 if orig_node.weight + x_add + y_add > 9 else 0
        new_weight = max(1, (orig_node.weight + x_add + y_add + carry) % 10)

        new_node = Node(x, y, new_weight)
        row.append(new_node)
    new_matrix.append(row)

for x in range(len(data)):
    for y in range(len(data[0])):
        matrix[x][y].set_neighbors(matrix)

for x in range(len(new_matrix)):
    for y in range(len(new_matrix[0])):
        new_matrix[x][y].set_neighbors(new_matrix)

solution(matrix)
solution(new_matrix)
