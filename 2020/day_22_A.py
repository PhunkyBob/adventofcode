# https://adventofcode.com/2020/day/22

import time

# input = open("day_22_input_sample.txt").read().split("\n\n")
input = open("day_22_input.txt").read().split("\n\n")


player1, player2 = [list(map(int, v)) for v in [player.split("\n")[1:] for player in input]]

def part_one(player1, player2):
    round = 0
    while player1 and player2:
        round += 1
        # print(f"-- Round {round} --")
        # print(f"Player 1's deck: {str(player1)}")
        # print(f"Player 2's deck: {str(player2)}")
        card1, card2 = player1.pop(0), player2.pop(0)
        # print(f"Player 1 plays: {card1}")
        # print(f"Player 2 plays: {card2}")
        if card1 > card2:
            # print("Player 1 wins the round!")
            player1 += [card1, card2]
        if card1 < card2:
            # print("Player 2 wins the round!")
            player2 += [card2, card1]
        print()
        
    print(f"== Post-game results after {round} rounds ==")
    print(f"Player 1's deck: {str(player1)}")
    print(f"Player 2's deck: {str(player2)}")
    score1 = sum((i + 1) * val for i, val in enumerate(reversed(player1)))
    score2 = sum((i + 1) * val for i, val in enumerate(reversed(player2)))
    
    print(f"Player 1 scores {score1}")
    print(f"Player 2 scores {score2}")
    return score1 + score2


# Part One
start_time = time.time()
score = part_one(player1, player2)
print(f"Part One: {score}")
print("--- %.2f seconds ---" % (time.time() - start_time))