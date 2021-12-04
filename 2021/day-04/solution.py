#!/usr/bin/env python

from typing import List, NoReturn, Tuple
from santa_helpers.reader import read


class Board:

    def __init__(self, numbers: List[List[int]]):
        self.unmarkedPoints = sum(sum(numbers, []))
        self.numbers = numbers
        self.rowHits = [0] * 5
        self.colHits = [0] * 5
        self.played = False

    def guess(self, number: int) -> Tuple[bool, int]:
        for i in range(0, 5):
            for j in range(0, 5):
                if self.numbers[i][j] == number:
                    self.rowHits[i] += 1
                    self.colHits[j] += 1
                    self.unmarkedPoints -= number

                    won = self.rowHits[i] == 5 or self.colHits[j] == 5
                    if won:
                        self.played = True

                    return won, self.unmarkedPoints * number

        return False, 0

    def calculateVictory(self, number: int) -> bool:
        for i in range(0, 5):
            for j in range(0, 5):
                if self.numbers[i][j] == number:
                    self.rowHits[i] += 1
                    self.colHits[j] += 1
                    self.unmarkedPoints -= number

                    return self.rowHits[i] == 5 or self.colHits[j] == 5

        return False

    def __str__(self) -> str:
        return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.numbers]) + '\n' + str(self.unmarkedPoints) + '\n'


def read_drawn_numbers(line: str) -> List[int]:
    return [int(i) for i in line.split(',')]


def read_boards(lines: List[str]) -> List[Board]:
    boardRows = []
    boards = []
    for line in lines:
        if not line.strip():
            continue

        boardRows.append([int(i) for i in line.split()])

        if len(boardRows) == 5:
            boards.append(Board(boardRows))
            boardRows = []

    return boards


def solution1(numbers: List[int], boards: List[Board]) -> None:
    for num in numbers:
        for i in range(0, len(boards)):
            won, result = boards[i].guess(num)
            if won:
                print(i, result)
                return


def solution2(numbers: List[int], boards: List[Board]) -> None:
    final = None
    for num in numbers:
        for board in boards:
            if board.played:
                continue

            won, result = board.guess(num)
            if won:
                final = result
                print(board)

    print(final)


lines = read('input', str.strip)

allNumbers = read_drawn_numbers(lines[0])

boards = read_boards(lines[2:])
solution1(allNumbers, boards)

# Boards are mutable, I'm rebuilding them for the second problem.
# Spent too much time debugging this :(
boards = read_boards(lines[2:])
solution2(allNumbers, boards)
