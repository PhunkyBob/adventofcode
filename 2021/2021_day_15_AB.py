# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/15 """

import time
import math
from collections import defaultdict
from queue import PriorityQueue
from itertools import product

class Cavern:
    cavern = []
    graph = {}

    def __init__(self, filename) -> None:
        self.cavern = [list(map(int, x.strip())) for x in open(filename, 'r').readlines()]

    def init_graph(self):
        self.graph = defaultdict(dict)
        for y, x in product(range(len(self.cavern)), range(len(self.cavern[0]))):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if x + dx < 0 or x + dx >= len(self.cavern[0]) or y + dy < 0 or y + dy >= len(self.cavern):
                    continue
                
                self.graph[(x,y)][(x+dx, y+dy)] = self.cavern[y+dy][x+dx]
        pass

    def extend(self):
        new_cavern_temp = []
        for line in self.cavern:
            new_line = []
            for mul_x in range(5):
                for val in line:
                    new_line.append((val + mul_x - 1) % 9 + 1)
            new_cavern_temp.append(new_line)
        
        new_cavern = []
        for mul_y in range(5):
            for line in new_cavern_temp:
                new_line = []
                for val in line:
                    new_line.append((val + mul_y - 1) % 9 + 1)
                new_cavern.append(new_line)
        self.cavern = new_cavern



    def dijkstra(self, start_node, end_node):
        unvisited_nodes = list(self.graph.keys())
        shortest_path = defaultdict(lambda: math.inf)
        previous_nodes = {}
        shortest_path[start_node] = 0
        
        current_min_node = None
        while unvisited_nodes and current_min_node != end_node:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes: # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            for neighbor in self.graph[current_min_node]:
                tentative_value = shortest_path[current_min_node] + self.graph[current_min_node][neighbor]
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
    
            unvisited_nodes.remove(current_min_node)
        
        return previous_nodes, shortest_path


def solve_part_one(input_file):
    cavern = Cavern(input_file)
    cavern.init_graph()
    previous_nodes, shortest_path = cavern.dijkstra((0,0), (len(cavern.cavern)-1, len(cavern.cavern[0])-1))
    return shortest_path[(len(cavern.cavern)-1, len(cavern.cavern[0])-1)]

def solve_part_two(input_file):
    cavern = Cavern(input_file)
    cavern.extend()
    cavern.init_graph()
    previous_nodes, shortest_path = cavern.dijkstra((0,0), (len(cavern.cavern)-1, len(cavern.cavern[0])-1))
    return shortest_path[(len(cavern.cavern)-1, len(cavern.cavern[0])-1)]


if __name__ == '__main__':
    start_time = time.time()

    # input_file = '2021_day_15_input_sample.txt'
    input_file = '2021_day_15_input.txt'

    """Part One"""
    result = solve_part_one(input_file)
    print(f'Day 15 Part One: {result}')
    # Your puzzle answer was 741.

    """Part Two"""
    # result = solve_part_two(input_file)
    print(f'Day 15 Part Two: {result}')
    # Your puzzle answer was 2976.

    print("--- %.2f seconds ---" % (time.time() - start_time))

