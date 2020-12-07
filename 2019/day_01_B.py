# https://adventofcode.com/2019/day/1

import math

def fuel_required(mass):
    total_fuel = max(0, math.floor(mass / 3) - 2)
    if total_fuel > 0:
        fuel_for_fuel = fuel_required(total_fuel)
        total_fuel += fuel_for_fuel
    return total_fuel


file = open('2019/day_01_input.txt', 'r')
total_fuel = sum(fuel_required(int(l)) for l in file.readlines())

print(f"{total_fuel} fuel needed for modules")

print(total_fuel)
