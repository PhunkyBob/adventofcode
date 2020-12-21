# https://adventofcode.com/2020/day/21

# input = open("day_21_input_sample.txt", "r")
input = open("day_21_input.txt", "r")

# Part One
allergens_candidates = {}
foods = []
for line in input.readlines():
    ingredients_txt, allergens_txt = line.strip().split(" (contains ")
    ingredients = ingredients_txt.split(" ")
    allergens = allergens_txt.replace(")", "").split(", ")
    foods.append(ingredients)
    for a in allergens:
        if a not in allergens_candidates:
            allergens_candidates[a] = ingredients
        else:
            new_candidates = []
            new_candidates = [i for i in ingredients if i in allergens_candidates[a]]
            allergens_candidates[a] = new_candidates

can_contain_a = []
for a in allergens_candidates:
    can_contain_a += [i for i in allergens_candidates[a]]



total = 0
for f in foods:
    for i in f:
        if i not in can_contain_a:
            total += 1
print(f"Part One: {total}")


#Part Two
allergens_verified = {}
while any(len(allergens_candidates[e]) for e in allergens_candidates):
    for c in allergens_candidates:
        if len(allergens_candidates[c]) == 1:
            allergens_verified[c] = allergens_candidates[c][0]
            for remove in allergens_candidates:
                allergens_candidates[remove] = [elem for elem in allergens_candidates[remove] if elem != allergens_verified[c]]

part_two = ",".join([allergens_verified[elem] for elem in sorted(allergens_verified)])
print(f"Part Two: {part_two}")