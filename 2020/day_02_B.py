import re

file = open('day_02_input.txt', 'r') 
lines = file.readlines() 
  
count_ok = 0
for line in lines: 
    pos1, pos2, char, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    if (pwd[int(pos1) - 1] == char) ^ (pwd[int(pos2) - 1] == char):
        count_ok = count_ok + 1

print(f"{count_ok} passwords are OK")
