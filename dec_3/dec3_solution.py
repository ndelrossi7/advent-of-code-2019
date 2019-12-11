from tqdm import tqdm
inputs = open("dec_3/dec3_input.txt", "r")
data = inputs.readlines()
first = data[0].split(',')
first[-1] = first[-1][:4]
second = data[1].split(',')
second[-1] = second[-1][:4]

origin = (0, 0)

def all_steps(lst):
    coords = [(0, 0)]
    for step in lst:
        x = coords[-1][0]
        y = coords[-1][1]
        if step[0] == 'R':
            for i in range(1, int(step[1:]) + 1):
                coords.append((x+i, y))

        elif step[0] == 'L':
            for i in range(1, abs(int(step[1:])+1)):
                coords.append((x-i, y))

        elif step[0] == 'U':
            for i in range(1, int(step[1:]) + 1):
                coords.append((x, y+i))

        elif step[0] == 'D':
            for i in range(1, abs(int(step[1:])+1)):
                coords.append((x, y-i))

    return coords

def manhattan_distance(coord):
    x1 = 0
    y1 = 0
    x2 = coord[0]
    y2 = coord[1]
    manhattan = abs(x1 - x2) + abs(y1 - y2)
    return manhattan

first_path = all_steps(first)
second_path = all_steps(second)
intersections = [coord for coord in first_path if coord in second_path]
man_distances = [manhattan_distance(coord) for coord in intersections]
min_distance = sorted(man_distances)[1]
