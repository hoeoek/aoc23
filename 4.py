
test_case = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\
"""

import re
    
with open("input_4.txt", "r") as f:
    puzzle_input = f.read()

def process_puzzle(puzzle_input, pattern = r":(.*)\|(.*)"):
    tot_sum = 0
    for card in puzzle_input.splitlines():
        matches = re.findall(pattern, card)
        wins, bets = matches[0]
        card_points = 0
        
        for bet in bets.split():
            if bet in wins.split() and card_points == 0:
                card_points += 1
            elif bet in wins.split() and card_points > 0:
                card_points = card_points * 2
        tot_sum += card_points
    return tot_sum

print(process_puzzle(test_case))
print(process_puzzle(puzzle_input))

