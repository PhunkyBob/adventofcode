# https://adventofcode.com/2020/day/23
import time
from rich.progress import Progress


# input_txt = "389125467"
input_txt = "247819356"

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
def part_1(cup_circle, loops=100):
    # with Progress() as progress:
    #     task1 = progress.add_task("[green]Playing...", total=loops)
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
            # progress.update(task1, advance=1)
        # progress.completed = True
        return cup_circle


""" We work with pointers.
"""
def part_2(cups, fill=1_000_000, loops=10_000_000):
    # with Progress() as progress:
    #     update_every = 500_000
    #     task1 = progress.add_task("Setup...", total=fill)
    #     task2 = progress.add_task("[green]Playing...", total=loops//update_every)

        cup_next = {}

        for i in range(fill):
            if i < len(cups) - 1:
                cup_next[cups[i]] = cups[i + 1]
            elif i == len(cups) - 1:
                cup_next[cups[-1]] = max(cups) + 1
            else: 
                cup_next[i + 1] = (i + 2)
            # progress.update(task1, advance=1)
            
        cup_next[fill] = cups[0]

        current_elem = cups[0]

        for i in range(loops):
            # Short circuit
            pop_1 = cup_next[current_elem]
            pop_2 = cup_next[pop_1]
            pop_3 = cup_next[pop_2]
            cup_next[current_elem] = cup_next[pop_3]
            destination =  current_elem - 1

            while destination in [pop_1, pop_2, pop_3] or destination == 0:
                destination = fill if destination == 0 else destination - 1

            cup_next[pop_3] = cup_next[destination]
            cup_next[destination] = pop_1
            current_elem = cup_next[current_elem]
            # if i % update_every == 0:
            #     progress.update(task2, advance=1)

        # progress.completed = True
        return cup_next


# Part One
start_time = time.time()
cup_circle = list(int(e) for e in input_txt)
final = part_1(cup_circle)
answer = final[final.index(1) + 1:] + final[:final.index(1)]
print("Part One: ", "".join(map(str, answer)))
print("--- %.2f seconds ---" % (time.time() - start_time))



# Part Two
# Using same method as Part One, it will take days.
# start_time = time.time()
# cup_circle = list(int(e) for e in input_txt)
# total_cups = 1_000_000
# cup_circle += list(i for i in range(max(cup_circle) + 1, total_cups + 1))
# final = part_1(cup_circle, loops=10_000_000)
# index = final.index(1)
# answer = final[index + 1] * final[index + 2]
# print(f"Part Two: ", answer)
# print("--- %.2f seconds ---" % (time.time() - start_time))

start_time = time.time()
cups = list(int(e) for e in input_txt)
final = part_2(cups)
answer = final[1] * final[final[1]]
print(f"Part Two: ", answer)
print("--- %.2f seconds ---" % (time.time() - start_time))