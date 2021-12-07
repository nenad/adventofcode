#!/usr/bin/env python

from typing import List
from santa_helpers.reader import read


def solution(crabPositions: List[int]) -> None:
    minPos, maxPos = min(crabPositions), max(crabPositions)
    # For now we ignore empty positions if minPos is > 0
    # print(crabPositions)
    crabBuckets = [0] * (maxPos + 1)
    for pos in crabPositions:
        crabBuckets[pos] += 1

    # print(crabBuckets)
    crabDistances = [0] * (maxPos + 1)
    crabDistancesIncrement = [0] * (maxPos + 1)
    for i in range(0, len(crabBuckets)):
        for pos in range(minPos, maxPos+1):
            weight = crabBuckets[pos]
            crabDistances[i] += weight * abs(pos - i)
            crabDistancesIncrement[i] += weight * sum_until(abs(pos - i))

    print("Solution 1:", min(crabDistances))
    print("Solution 2:", min(crabDistancesIncrement))


def sum_until(n: int) -> int:
    return (n*(n+1))/2


line = read('input', str.strip)
data = [int(i) for i in line[0].split(',')]

solution(data)
