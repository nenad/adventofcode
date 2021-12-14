from typing import Dict, List
from santa_helpers.reader import read
from operator import itemgetter

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

# Go two characters at a time (polymer) until we reach the end with the second one.
# If polymer is in $current map, increase the count of two new polymers in the $next map.
# If polymer is not in $current map, pass it forward to the $next map.
# NN -> NC CN
# NC -> NB BC
# CB -> CH HB
# XX -> XX


def solution(template: str, insertion_rules: Dict[str, str], runs: int = 10):
    pairs = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        pairs[pair] = pairs.get(pair, 0) + 1

    next_pairs = {}
    char_counts = {}
    for char in template:
        char_counts[char] = char_counts.get(char, 0) + 1

    for _ in range(runs):
        next_pairs = {}
        for pair, count in pairs.items():
            if pair in insertion_rules:
                new_char = insertion_rules[pair]
                pair_one = f'{pair[0]}{new_char}'
                pair_two = f'{new_char}{pair[1]}'
                next_pairs[pair_one] = next_pairs.get(pair_one, 0) + count
                next_pairs[pair_two] = next_pairs.get(pair_two, 0) + count
                char_counts[new_char] = char_counts.get(new_char, 0) + count
            else:
                next_pairs[pair] = next_pairs.get(pair, 0) + count

        pairs = next_pairs

    print(max(char_counts.values()) - min(char_counts.values()))


def get_data(line: str):
    if line.strip() == '':
        return

    parts = line.strip().split(' -> ')
    if len(parts) == 1:
        return parts[0]
    else:
        return (parts[0], parts[1])


data = read('input', get_data)
template = data[0]
polymers = {x: y for x, y in data[2:]}

solution(template, polymers, 10)
solution(template, polymers, 40)
