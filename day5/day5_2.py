'''
Day 5: If You Give A Seed A Fertilizer
https://adventofcode.com/2023/day/5

Algorithm:
We are mapping the ranges of the seeds as we go. At each iteration of this problem, we start with a range
from the previous mapping. For the initial case of the problem, we are able to get the mapping from the
beginning of the problem by using the values provided for the seed ranges.

When we are mapping to the next range, what we are trying to accomplish is as follows. 
1. We loop through the ranges that are provided moving into the map
2. We want to find all the source ranges in the mapping provided that overlap with the ranges that we have
   existing
3. If there is an overlap, we want to calculate the new range that we will then map into the next mapping
   - at the same time, we also want to consider the possibility that the overlap range will leave some of the
     original range unmapped, and thus we want to add those back in to the input ranges that we are looping through
     to make sure that we cover all the ranges that were inputted and none get left behind
     
What are the possible cases of overlap ranges?

- the new range completely is completely over the existing range
   - then we can calculate for the whole range
- the overlap only covers a portion of the left side of the input range
   - then we want to add the remainder of the input range on the right into the input range list
- the overlap only covers a portion of the right side of the input range
   - then we want to add the remainder of the input range on the left into the input range list
- the overlap only covers a portion of the input range in the middle
   - in this case we want to cover the remaining left and right sides of the input range, as two
     separate ranges in the input list
     
How do we determine when there is an overlap? 

So we are comparing one range to another. the key here is if the start of a range is within the boundaries of
another range, or if the end of a range is within the boundaries of another range, then there is an overlap. 

'''
from collections import defaultdict

file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day5/day5.txt"

seeds = []

def parse_text_file(file_path):
    data = {
        "seed_to_soil_map": [],
        "soil_to_fertilizer_map": [],
        "fertilizer_to_water_map": [],
        "water_to_light_map": [],
        "light_to_temperature_map": [],
        "temperature_to_humidity_map": [],
        "humidity_to_location_map": [],
    }

    current_section = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("seeds:"):
                x = list(map(int, line.split(":")[1].split()))
                for i in range(0, len(x), 2):
                    seeds.append((x[i], x[i] + x[i+1]))
            elif line.startswith("seed-to-soil map:"):
                current_section = "seed_to_soil_map"
            elif line.startswith("soil-to-fertilizer map:"):
                current_section = "soil_to_fertilizer_map"
            elif line.startswith("fertilizer-to-water map:"):
                current_section = "fertilizer_to_water_map"
            elif line.startswith("water-to-light map:"):
                current_section = "water_to_light_map"
            elif line.startswith("light-to-temperature map:"):
                current_section = "light_to_temperature_map"
            elif line.startswith("temperature-to-humidity map:"):
                current_section = "temperature_to_humidity_map"
            elif line.startswith("humidity-to-location map:"):
                current_section = "humidity_to_location_map"
            elif line == "":
                current_section = None
            else:
                # Structuring it so that the list for each mapping is
                # <0> - destination start
                # <1> - source start
                # <2> - source end
                # Since you only really need the source end and not the destination end
                values = list(map(int, line.split()))
                
                # calculate the range using the increment, it is no longer needed after this step
                # so I just overwrite it
                values[2] = values[1] + values[2]
                
                # append to main dictionary
                data[current_section].append(values)

    return data

result = parse_text_file(file_path)

# We can stop thinking about the input here, we are already at a point where the input parsing scales well with the input data that we have
# * This makes sense considering the fact that the input txt is relatively small, it's more so when we dynamically build out the data at runtime
# * that this problem actually gets harder

# This loops through the mappings that we possess 
for key, mappings in result.items():
    print(f"Section: {key} seeds: {seeds}")
    
    # list of seeds that we will pass on into the next section
    next_seeds = []
    
    # while we still have input seeds, we will keep on going until they are fully mapped to the next list
    while len(seeds) > 0:
        # pop a seed from the input list and get the start and end values for the range
        print(f"seeds: {seeds}")
        seed_start, seed_end = seeds.pop()
        # print(f"next seeds: {next_seeds}")
        # print(f"seed start: {seed_start} seed end: {seed_end}")
        
        # We have the range that we are checking for now, go through each of them one at a time
        for mapping in mappings:
            # parse the start and the ending as well as the diff
            start, end = mapping[1], mapping[2]
            diff = mapping[1] - mapping[0]
            
            print(f"start: {start} end: {end}")
            
            # check for overlap
            overlap_start = max(start, seed_start)
            overlap_end = min(end, seed_end)
            
            # if we find that the overlap values above actually form a valid range, then that means that we found an overlap
            if overlap_start < overlap_end:
                next_seeds.append((overlap_start - diff, overlap_end - diff))
                
                # These if statements help cover the ranges that are not handled by the overlap, and ensure that we are adding
                # them back into the input range to get them evaluated. 
                if overlap_start > seed_start:
                    seeds.append((seed_start, overlap_start))
                if overlap_end < seed_end:
                    seeds.append((overlap_end, seed_end))
                break
            
        # otherwise if there is no overlap found, we only append this entire range if we go through the whole thing without finding another thing to append 
        else:
            next_seeds.append((seed_start, seed_end)) 
    seeds = next_seeds

print(f"The smallest location found is: {min(seeds)[0]}")
            