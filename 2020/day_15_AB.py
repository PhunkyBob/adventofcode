# https://adventofcode.com/2020/day/15

import time


# input = "0,3,6".split(',')
# input = "3,1,2".split(',')
input = "7,14,0,17,11,1,2".split(',')

def compute(input, total_turns):
    memory = {}
    last_spoken = 0
    turn = 0
    for turn in range(total_turns):
        if turn < len(input):
            last_spoken = int(input[turn])
            memory[last_spoken] = (turn, turn)
        else:
            last, before_last = memory[last_spoken]
            last_spoken = last - before_last
            if last_spoken not in memory:
                memory[last_spoken] = (turn, turn)
            else:
                memory[last_spoken] = (turn, memory[last_spoken][0])
    return last_spoken

# Part One
start_time = time.time()
max_turn = 2020
last_spoken = compute(input, max_turn)
print(f"Part One, Turn {max_turn + 1}, last spoken number: {last_spoken}")
print("--- %.2f seconds ---" % (time.time() - start_time))

# Part Two
start_time = time.time()
max_turn = 30000000
last_spoken = compute(input, max_turn)
print(f"Part One, Turn {max_turn + 1}, last spoken number: {last_spoken}")
print("--- %.2f seconds ---" % (time.time() - start_time))
