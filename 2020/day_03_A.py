file = open('day_03_input.txt', 'r') 
lines = file.readlines()

h_pos = 0
trees_encoutered = 0
for line in lines:
    width = len(line.strip())
    if line[h_pos] == '#':
        trees_encoutered = trees_encoutered + 1
    h_pos = (h_pos + 3) % width

print(f"{trees_encoutered} trees encoutered")