'''
Day 2: Cube Conundrum
https://adventofcode.com/2023/day/2

Input: Games on each new line, each line is a semi-colon separated value of sets that are played, with each set being a csv of # of marbles to color.
Output: Given a specific configuration defined in the problem, need to get the sum of each of the games that were possible.

Algorithm:
1) write the parsing logic for the raw data
2) write checks against the max number, if any fail, continue to next line
  - if none fail, then add Game ID to the result
3) keep track of the max value found in each line

'''
import math

file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day2/day2.txt"

res = 0

with open(file_path, 'r') as file:
    for line in file:
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        
        # cut out "Game "
        line = line[5:]
        _, sets = line.split(":")
        
        sets = sets.split(";")
        for s in sets:
            pairs = s.split(",")
            for pair in pairs:
                val, color = pair.split()
                if int(val) > cubes[color]:
                    cubes[color] = int(val)
        
        res += math.prod(cubes.values())
            
    print(f"The sum of powers for all sets is {res}")