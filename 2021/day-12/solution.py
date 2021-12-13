from typing import Dict, List
from santa_helpers.reader import read
from collections import Counter

graph = {}
start = 'start'
end = 'end'


def solution1() -> None:
    paths = []
    visited = []
    visit(start, visited, paths)
    print(len(paths))


def solution2() -> None:
    paths = []
    visited = []
    visit(start, visited, paths, True)
    print(len(paths))


def visit(dest: str, visited: List[str], all_paths: List[List[str]], double_visit: bool = False):
    visited.append(dest)
    if dest == end:
        all_paths.append(visited)
        return

    neighbors = sorted(graph[dest])
    for next in neighbors:
        if next == 'start':
            continue

        small_caves = [x for x in visited if x not in ['start', 'end'] and x.islower()]
        can_double_visit = double_visit and len(Counter(small_caves)) == len(small_caves)
        if can_double_visit or next.isupper() or next not in visited:
            visit(next, visited.copy(), all_paths, double_visit)

    return all_paths


def add_to_graph(line: str) -> None:
    start, end = line.strip().split('-')
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []

    graph[start].append(end)
    graph[end].append(start)


read('input', add_to_graph)

solution1()
solution2()
