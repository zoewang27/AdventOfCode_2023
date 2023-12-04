
import re

file = open("input.txt")
lines = file.readlines()

card_dic = {}
total = 0
pattern = re.compile(r'\d+')

def dealwith_line(every_line):
    card, num = every_line.split(":")
    card_1 = pattern.findall(card)
    return card_1[0], num

def main():
    # update card_dic
    for line in lines:
        key, _ = dealwith_line(line)
        card_dic[key] = 1

    #find interaction and update value
    for line in lines:
        #find current card_id
        card_id, num = dealwith_line(line)
        card_id = int(card_id)

        win_num, all_num = num.split("|")
        win_set = set(pattern.findall(win_num))
        all_set = set(pattern.findall(all_num))
        if len(win_set & all_set) >= 1:
            for i in range(len(win_set & all_set)):
                card_key = str(card_id + i + 1)
                if card_key in card_dic:
                    card_dic[card_key] = card_dic[card_key] + card_dic[str(card_id)]

    total = sum(card_dic.values())
    print(total)

main()