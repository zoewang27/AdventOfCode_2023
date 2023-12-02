"""
1, get lines from file
2, extract the first number and last number for every line
3, string_number = first_number + last_number, and convert it to int
4, add all numbers to the total_sum, and print it
"""

# part 1
total_sum = 0
with open("input.txt") as myfile:
    for line in myfile:
        every_number = []
        for ch in line:
            if ch.isnumeric():
                every_number.append(ch)
        value = int(every_number[0] + every_number[-1])
        total_sum += value

print(total_sum)