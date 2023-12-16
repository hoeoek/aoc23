import re

test_cases = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

possible = "only 12 red cubes, 13 green cubes, and 14 blue cubes"

def build_budget(possible):
    regex = re.compile(r'(\d+) (\w+)')
    matches = regex.findall(possible)
    return dict((color, int(count)) for count, color in matches)

def check_against_budget(budget, hand):
    regex = re.compile(r'(\d+) (\w+)')
    matches = regex.findall(hand)
    return all(budget.get(color, 0) >= int(count) for count, color in matches)

def process_games():
    with open('input_2.txt', 'r') as f:
        cases = f.readlines()
    budget = build_budget(possible)
    id_sum = 0
    for game in cases:
        ok = True
        game_no = int(re.compile(r'(\d+):').findall(game)[0])
        game = game.split(':')[1].split(';')
        for hand in game:
            if not check_against_budget(budget, hand):
                print(f"Budget exceeded in game {game_no}")
                ok = False
                break
        if ok: 
            id_sum += game_no
        #print(f"Game number {game_no}, current id sum: {id_sum}")
    print(f"Final id sum: {id_sum}")
    return id_sum



process_games()

# Part 2, work in progress ##############################

# print(process_games(cases))
# 
# def get_max_count_of_each_color(cases):
#     regex = re.compile(r'(\d+) (\w+)')
#     matches = regex.findall(cases)
#     return dict((color, int(count)) for count, color in matches)
# 
# def count_products(cases):
#     max_count = get_max_count_of_each_color(cases)
#     regex = re.compile(r'(\d+) (\w+)')
#     matches = regex.findall(cases)
#     return sum(max_count.get(color, 0) * int(count) for count, color in matches)
# 
# 
# for game in test_cases:
#     for hand in game.split(':')[1].split(';'):
#         get_max_count_of_each_color(hand)
#     get_max_count_of_each_color(game.split(':')[1].split(';')[0])
#     print(count_products(game.split(':')[1].split(';')[0]))
# 
#     print(get_max_count_of_each_color(game.split(':')[1].split(';')[0]))
#             