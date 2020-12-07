# https://adventofcode.com/2019/day/1

import math

def fuel_required(mass):
    return math.floor(mass / 3) - 2

file = open('2019/day_01_input.txt', 'r') 
total_fuel = sum(fuel_required(int(l)) for l in file.readlines())

print(total_fuel)
