import time
import re
# Start timer
start_time = time.time()

"""
1, save all *' location 
2, save all digital and its related location
3, save their intersection
"""
digital_list = []
symbol_list = []
row = 0
total = 0
with open("input_test.txt") as myfile:

    for line in myfile:
        line = line.strip()
        row += 1
        # all symbols' location
        pattern_1 = re.compile('[\*]')
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


symbol_set = set(symbol_list)
digital_dict = {item[0]: set(item[1]) for item in digital_list}
calculated_pairs = set()

for i, j in symbol_set:
    num = []

    for k, v in digital_dict.items():
        if (i, j) in v and k not in calculated_pairs:
            num.append(k)

    if len(num) == 2:
        ratio = int(num[0]) * int(num[1])
        total += ratio
        calculated_pairs.add(num[0])
        calculated_pairs.add(num[1])

print(total)


# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)