# https://adventofcode.com/2020/day/5

def seat_id(input):
    row = input[0:-3].replace('F', '0').replace('B', '1')
    col = input[-3:].replace('L', '0').replace('R', '1')
    return int(row, 2) * 8 + int(col, 2)

def boarding_pass(row, col):
    return ('00000000' + bin(row).replace('0b', ''))[-7:].replace('0', 'F').replace('1', 'B') + ('00000000' + bin(col).replace('0b', ''))[-3:].replace('0', 'L').replace('1', 'R')

seats = open('day_05_input.txt', 'r').read().split()

seats_ids = [seat_id(s) for s in seats]
empty_seat_id = set(range(min(seats_ids), max(seats_ids))) - set(seats_ids)
print(f"Empty seats: {empty_seat_id}")


