from typing import Dict, List, Tuple
from santa_helpers.reader import read


def get_input(line: str) -> Tuple[List[str], List[str]]:
    segmentLine, outputLine = line.split('|')
    segments = segmentLine.strip().split(' ')
    output = outputLine.strip().split(' ')
    return (segments, output)


def solution1(input: List[Tuple[List[str], List[str]]]):
    count = 0
    for _, output in input:
        count += len([s for s in output if len(s) in (2, 3, 4, 7)])
    print(count)


def solution2(input: List[Tuple[List[str], List[str]]]):
    numberMap = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }

    sum = 0
    for segments, output in input:
        segment_map = get_segment_map(segments)

        number = ''
        for o in output:
            translated = ''.join(sorted([segment_map[c] for c in o]))
            number += f'%d' % numberMap[translated]

        sum += int(number)

    print(sum)


def get_segment_map(segments: List[str]) -> Dict:
    #  aaaa    ....    aaaa    aaaa    ....
    # b    c  .    c  .    c  .    c  b    c
    # b    c  .    c  .    c  .    c  b    c
    #  ....    ....    dddd    dddd    dddd
    # e    f  .    f  e    .  .    f  .    f
    # e    f  .    f  e    .  .    f  .    f
    #  gggg    ....    gggg    gggg    ....

    #  aaaa    aaaa    aaaa    aaaa    aaaa
    # b    .  b    .  .    c  b    c  b    c
    # b    .  b    .  .    c  b    c  b    c
    #  dddd    dddd    ....    dddd    dddd
    # .    f  e    f  .    f  e    f  .    f
    # .    f  e    f  .    f  e    f  .    f
    #  gggg    gggg    ....    gggg    gggg

    digitSegments = {}
    # Extract the unique numbers
    for s in segments:
        if len(s) == 2:
            digitSegments[1] = s
        if len(s) == 3:
            digitSegments[7] = s
        if len(s) == 4:
            digitSegments[4] = s
        if len(s) == 7:
            digitSegments[8] = s

    letterCounts = {}
    for segment in segments:
        for char in segment:
            if char in letterCounts:
                letterCounts[char] += 1
            else:
                letterCounts[char] = 1

    segmentMap = {}
    # a = 8 - known by diffing segments from number 1 and 7.
    segmentMap['a'] = set(digitSegments[7]).difference(digitSegments[1]).pop()
    # b = 6 occurrences - unique.
    segmentMap['b'] = [k for k in letterCounts if letterCounts[k] == 6].pop()
    # c = 8 - if you know a,  you know c, both have 8 occurrences.
    segmentMap['c'] = [k for k in letterCounts
                       if letterCounts[k] == 8 and k != segmentMap['a']].pop()
    # e = 4 occurrences - unique.
    segmentMap['e'] = [k for k in letterCounts if letterCounts[k] == 4].pop()
    # f = 9 occurrences - unique.
    segmentMap['f'] = [k for k in letterCounts if letterCounts[k] == 9].pop()
    # d = 7 - can be figured out by knowing b,c,f and the segments of the number 4.
    segmentMap['d'] = [c for c in digitSegments[4]
                       if c not in [segmentMap['b'], segmentMap['c'], segmentMap['f']]].pop()
    # g = 7 - known if you know d, both have the same number of segments.
    segmentMap['g'] = [k for k in letterCounts
                       if letterCounts[k] == 7 and k != segmentMap['d']].pop()

    return {v: k for k, v in segmentMap.items()}


data = read('input', get_input)

solution1(data)
solution2(data)
