from typing import Dict, List
from santa_helpers.reader import read
import itertools

graph = {}
start = 'start'
end = 'end'


def solution1() -> None:
    paths = []
    visited = []
    visit(start, visited, paths)
    print(len(paths))


def solution2() -> None:
    two_visit_caves = [x for x in list(graph.keys()) if x.islower() and x != end and x != start]
    all_paths = []
    for cave in two_visit_caves:
        visited = []
        visit(start, visited, all_paths, cave)

    all_paths.sort()
    all_deduped = list(l for l, _ in itertools.groupby(all_paths))

    print(len(all_deduped))


def visit(dest: str, visited: List[str], all_paths: List[List[str]], double_visit: str = None):
    visited.append(dest)
    if dest == end:
        all_paths.append(visited)
        return

    neighbors = sorted(graph[dest])

    for next in neighbors:
        can_double_visit = True if next == double_visit and visited.count(double_visit) < 2 else False

        if next not in visited or next.isupper() or can_double_visit:
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
