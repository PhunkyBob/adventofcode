# https://adventofcode.com/2020/day/19
import re 

# rules, messages = open("day_19_input_sample1.txt", "r").read().split("\n\n")
rules, messages = open("day_19_input.txt", "r").read().split("\n\n")

rules = {int(r.split(': ')[0]): r.split(': ')[1].split(" ") for r in rules.split("\n")}

patterns = {}

def find_pattern(index):
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
                pattern += find_pattern(item)
            continue
        if item == '|':
            pattern += '|'
            continue

    patterns[index] = f"(?:{pattern})"
    return patterns[index]

pattern = "^" + find_pattern(0) + "$"
total = sum(1 for m in messages.split("\n") if re.match(pattern, m))
print(f"Part One: {total}")