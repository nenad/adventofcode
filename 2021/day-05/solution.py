from typing import List, Tuple
from santa_helpers.reader import read


class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


class Segment:
    def __init__(self, begin: Coordinate, end: Coordinate) -> None:
        self.begin = begin
        self.end = end

    def is_straight(self):
        return self.begin.x == self.end.x or self.begin.y == self.end.y

    def points(self) -> List[Coordinate]:
        # 8,0 -> 0,8
        x_range = []
        if self.begin.x <= self.end.x:
            x_range = range(self.begin.x, self.end.x+1)
        else:
            x_range = range(self.begin.x, self.end.x-1, -1)

        y_range = []
        if self.begin.y <= self.end.y:
            y_range = range(self.begin.y, self.end.y+1)
        else:
            y_range = range(self.begin.y, self.end.y-1, -1)

        # In real system this should be Eucledian distance, but our
        # diagonal lines are at 45 degree angles and have the same
        # distance on the x and y axis from the begin and end coordinate.
        coords = []
        if len(x_range) == 1:
            coords = [Coordinate(x_range[0], y) for y in y_range]
        elif len(y_range) == 1:
            coords = [Coordinate(x, y_range[0]) for x in x_range]
        else:
            coords = [Coordinate(x_range[i], y_range[i])
                      for i in range(0, len(x_range))]

        return coords

    def __str__(self) -> str:
        points = ', '.join([str(c) for c in self.points()])
        return f'Begin: {self.begin}\nEnd: {self.end}\nPoints: {points}'


def read_coordinates(line: str) -> Segment:
    # Example row:
    # 0,9 -> 5,9

    begin, end = line.split('->')
    x1, y1 = begin.split(',')
    x2, y2 = end.split(',')
    return Segment(
        Coordinate(int(x1), int(y1)),
        Coordinate(int(x2), int(y2))
    )


def solution(segments: List[Segment]) -> None:
    field = {}

    required_intersections = 2
    intersection_count = 0

    for s in segments:
        for p in s.points():
            key = str(p)
            if key in field:
                field[key] += 1
            else:
                field[key] = 1

            if field[key] == required_intersections:
                intersection_count += 1

    # Debug field
    # for x in range(0, len(field)):
    #     for y in range(0, len(field[0])):
    #         if field[y][x] == 0:
    #             print('.', end='')
    #         else:
    #             print(field[y][x], end='')
    #     print()
    # print()

    print(intersection_count)


allSegments = read('input', read_coordinates)

# Only straight segments (solution 1)
solution([s for s in allSegments if s.is_straight()])

# All segments (solution 2)
solution(allSegments)
