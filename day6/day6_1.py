'''
Day 6: Wait For It
https://adventofcode.com/2023/day/6

# TODO
- Parse the Input DONE
- Write down a brute force algorithm for the problem
'''
from functools import reduce

# Input Parsing
file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day6/day6.txt"

times = []
distances = []
with open(file_path, "r") as file:
    for i, line in enumerate(file):
        line = line.strip()
        line = line.split(':')[1].split()
        
        match i:
            case 0:
                times = line
            case 1: 
                distances = line
            case _:
                print("More lines than expected in the input")
                
print(f"times: {times} \n distances: {distances}")
            
# Solve the problem (brute force)

num_races = len(times)

results = []
# Loop through the races
for i in range(0, num_races):
    time = int(times[i])
    max_distance = int(distances[i])
    better_races = 0
    
    # brute force, loop through each possible outcome
    for j in range(1, time):
        speed = j
        remaining_time = time - speed
        travelled_distance = remaining_time * speed
        
        if travelled_distance > max_distance:
            better_races += 1
    results.append(better_races)
    
print(f"The product of all ways to exceed the record distance for each race is: {reduce(lambda x,y: x * y, results, 1)}")
            