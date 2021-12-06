#!/usr/bin/env python

from typing import List
from santa_helpers.reader import read


def solution(fishAges: List[int]) -> None:
    ageBucket = [0] * 9
    for age in fishAges:
        ageBucket[age] += 1

    print(ageBucket)

    generations = 256
    for day in range(0, generations):
        new = ageBucket[0]
        for i in range(0, 8):
            ageBucket[i] = ageBucket[i+1]

        ageBucket[6] += new
        ageBucket[8] = new

        print(f'Day {day}; New: {new}; Total: {sum(ageBucket)}', [f"{i}: {v}" for i, v in enumerate(ageBucket) if v])

    print(sum(ageBucket))
        

line = read('input', str.strip)
data = [int(i) for i in line[0].split(',')]

solution(data)
