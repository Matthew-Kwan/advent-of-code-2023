'''
Day 4: Scratchcards
https://adventofcode.com/2023/day/4

This is now a recursive problem where we want to resolve how many cards of each you get

'''
from collections import defaultdict

file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day4/day4.txt"

# As we have one of each card, we can automatically assign each to have 1 card
card_dict = defaultdict(lambda: 1)

with open(file_path, 'r') as file:
    for line in file:
        # cut out "Card "
        line = line[5:]
        card_id, rest = line.split(":")
        card_id = int(card_id)
        winning, actual = rest.split("|")
        winning = set(digit for digit in winning.split())
        actual = actual.split()
        
        res = 0 
        for num in actual:
            if num in winning:
                res += 1
                
        if card_id not in card_dict:
            card_dict[card_id] = 1
        
        for i in range(card_id+1, card_id + res + 1):
            card_dict[i] += card_dict[card_id]
        
    print(f"The sum of all points is {sum(card_dict.values())}")