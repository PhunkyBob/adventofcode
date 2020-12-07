import re

file = open('day_02_input.txt', 'r') 
lines = file.readlines() 
  
count_ok = 0
for line in lines: 
    my_matches = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    pos1 = int(my_matches[1])
    pos2 = int(my_matches[2])
    char = my_matches[3]
    pwd = my_matches[4]
    if (pwd[pos1 - 1] == char) ^ (pwd[pos2 - 1] == char):
        count_ok = count_ok + 1

print(f"{count_ok} passwords are OK")
