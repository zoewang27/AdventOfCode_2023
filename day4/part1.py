import re
"""
1，get winning number and number you have
2，get interaction
3，if exist interaction, calculate score
4，calculate whole score
"""
total = 0
with open("input.txt") as myfile:
    for line in myfile:
        score = 0
        card, num = line.split(":")
        win_num, all_num = num.split("|")
        pattern = re.compile(r'\d+')
        win_set = set(pattern.findall(win_num))
        all_set = set(pattern.findall(all_num))
        if len(win_set & all_set) >= 1:
            score = 2 ** (len(win_set & all_set)-1)
        total += score
print(total)
