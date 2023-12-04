'''
Day 3: Gear Ratios
https://adventofcode.com/2023/day/3
'''

file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day3/day3.txt"

matrix = []

checked_set = set()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up_left': (-1, -1),
    'up_right': (-1, 1),
    'down_left': (1, -1),
    'down_right': (1, 1),
}

def check_around_symbol(x: int, y: int) -> int:
    sum = 0
    for direction in directions.values():
        
        # Get new indices
        new_y = y + direction[0]
        new_x = x + direction[1]
        
        # Check for boundaries
        if new_x >= 0 and new_x < len(matrix) and new_y >= 0 and new_y < len(matrix[0]):
            
            # only proceed if the value around the symbol is a digit and we have not already checked the index
            if matrix[new_x][new_y].isdigit() and (new_x, new_y) not in checked_set:
                # add it to the checked set
                checked_set.add((new_x, new_y))
                
                # init the string number that we will track
                digit_str = matrix[new_x][new_y]
                
                # get new values for the two pointers
                left, right = new_y-1, new_y+1
                
                # work on the left pointer first
                while left >= 0 and (new_x, left) not in checked_set:
                    if matrix[new_x][left].isdigit():
                        # if a digit, append the value to the result string on the left
                        digit_str = matrix[new_x][left] + digit_str
                        
                        # add the checked index into the checked set
                        checked_set.add((new_x, left))
                        left -= 1
                    else:
                        break
                    
                # work on the right pointer
                while right < len(matrix[0]) and (new_x, right) not in checked_set:
                    if matrix[new_x][right].isdigit():
                        # if a digit, append to the right of the result string
                        digit_str = digit_str + matrix[new_x][right]
                        
                        # add the index to the checked set
                        checked_set.add((new_x, right))
                        right += 1
                    else:
                        break
                sum += int(digit_str)
    return sum

with open(file_path, 'r') as file:
    res: int = 0
    for line in file:
        matrix.append(list(line.strip()))
        
    print(matrix)
    for x, row in enumerate(matrix):
        for y, val in enumerate(row):
            if matrix[x][y] != "." and not matrix[x][y].isdigit() and not matrix[x][y].isspace():
                res += check_around_symbol(x, y)
        
    print(f"The sum of all part numbers in the engine schematic is {res}.")
