import numpy as np

masses = np.loadtxt('dec1_input.txt', delimiter = ',', unpack = False)

def fuel_counter_upper(masses):
    fuel = 0
    for mass in masses:
        fuel += (mass//3) - 2
    return int(fuel)