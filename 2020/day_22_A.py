# https://adventofcode.com/2020/day/22

# player1, player2 = open("day_22_input_sample.txt").read().split("\n\n")
player1, player2 = open("day_22_input.txt").read().split("\n\n")

player1 = list(int(e) for e in player1.split("\n")[1:])
player2 = list(int(e) for e in player2.split("\n")[1:])

# Part One
print("Part One")
round = 1
while len(player1) and len(player2):
    print(f"-- Round {round} --")
    print(f"Player 1's deck: {str(player1)}")
    print(f"Player 2's deck: {str(player2)}")
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    print(f"Player 1 plays: {card1}")
    print(f"Player 2 plays: {card2}")
    if card1 > card2:
        print("Player 1 wins the round!")
        player1.append(card1)
        player1.append(card2)
    if card1 < card2:
        print("Player 2 wins the round!")
        player2.append(card2)
        player2.append(card1)
    print()
    round += 1

print("== Post-game results ==")
print(f"Player 1's deck: {str(player1)}")
print(f"Player 2's deck: {str(player2)}")

score1 = sum((i + 1) * val for i, val in enumerate(reversed(player1)))
score2 = sum((i + 1) * val for i, val in enumerate(reversed(player2)))

print(f"Player 1 scores {score1}")
print(f"Player 2 scores {score2}")