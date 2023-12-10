'''
Day 5: If You Give A Seed A Fertilizer
https://adventofcode.com/2023/day/5
'''
from collections import defaultdict

file_path = "/Users/matthewkwan/workplace/advent-of-code-2023/day5/day5.txt"

def parse_text_file(file_path):
    data = {
        "seeds": [],
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
                data['seeds'] = list(map(int, line.split(":")[1].split()))
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
                # <3> - increment
                # Since you only really need the source end and not the destination end
                values = list(map(int, line.split()))
                
                # calculate the range using the increment, it is no longer needed after this step
                # so I just overwrite it
                values[2] = values[1] + values[2] - 1
                
                # append to main dictionary
                data[current_section].append(values)

    return data

result = parse_text_file(file_path)
seeds = result["seeds"]
del result["seeds"]

for i in range(len(seeds)):
    for mappings in result.values():
        for mapping in mappings:
            if mapping[1] <= seeds[i] <= mapping[2]:
                # seed found in the mapping
                diff = mapping[1] - mapping[0]
                seeds[i] = seeds[i] - diff
                break

print(f"{result}")
print(f"The smallest location found is: {min(seeds)}")
            
            