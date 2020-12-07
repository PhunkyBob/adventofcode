file = open('day_03_input.txt', 'r') 
lines = file.readlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

expected_result = 1
for (right, down) in slopes:
    h_pos = 0
    trees_encoutered = 0
    for idx, line in enumerate(lines):
        width = len(line.strip())
        if idx % down == 0:
            if line[h_pos] == '#':
                trees_encoutered = trees_encoutered + 1
            h_pos = (h_pos + right) % width
    print(f"Slope ({right}, {down}) : {trees_encoutered} trees encoutered")
    expected_result = expected_result * trees_encoutered
print(f"Expected result {expected_result}")