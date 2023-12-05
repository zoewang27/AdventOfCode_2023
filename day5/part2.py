# read file
seeds = []
big_map = []
with open('input_test.txt', 'r') as file:
    for line in file:
        # get seed data
        if line.startswith('seeds:'):
            seeds = list(map(int, line.split()[1:]))

        elif line.strip().endswith('map:'):
            single_map = []
            while True:
                row = list(map(int,file.readline().split())) # read the next line
                if not row:
                    break
                single_map.append(row)
            big_map.append(single_map)

def get_des(source,map): #example: source=79, map=[[50, 98, 2], [52, 50, 48]]
    destination = source
    for r in map:
        if r[1] <= source <= r[1] + r[2] - 1:
            destination = source - r[1] + r[0]
            break
    return destination

def main():
    # splitting a list
    start = seeds[::2]  # get start number
    length = seeds[1::2]  # get length

    min_loc = None
    for n in range(len(start)):
        for h in range(length[n]):
            s = start[n]+h
            for j in big_map:
                d = get_des(s, j)
                s = d

            if min_loc is None or d < min_loc:
                min_loc = d
    print(min_loc)

main()
