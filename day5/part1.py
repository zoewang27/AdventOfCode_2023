# read file, save seeds and map
seeds = []
big_map = []
with open('input.txt', 'r') as file:
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

# find destination
def get_des(source,map): #example: source=79, map=[[50, 98, 2], [52, 50, 48]]
    destination = source
    for r in map:
        if r[1] <= source <= r[1] + r[2] - 1:
            destination = source - r[1] + r[0]
            break
    return destination

def main():
    min_loc = None
    for i in seeds:
        s = i
        for j in big_map:
            d = get_des(s,j)
            s = d
        if min_loc is None or d < min_loc:
            min_loc = d
    print(min_loc)

main()
