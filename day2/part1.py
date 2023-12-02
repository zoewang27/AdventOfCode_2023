import time
import re

# Start timer
start_time = time.time()



color_map = {
    "blue": "14",
    "green": "13",
    "red": "12",
}

total_number = 0

with open("input.txt") as myfile:
    for line in myfile:
        game_number = int(line.split(":")[0].split(" ")[1])
        cubes_set = line.split(":")[1].split(";")
        result = True
        # deal with every record
        for i in range(len(cubes_set)):
            x = cubes_set[i].split(",")
            matches = [re.match(r'\s*(\d+)\s*([a-zA-Z]+)', item) for item in x]
            for match in matches:
                number, color = match.groups()  # number = 4； color = blue
                if int(number) > int(color_map[color]):
                    result = False
                    break

            if not result:
                break

        if result:
            total_number += game_number

print(total_number)

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)