"""
1, get lines from file
2, for every line: extract the first number and last number(including digital and words)
3, string_number = first_number + last_number, and convert it to int
4, add all numbers to the total_sum, and print it
"""

import time

# Start timer
start_time = time.time()


digital_map = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

total_sum = 0

with open("input.txt") as myfile:
    for line in myfile:
        every_number = []
        tem = ""
        for ch in line:
            if ch.isnumeric():
                every_number.append(ch)
                tem = ""
            else:
                tem += ch
                for i in digital_map.keys():
                    if i in tem:
                        every_number.append(digital_map[i])
                        tem = tem[len(i)-1:]
        value = int(every_number[0] + every_number[-1])
        total_sum += value

print(total_sum)


# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)