#!/usr/bin/env python

from typing import List, Tuple
from santa_helpers.reader import read
import sys

sys.setrecursionlimit(100)


def solution_1(data: List[str]):
    dataLength = len(data)
    signalLength = len(data[0])

    most_common = [0] * signalLength

    mcResult = ["0"] * signalLength
    lcResult = ["1"] * signalLength

    for signal in data:
        for i in range(0, signalLength):
            if signal[i] == "1":
                most_common[i] += 1
                if most_common[i] > int(dataLength/2):
                    mcResult[i] = "1"
                    lcResult[i] = "0"


    gamma = int(''.join(mcResult), 2)
    epsilon = int(''.join(lcResult), 2)

    print(epsilon * gamma)

def solution_2(data: List[str]):
    most_common, least_common = split(data, 0)

    oxygen = int(filter(most_common, 1, True), 2)
    co2 = int(filter(least_common, 1, False), 2)

    print(oxygen * co2)

def split(data: List[str], index: int) -> Tuple[List[str], List[str]]:
    ones = []
    zeros = []

    for line in data:
        if line[index] == "1":
            ones.append(line)
        else:
            zeros.append(line)

    if len(zeros) > len(ones):
        return zeros, ones
    elif len(zeros) < len(ones):
        return ones, zeros

    return ones, zeros


def filter(data: List[str], index: int, is_most_common: bool):
    most_common, least_common = split(data, index)

    if is_most_common:
        next = most_common
    else:
        next = least_common

    if len(next) == 1:
        return next[0]

    return filter(next, index+1, is_most_common)


lines = read('input', str.strip)

solution_1(lines)
solution_2(lines)
