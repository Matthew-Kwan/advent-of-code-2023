'''
Day 6: Wait For It
https://adventofcode.com/2023/day/6
'''
from functools import reduce
import math

# Input Parsing
file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day6/day6.txt"

time = 0
max_distance = 0
with open(file_path, "r") as file:
    for i, line in enumerate(file):
        line = line.strip()
        line = line.split(':')[1].split()
        value = int("".join(line))
        
        match i:
            case 0:
                time = value
            case 1: 
                max_distance = value
            case _:
                print("More lines than expected in the input")
            
# Solve the problem

results = []

# # brute force, took like 15s
# for j in range(1, time):
#     speed = j
#     remaining_time = time - speed
#     travelled_distance = remaining_time * speed
    
#     if travelled_distance > max_distance:
#         better_races += 1
        
# quadratic approach
x1 = math.ceil((time - math.sqrt(time**2 - 4 * max_distance)) / 2)
x2 = int((time + math.sqrt(time**2 - 4 * max_distance)) // 2)
better_races = x2 - x1 + 1
    
print(f"The number of ways to exceed the max distance for this race is: {better_races}")
            