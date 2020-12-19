# https://adventofcode.com/2020/day/19
import re 


# rules, messages = open("day_19_input_sample1.txt", "r").read().split("\n\n")
# rules, messages = open("day_19_input_sample2.txt", "r").read().split("\n\n")
rules, messages = open("day_19_input.txt", "r").read().split("\n\n")

rules = {int(r.split(': ')[0]): r.split(': ')[1].split(" ") for r in rules.split("\n")}



def find_pattern(index, depth=0):
    pattern = ""
    for item in rules[index]:
        match = re.match(r"\"(\w+)\"", item)
        if match:
            pattern += match[1]
            continue
        if item.isdigit():
            item = int(item)
            if item in patterns:
                # Already computed
                pattern += patterns[item]
            else:
                if item == index:
                    if depth == 0:
                        return f"({pattern})"
                    else:
                        pattern += find_pattern(item, depth - 1)
                else:
                    pattern += find_pattern(item, depth)
            continue
        if item == '|':
            pattern += '|'
            continue

    patterns[index] = f"({pattern})"
    return patterns[index]


# Part One
patterns = {}
pattern = "^" + find_pattern(0) + "$"
total = sum(1 for m in messages.split("\n") if re.match(pattern, m))
print(f"Part One: {total}")

# Part Two
rules[8] = "42 | 42 8".split(" ")
rules[11] = "42 31 | 42 11 31".split(" ")

patterns = {}
pattern = "^" + find_pattern(0, 10) + "$"
total = sum(1 for m in messages.split("\n") if re.match(pattern, m))
print(f"Part Two: {total}")
