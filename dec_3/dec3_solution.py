inputs = open("dec_3/dec3_input.txt", "r")
data = inputs.readlines()
first = data[0].split(',')
first[-1] = first[-1][:4]
second = data[1].split(',')
second[-1] = second[-1][:4]

origin = (0, 0)

# recursively add to a list based on previous coordinate

def steps(lst):
    coords = [(0, 0)]
    for step in lst: 
        prev = coords[-1]
        if step[0] == 'R':
            next_ = (prev[0] + int(step[1:]), prev[1])
            coords.append(next_)
        elif step[0] == 'L':
            next_ = (prev[0] - int(step[1:]), prev[1])
            coords.append(next_)
        elif step[0] == 'U':
            next_ = (prev[0], prev[1] + int(step[1:]))
            coords.append(next_)
        elif step[0] == 'D':
            next_ = (prev[0], prev[1] - int(step[1:]))
            coords.append(next_)
    return coords

first_path = steps(first)
second_path = steps(second)

def all_steps(lst):
    coords = [(0, 0)]
    for step in tqdm(lst):
        x = coords[-1][0]
        y = coords[-1][1]
        if step[0] == 'R':
            for i in range(x, (int(step[1:]) + x + 1)):
                coords.append((x+i, y))

        elif step[0] == 'L':
            for i in range(x, (int(step[1:]) - x + 1)):
                coords.append((x-i, y))

        elif step[0] == 'U':
            for i in range(y, (int(step[1:]) + y + 1)):
                coords.append((x, y+i))

        elif step[0] == 'D':
            for i in range(y, (int(step[1:]) - y + 1)):
                coords.append((x, y-i))

    return coords

first_path = all_steps(first)
second_path = all_steps(second)
intersections = [coord for coord in first_path if coord in second_path]


my_coords = [(0, 0)]
x = my_coords[-1][0]
y = my_coords[-1][1]
test = second[6]
testing = []
if test[0] == 'R':
    for i in range(x, (int(test[1:])+x+1)):
        testing.append(((x+i), y))