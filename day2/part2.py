import time
import re

# Start timer
start_time = time.time()


total_number = 0

with open("input.txt") as myfile:
    for line in myfile:
        game_number = int(line.split(":")[0].split(" ")[1])
        cubes_set = line.split(":")[1].split(";")  # split record
        # deal with every record
        color_map = {
            "blue": "0",
            "green": "0",
            "red": "0",
        }
        for i in range(len(cubes_set)):
            x = cubes_set[i].split(",")
            matches = [re.match(r'\s*(\d+)\s*([a-zA-Z]+)', item) for item in x]

            for match in matches:
                number, color = match.groups()
                if int(number) > int(color_map[color]):
                    color_map[color] = number

        line_value = int(color_map["blue"]) * int(color_map["green"]) * int(color_map["red"])
        total_number += line_value

print(total_number)

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)