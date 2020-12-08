# https://adventofcode.com/2020/day/7

import re 
import networkx as nx
import matplotlib.pyplot as plt

rules_txt = open('day_07_input_sample1.txt', 'r').read().split("\n")
# rules_txt = open('day_07_input_sample2.txt', 'r').read().split("\n")
# rules_txt = open('day_07_input.txt', 'r').read().split("\n")

DG = nx.DiGraph()

for r in rules_txt:
    id = r.split(" bags contain ")[0].strip()
    content_txt = r.split(" bags contain ")[1].split(", ")
    content = {}
    for c in content_txt:
        res = re.match(r'(\d+) ([\w\s]+) bag', c)
        if res:
            DG.add_edge(id, res[2], weight=int(res[1]))

ancestors = nx.ancestors(DG, "shiny gold")
print("'shiny gold' ancestors: " + str(ancestors))
print(f"Part One: {len(ancestors)} ancestors")


nx.draw(DG, with_labels=True, with_weight=True)
plt.show()