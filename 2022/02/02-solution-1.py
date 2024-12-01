# X = Rock, Y = Paper, Z = Scissor
# A = Rock, B = Paper, C = Scissors
SYMBOL_SCORE = {"X": 1, "Y": 2, "Z": 3}


def match_score(my, opponent):
    # X = Rock
    if my == "X":
        if opponent == "A":
            return 3
        if opponent == "B":
            return 0
        if opponent == "C":
            return 6
    # Y = Paper
    if my == "Y":
        if opponent == "A":
            return 6
        if opponent == "B":
            return 3
        if opponent == "C":
            return 0
    # Z = Scissor
    if my == "Z":
        if opponent == "A":
            return 0
        if opponent == "B":
            return 6
        if opponent == "C":
            return 3


total_score = 0
with open("02-input.txt") as f:
    lines = f.readlines()
    for line in lines:
        opponent_shape = line.split()[0]
        my_shape = line.split()[1]
        total_score += match_score(my_shape, opponent_shape)
        total_score += SYMBOL_SCORE[my_shape]

print(f"The total score is: {total_score}")
