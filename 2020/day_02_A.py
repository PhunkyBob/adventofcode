import re

file = open('day_02_input.txt', 'r') 
lines = file.readlines() 
  
count_ok = 0
for line in lines: 
    min, max, char, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    if int(min) <= pwd.count(char) <= int(max):
        count_ok = count_ok + 1

print(f"{count_ok} passwords are OK")
