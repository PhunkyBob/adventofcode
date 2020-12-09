# https://adventofcode.com/2020/day/9

# numbers = [int(x) for x in open("day_09_input_sample.txt", "r")]
# preamble = 5
numbers = [int(x) for x in open("day_09_input.txt", "r")]
preamble = 25


def verif(input, result):
    return any(result - i != i and result - i in input for i in input)


# Part One
max_search_index = 0
value_problem = 0
for i in range(preamble, len(numbers)):
    if not verif(numbers[i-preamble:i], numbers[i]):
        max_search_index = i
        value_problem = numbers[i]
        break
print(f"Error line {max_search_index} : {value_problem}")


# Part Two
solution = []
for i in range(max_search_index):
    j = i
    while j >= 0 and sum(numbers[j:i]) <= value_problem:
        if sum(numbers[j:i]) == value_problem:
            solution = numbers[j:i]
            break
        j = j - 1
print(f"Sum " + str(solution) + f" = {value_problem}")
smallest = min(solution)
largest = max(solution)
print(f"Part Two answer : {smallest} + {largest} = {smallest + largest}")