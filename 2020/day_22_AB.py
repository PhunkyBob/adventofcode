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


# Part Two

game = 0
def part_two(player1, player2):
    p1_wins, winning_deck = play(player1, player2)
    score = sum((i + 1) * val for i, val in enumerate(reversed(winning_deck)))
    print(f"Player {1 if p1_wins else 2} wins. Score: {score}")
    return score


def play(player1, player2, depth=1):
    global game
    game += 1
    this_game = game
    memory = []
    # print(f"=== Game {this_game} ===")
    round = 0
    while player1 and player2:
        round += 1
        # print(f"-- Round {round}, Game {this_game} --")
        # print(f"Player 1's deck: {str(player1)}")
        # print(f"Player 2's deck: {str(player2)}")

        signature = str(player1) + " vs. " + str(player2)
        if signature in memory:
            # ends in a win for player 1
            # print("Recursive loop, Player 1 wins")
            return True, player1

        memory.append(signature)
        card1, card2 = player1.pop(0), player2.pop(0)
        # print(f"Player 1 plays: {card1}")
        # print(f"Player 2 plays: {card2}")

        if len(player1) >= card1 and len(player2) >= card2:
            # print("Playing a sub-game to determine the winner...")
            p1_wins, _ = play(player1[:card1], player2[:card2], depth+1)
        else:
            p1_wins = card1 > card2

        if p1_wins:
            # print(f"Player 1 wins the round {round} of game {this_game}!")
            player1 += [card1, card2]
        else:
            # print(f"Player 2 wins the round {round} of game {this_game}!")
            player2 += [card2, card1]

    return (True, player1) if player1 else (False, player2)


player1, player2 = [list(map(int, v)) for v in [player.split("\n")[1:] for player in input]]
start_time = time.time()
score = part_two(player1, player2)
print(f"Part Two: {score}")
print("--- %.2f seconds ---" % (time.time() - start_time))



