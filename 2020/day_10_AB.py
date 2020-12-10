# https://adventofcode.com/2020/day/10

import re

def count_overlappings(pattern, text):
    left = 0
    count = 0
    while True:
        match = re.search(pattern, text[left:])
        if not match:
            break
        count += 1
        left += match.start() + 1
    return count

# adapters = [int(x) for x in open("day_10_input_sample1.txt", "r")]
# adapters = [int(x) for x in open("day_10_input_sample2.txt", "r")]
adapters = [int(x) for x in open("day_10_input.txt", "r")]

adapters.append(0)
adapters.sort()

# Part One
differences_count = {1: 0, 2: 0, 3: 1}
for i in range(1, len(adapters)):
    differences_count[adapters[i] - adapters[i-1]] += 1
print("Part One: " + str(differences_count[1] * differences_count[3]))

# Alternative
adapters.append(adapters[-1] + 3)
differences = []
for i in range(1, len(adapters)):
    differences.append(str(adapters[i] - adapters[i-1]))
plus_1 = sum(1 for d in differences if d == '1')
plus_3 = sum(1 for d in differences if d == '3')
print("Part One: " + str(plus_1 * plus_3))


# Part Two
differences_txt = "_" + "".join(differences) + "_"
four_ones = count_overlappings("[^1]1111[^1]", differences_txt)
three_ones = count_overlappings("[^1]111[^1]", differences_txt)
two_ones = count_overlappings("[^1]11[^1]", differences_txt)

print(7**four_ones * 4**three_ones * 2**two_ones)
