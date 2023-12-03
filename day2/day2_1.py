'''
Day 2: Cube Conundrum
https://adventofcode.com/2023/day/2

Input: Games on each new line, each line is a semi-colon separated value of sets that are played, with each set being a csv of # of marbles to color.
Output: Given a specific configuration defined in the problem, need to get the sum of each of the games that were possible.

Algorithm:
1) write the parsing logic for the raw data
2) write checks against the max number, if any fail, continue to next line
  - if none fail, then add Game ID to the result

'''

file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day2/day2.txt"

# Constants provided by the question
cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

res = 0

with open(file_path, 'r') as file:
    for line in file:
        # cut out "Game "
        line = line[5:]
        gameID, sets = line.split(":")
        gameID = int(gameID)
        valid = True
        
        sets = sets.split(";")
        for s in sets:
            pairs = s.split(",")
            for pair in pairs:
                val, color = pair.split()
                if int(val) > cubes[color]:
                    valid = False
                    break
        if valid:
            res += gameID
            
    print(f"The sum of all valid Game IDs is {res}")