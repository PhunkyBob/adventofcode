# https://adventofcode.com/2020/day/25

import time

input_file = "day_25_input_sample.txt"
input_file = "day_25_input.txt"
card_pk, door_pk = map(int, open(input_file, "r"))



def get_loops(pk, initial_sn=7):
    loop = 0
    value = 1
    while value != pk:
        loop += 1
        value = (value * initial_sn) % 20201227
    return loop

def encrypt(sn, loop_size):
    value = pow(sn, loop_size, 20201227)
    return value

def get_encryption_key(pk1, pk2, initial_sn=7):
    loop = 0
    value = 1
    while value != pk1 and value != pk2:
        loop += 1
        value = (value * initial_sn) % 20201227
    return pow(pk2 if value == pk1 else pk1, loop, 20201227)


start_time = time.time()
# card_loops = get_loops(card_pk)
# door_loops = get_loops(door_pk)
# encryption_key = encrypt(door_pk, card_loops)
encryption_key = get_encryption_key(door_pk, card_pk)
print(f"Part One, encryption key is: {encryption_key}")
print("--- %.2f seconds ---" % (time.time() - start_time))

