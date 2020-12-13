# https://adventofcode.com/2020/day/13

# f = open("day_13_input_sample.txt", "r")
f = open("day_13_input.txt", "r")
earliest_timestamp = int(f.readline().strip())
bus_ids = [(i, int(b)) for (i, b) in enumerate(f.readline().strip().split(",")) if b != 'x']

# Part One
next_buses = [(b, earliest_timestamp + (b - earliest_timestamp % b) % b) for (i, b) in bus_ids]
next_bus = min(next_buses, key=(lambda b: b[1]))
print(f"Part One: next bus is {next_bus[0]} in {next_bus[1] - earliest_timestamp} min --> {next_bus[0] * (next_bus[1] - earliest_timestamp)}")

# Part Two
timestamp = 0
jump = 1        # Multiplication of all ranks already solved
for rank, b in bus_ids:
    while (timestamp + rank) % b != 0:
        timestamp += jump
    jump *= b
print(f"Part Two: {timestamp}")