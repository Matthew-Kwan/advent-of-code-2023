'''
Input: a txt doc with strings should possess at least 1 digit
Output: get the first and last digit from each string, form a two-digit number, then sum them together

Edge Cases:
- if a string has a single digit, then that digit is repeated twice to get the two-digit number

Algorithms:
- do a two pointer approach
- use isDigit functionality
- find out how to append to beginning or end of string and use those functions for two pointers\
    
Part two: 
- I can keep memory of a string that is continuous and check if I can find anything at that point
  - for the right pointer, I can just reverse the string everytime, or better yet, append it in the opposite order 
'''



file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day1/day1.txt"
number_dict = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9"
}
res = 0

def check_validity(val: str, side: str) -> bool:
    if side == "left":
        for key in number_dict:
            if key.startswith(val): 
                return True
    else:
        for key in number_dict:
            if key.endswith(val): 
                return True
    return False

with open(file_path, 'r') as file:
    for line in file:
        number = ""
        left = 0
        right = len(line) - 1
        
        left_str = ""
        right_str = ""
        # keep going with left and right pointers until the end of the string
        while left < len(line) or right >= 0:
            if left < len(line):
                if line[left].isdigit():
                    number = line[left] + number
                    # make this value break the while condition
                    left = len(line)
                else:
                    left_str = left_str + line[left]
                    if left_str in number_dict:
                        number = number_dict[left_str] + number
                        left = len(line)
                    elif not check_validity(left_str, "left"):
                        while True:
                            left_str = left_str[1:]
                            if check_validity(left_str, "left") or len(left_str) == 0:
                                break
            
            if right >= 0:
                if line[right].isdigit():
                    number = number + line[right]
                    # make this value break the while condition
                    right = -1
                else:
                    right_str = line[right] + right_str
                    if right_str in number_dict:
                        number = number + number_dict[right_str]
                        right = -1
                    elif not check_validity(right_str, "right"):
                        while True:
                            right_str = right_str[:-1]
                            if check_validity(right_str, "right") or len(right_str) == 0:
                                break
                
            # increment/decrement pointers
            left += 1
            right -= 1
        
        try:
            calibration_value = int(number)
        except Exception:
            print(f"Failed to convert {number} to a string")
        
        res += calibration_value

    print(f"The sum of all calibration values is {res}")