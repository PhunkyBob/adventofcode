# https://adventofcode.com/2020/day/6

answers = open('day_06_input.txt', 'r').read().split("\n\n")

# Part A
total = sum(len(set(a.replace("\n", ""))) for a in answers)
print(f"Sum of counts: {total}")

# Part B
total = 0
for a in answers:
    intersection = "abcdefghijklmnopqrstuvwxyz"
    for p in a.split("\n"):
        intersection = set(intersection).intersection(p)
    total += len(intersection)
print(f"Sum of counts: {total}")