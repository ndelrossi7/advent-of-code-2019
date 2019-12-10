import numpy as np

inputs = np.loadtxt('dec_2/dec2_input.txt', delimiter = ',', unpack = False)
inputs = [int(x) for x in inputs]
# Part 1 
def opcode(lst):
    l = lst[:]
    place = 0
    for i in range(0, len(lst)+1, 4):
        if l[i] == 1:
            l[l[place+3]] = l[l[place+1]] + l[l[place+2]]
        elif l[i] == 2:
            l[l[place+3]] = l[l[place+1]] * l[l[place+2]]
        elif l[i] == 99:
            break
        place += 4
    return l

def program1202(lst):
    lst[1] = 12
    lst[2] = 2
    return lst

prog1202 = program1202(inputs)

part1ans = opcode(prog1202)[0]
# print(part1ans)

# -------------------------

# Part 2

def pairs(lst):
    for n in range(100):
        for v in range(100):
            lst[1] = n
            lst[2] = v
            result = opcode(lst)
            if result[0] == 19690720:
                return (100 * n + v)

part2ans = pairs(inputs)
# print(part2ans)