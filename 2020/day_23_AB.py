# https://adventofcode.com/2020/day/23

input_txt = "389125467"
# input_txt = "247819356"

"""Brute copy of lists.
"""
def move_v1(input):
    current = input[0]
    # print("cups: " + " ".join(map(lambda x: f"({x})" if x == current else str(x), input)))
    pickup = input[1:4]
    # print("pick up: " + ", ".join(map(str, pickup)))
    remainings = list(input[4:])
    destination = max([0] + [e for e in remainings if e < current])
    destination = destination if destination != 0 else max(remainings)
    # print(f"destination: {destination}")
    new_input = list()
    for i in remainings:
        new_input.append(i)
        if i == destination:
            new_input += list(pickup)
    new_input.append(current)
    # print()

    return new_input

""" We use only 1 list and work on it.
"""
def compute(input_txt, loops=100):
    cup_circle = list(int(e) for e in input_txt)
    cup_size = len(cup_circle)
    current_pos = 0
    pop_cnt = 3
    for _ in range(loops):
        current_elem = cup_circle[current_pos]
        popped = [cup_circle[(current_pos + i) % cup_size] for i in range(1, pop_cnt + 1)]
        for p in popped:
            cup_circle.remove(p)
        destination = current_elem - 1
        while destination in popped or destination == 0:
            destination = cup_size if destination == 0 else (destination - 1) % cup_size
            
        destination_pos = cup_circle.index(destination)
        for p in reversed(popped):
            cup_circle.insert(destination_pos + 1, p)
        current_pos = (cup_circle.index(current_elem) + 1) % cup_size

    return cup_circle



# Part One
# input = list(int(e) for e in input_txt)

# total_rounds = 100
# for i in range(total_rounds):
#     print(f"-- move {i+1} --")
#     input = move_v1(input)
# current = input[0]
# print("final: " + " ".join(map(lambda x: f"({x})" if x == current else str(x), input)))
# part_one = input[input.index(1) + 1:] + input[:input.index(1)]
# print("Part One: ", "".join(map(str, part_one)))

final = compute(input_txt)
answer = final[final.index(1) + 1:] + final[:final.index(1)]
print("Part One: ", "".join(map(str, answer)))




# Part Two
# input = list(int(e) for e in input_txt)
# total_cups = 1_000_000
# input += list(i for i in range(max(input) + 1, total_cups + 1))

# total_rounds = 10_000_00
# for i in range(total_rounds):
#     input = move(input)
# index_1 = input.index(1)
# part_two = input[index_1 + 1] * input[index_1 + 2]
# print(f"Part Two: {part_two}")