# https://adventofcode.com/2020/day/5

def seat_id(input):
    row = input[0:-3].replace('F', '0').replace('B', '1')
    col = input[-3:].replace('L', '0').replace('R', '1')
    return int(row, 2) * 8 + int(col, 2)

seats = open('day_05_input.txt', 'r').read().split()
seats_ids = [seat_id(s) for s in seats]
max_seat_id = max(seats_ids)
print(f"Max seat ID: {max_seat_id}")