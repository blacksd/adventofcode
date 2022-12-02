# A = Rock, B = Paper, C = Scissors
# X = Lose, Y = Draw, Z = Win
SYMBOL_SCORE = {"A": 1, "B": 2, "C": 3}
MATCH_SCORE = {"X": 0, "Y": 3, "Z": 6}


def determine_shape(outcome, opponent):
    # X = Lose
    if outcome == "X":
        if opponent == "A":
            return "C"
        if opponent == "B":
            return "A"
        if opponent == "C":
            return "B"
    # Y = Draw
    if outcome == "Y":
        if opponent == "A":
            return "A"
        if opponent == "B":
            return "B"
        if opponent == "C":
            return "C"
    # Z = Win
    if outcome == "Z":
        if opponent == "A":
            return "B"
        if opponent == "B":
            return "C"
        if opponent == "C":
            return "A"


total_score = 0
with open('02-input.txt') as f:
    lines = f.readlines()
    for line in lines:
        opponent_shape = line.split()[0]
        desired_outcome = line.split()[1]
        my_shape = determine_shape(desired_outcome, opponent_shape)
        total_score += MATCH_SCORE[desired_outcome]
        total_score += SYMBOL_SCORE[my_shape]

print(f"The total score is: {total_score}")
