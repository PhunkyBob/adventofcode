# https://adventofcode.com/2020/day/1

values = [int(x) for x in open("day_01_input.txt", "r")]

# Part One
# for i in values:
#     for j in values:
#         if i + j == 2020:
#             print(f"{i} * {j} = {i*j}")


# Alternative
res = list(i * j for i in values for j in values if i + j == 2020)[0]
print(f"Part One: {res}")


# Part Two
# for i in values:
#     for j in values:
#         for k in values:
#             if i + j + k == 2020:
#                 print(f"{i} * {j} * {k} = {i*j*k}")

# Alternative
res = list(i * j * k for i in values for j in values for k in values if i + j + k == 2020)[0]
print(f"Part Two: {res}")
