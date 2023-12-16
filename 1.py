# Advent of Code: Day 1

with open("input_1.txt", "r") as f:
    puzzle_input = f.read()
    
lines = puzzle_input.split("\n")

dub_words = {
    "oneight": "oneeight",
    "twone": "twoone",
    "threeight": "threeeight",
    "fiveight": "fiveeight",
    "sevenine": "sevennine",
    "eightwo": "eighttwo",
    "nineight": "nineeight"
}

word2num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def replace_words_with_digits(line):
    for sqeezed, unsqeezed in dub_words.items():
        line = line.replace(sqeezed, unsqeezed)
    for word, digit in word2num.items():
        line = line.replace(word, digit)
    return line

def extract_number_chars(lines: list):
    tot_sum = 0
    for line in lines:
        line = replace_words_with_digits(line)
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

print(extract_number_chars(lines))
