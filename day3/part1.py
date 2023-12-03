import time
import re
# Start timer
start_time = time.time()

"""
1, save all symbols' location 
2, save all digital and its corresponding location
3, save their intersection
"""
digital_list = []
symbol_list = []
row = 0
total = 0
with open("input.txt") as myfile:

    for line in myfile:
        line = line.strip()
        row += 1
        # all symbols' location
        pattern_1 = re.compile('[^\.\d]')
        match_s = pattern_1.finditer(line)
        for s in match_s:
            y_axis = s.start()
            symbol_list.append((row, y_axis))

        # all digitals and its corresponding location
        pattern_2 = re.compile(r'\d+')
        match_d = pattern_2.finditer(line)
        for n in match_d:
            number_start = n.start()
            number_end = n.end()
            per_number = []
            for r in range(row-1,row+2): # every number set‘s all coordinates [(),(),()]
                for c in range(number_start-1, number_end+1):
                    per_number.append((r,c))
            digital_list.append([n.group(),per_number]) # [ ["",[(),(),()]],  ["",[(),(),()]]  ]

#check if there are any intersection
sl = set(symbol_list)
for i in digital_list:
    if set(i[1]) & sl:
        total += int(i[0])
print(total)


# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)