import re

lines = open('day_02_input.txt', 'r').readlines()

# Part One
count_ok = 0
for line in lines: 
    min, max, char, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    if int(min) <= pwd.count(char) <= int(max):
        count_ok = count_ok + 1

print(f"Part One: {count_ok} passwords are OK")

# Part Two
count_ok = 0
for line in lines: 
    pos1, pos2, char, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    if (pwd[int(pos1) - 1] == char) ^ (pwd[int(pos2) - 1] == char):
        count_ok = count_ok + 1

print(f"Part Two: {count_ok} passwords are OK")
