from typing import Any, Callable, List

def return_string(line: str):
    return line

def read(filename: str, op: Callable[[str], Any] = return_string) -> List:
    data = []
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break

            data.append(op(line))

    return data
