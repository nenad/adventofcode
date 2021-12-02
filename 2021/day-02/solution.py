#!/usr/bin/env python

from typing import List, Tuple


def solution_1(directions: List[Tuple]):
    forward, depth = 0, 0
    for item in directions:
        (direction, value) = item
        if direction == "forward":
            forward += value
        elif direction == "up":
            depth -= value
        else:
            depth += value
        
    print(forward*depth)

def solution_2(directions: List[Tuple]):
    forward, depth, aim = 0, 0, 0
    for item in directions:
        (direction, value) = item
        if direction == "forward":
            forward += value
            depth += aim * value
        elif direction == "up":
            aim -= value
        else:
            aim += value
        
    print(forward*depth)

with open('input') as f:
    items = []
    while True:
        line = f.readline()
        if not line:
            break

        direction, value = line.split(" ")
        value = int(value)

        items.append((direction, value))

    solution_1(items)
    solution_2(items)
