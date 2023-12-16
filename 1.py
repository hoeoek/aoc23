# Advent of Code: Day 1

with open("input.txt", "r") as f:
    puzzle_input = f.read()
    
lines = puzzle_input.split("\n")

def extract_number_chars(lines):
    tot_sum = 0
    for line in lines:
        numbers = ""
        for char in line:
            if char.isdigit():
                numbers += char
        if len(numbers) > 1:
            tot_sum += int(numbers[0] + numbers[-1])
        elif len(numbers) == 1:
            tot_sum += int(numbers + numbers)
        elif len(numbers) == 0:
            pass
        else:
            print("Something's fishy")
    return tot_sum

extract_number_chars(lines)
