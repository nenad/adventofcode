from santa_helpers.reader import read


class Rect:
    def __init__(self, x1: int, x2: int, y1: int, y2: int) -> None:
        if x1 > x2:
            x2, x1 = x1, x2
        if y1 < y2:
            y2, y1 = y1, y2

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def in_width(self, x: int) -> bool:
        return x >= self.x1 and x <= self.x2

    def in_height(self, y: int) -> bool:
        return y >= self.y1 and y <= self.y2

    def in_box(self, x: int, y: int) -> bool:
        return x >= self.x1 and x <= self.x2 and y >= self.y2 and y <= self.y1

    def __repr__(self) -> str:
        return f'x={self.x1}..{self.x2} y={self.y1}..{self.y2}'


def nsum(n: int) -> int:
    return (n*(n+1))/2


def solution1(rect: Rect) -> None:
    # For this part we only need y2 coordinate
    # A good explanation why is this solution here:
    # https://github.com/prendradjaja/advent-of-code-2021/blob/main/17--trick-shot/a.py

    max_y = -rect.y2 - 1

    print(nsum(max_y))


def solution2(rect: Rect) -> None:
    hits = 0
    for x in range(0, rect.x2 + 1):
        for y in range(rect.y2, -rect.y2):
            if is_hit(x, y, rect):
                hits += 1
    print(hits)


def is_hit(x: int, y: int, rect: Rect) -> bool:
    max_y = rect.y2
    dist_x = x
    dist_y = y
    while dist_y >= max_y:
        if rect.in_box(dist_x, dist_y):
            return True

        y -= 1
        x = max(0, x-1)
        dist_x += x
        dist_y += y

    return False


def get_rect(line: str):
    line = line[13:]
    w, h = line.split(', ')
    x1, x2 = w[2:].split('..')
    y1, y2 = h[2:].split('..')
    return Rect(int(x1), int(x2), int(y1), int(y2))


rect = read('input', get_rect)[0]

solution1(rect)
solution2(rect)
