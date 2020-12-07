# https://adventofcode.com/2020/day/7

import re 

rules = {}

def count_bags(color):
    nb_bags = 0
    for c in rules[color]:
        nb_bags += (1 + count_bags(c)) * int(rules[color][c])

    return nb_bags


# rules_txt = open('day_07_input_sample1.txt', 'r').read().split("\n")
# rules_txt = open('day_07_input_sample2.txt', 'r').read().split("\n")
rules_txt = open('day_07_input.txt', 'r').read().split("\n")


for r in rules_txt:
    id = r.split(" bags contain ")[0].strip()
    content_txt = r.split(" bags contain ")[1].split(", ")
    content = {}
    for c in content_txt:
        res = re.match(r'(\d+) ([\w\s]+) bag', c)
        if res:
            content[res[2]] = res[1]
    rules[id] = content


# Part A
contains_shiny_gold = []
old_size = 0
contains_shiny_gold.append('shiny gold')
new_size = len(contains_shiny_gold)
while old_size != new_size:
    old_size = new_size
    for r in rules:
        for c in rules[r]:
            if c in contains_shiny_gold and r not in contains_shiny_gold:
                contains_shiny_gold.append(r)
    new_size = len(contains_shiny_gold)

print("Contains shiny gold: " + str(contains_shiny_gold))
print(len(contains_shiny_gold) - 1)


# Part 2
print("A shiny gold bag contains " + str(count_bags("shiny gold")) + " bags.")
