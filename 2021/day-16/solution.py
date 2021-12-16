from typing import List, Tuple
from santa_helpers.reader import read

hex_map = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

op_map = {
    0: 'sum',
    1: 'product',
    2: 'min',
    3: 'max',
    4: 'return',
    5: 'gt',  # always two subpackets
    6: 'lt',  # always two subpackets
    7: 'eq'  # always two subpackets
}


class Packet:
    def __init__(self, version: int, type: int, payload) -> None:
        self.root = False
        self.version = version
        self.type = type
        self.payload = payload
        self.children = []

    def __repr__(self) -> str:
        return f'#{self.type} = {self.version}'

    def __str__(self) -> str:
        return self.__repr__()


def solution(binary: str):
    root = Packet(-1, -1, -1)
    root.root = True

    get_packets(binary, root)
    root = root.children[0]  # get the first child, there must be one

    version_sum = 0
    queue = [root]
    while queue:
        current = queue.pop(0)
        version_sum += current.version
        for c in current.children:
            queue.append(c)
    
    print("Solution 1: ", version_sum)
    print("Solution 2: ", traverse(root))


def traverse(node: Packet) -> int:
    if op_map[node.type] == 'return':
        return node.payload

    if op_map[node.type] == 'sum':
        result = 0
        for c in node.children:
            result += traverse(c)
        return result

    if op_map[node.type] == 'product':
        result = 1
        for c in node.children:
            result *= traverse(c)
        return result

    if op_map[node.type] == 'max':
        numbers = []
        for c in node.children:
            numbers.append(traverse(c))
        return max(numbers)

    if op_map[node.type] == 'min':
        numbers = []
        for c in node.children:
            numbers.append(traverse(c))
        return min(numbers)

    if op_map[node.type] == 'eq':
        return 1 if traverse(node.children[0]) == traverse(node.children[1]) else 0

    if op_map[node.type] == 'lt':
        return 1 if traverse(node.children[0]) < traverse(node.children[1]) else 0

    if op_map[node.type] == 'gt':
        return 1 if traverse(node.children[0]) > traverse(node.children[1]) else 0


def get_packets(payload: str, parent: Packet) -> int:
    version = int(payload[:3], 2)
    type = int(payload[3:6], 2)
    offset = 6
    if type == 4:
        number, bits_passed = get_literal(payload[6:])
        parent.children.append(Packet(version, type, number))
        return offset + bits_passed

    len_type = int(payload[6])
    offset += 1
    if len_type == 0:
        payload_bits = int(payload[offset:offset+15], 2)
        offset += 15
        new_payload = payload[offset:offset+payload_bits]
        container = Packet(version, type, new_payload)
        parent.children.append(container)

        bits_passed = 0
        while bits_passed < payload_bits:
            bits_passed += get_packets(new_payload[bits_passed:], container)

        return offset + bits_passed
    else:
        packet_count = int(payload[offset:offset+11], 2)
        offset += 11
        new_payload = payload[offset:]
        container = Packet(version, type, new_payload)
        parent.children.append(container)

        bits_passed = 0
        for _ in range(packet_count):
            bits_passed += get_packets(new_payload[bits_passed:], container)

        return offset + bits_passed


def get_literal(payload: str) -> Tuple[int, int]:
    i = 0
    number = ''
    while True:
        i += 5
        number += payload[i-4:i]
        if payload[i-5] == '0':  # This is the final group
            break

    return (int(number, 2), i)


def get_binary(hex: str) -> str:
    binary = ''
    for x in hex:
        binary += hex_map[x]

    return binary


data = read('input')[0].strip()
solution(get_binary(data))
