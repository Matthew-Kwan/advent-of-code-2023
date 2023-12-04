'''
Day 4: Scratchcards
https://adventofcode.com/2023/day/4

Determine how many winning numbers are on each card

'''

file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day4/day4.txt"

card_dict = {}

with open(file_path, 'r') as file:
    total = 0
    for line in file:
        winning, actual = line.split("|")
        winning = set(digit for digit in winning.split())
        actual = actual.split()
        
        res = 0 
        for num in actual:
            if num in winning:
                if res == 0:
                    res = 1
                else: 
                    res *= 2
        total += res
        
    print(f"The sum of all points is {total}")