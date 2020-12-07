# https://adventofcode.com/2019/day/3

def steps(path):
    wire = {}
    x = 0
    y = 0
    steps = 0
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    # wire.append((x ,y))
    for pos in path.split(','):
        div_x, div_y = directions[pos[0]]
        for _ in range(int(pos[1:])):
            steps += 1
            x += div_x
            y += div_y
            if (x, y) not in wire:
                wire[(x ,y)] = steps
    return wire

wires = open('day_03_input.txt', 'r').read().split()

# wires = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
# wires = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

wire1 = steps(wires[0])
wire2 = steps(wires[1])

intersection = set(wire1).intersection(wire2)
closer = min(abs(i[0]) + abs(i[1]) for i in intersection)
faster = min(wire1[i] + wire2[i] for i in intersection)

print(f"Closer {closer}")
print(f"Faster {faster}")
