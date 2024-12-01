import pprint
import numpy as np


def calc_score(position, list):
    left = list[0:position]
    right = list[position + 1 : len(list)]
    current_height = list[position]
    tree_count_right = 0
    for index, height in enumerate(right):
        if height < current_height:
            tree_count_right += 1
        if height >= current_height:
            tree_count_right += 1
            break
    tree_count_left = 0
    for index, height in enumerate(np.flip(left)):
        if height < current_height:
            tree_count_left += 1
        if height >= current_height:
            tree_count_right += 1
            break
    return tree_count_left * tree_count_right


def find_scenic_view(heights):
    max_score = -1

    row_size = len(heights[0, :])
    column_size = len(heights[:, 0])

    for row_index in range(0, row_size):
        for column_index in range(0, column_size):
            score_row = calc_score(column_index, heights[row_index, :])
            score_column = calc_score(row_index, heights[:, column_index])
            current_score = score_row * score_column
            if current_score > max_score:
                max_score = current_score
    return max_score


with open("08-input.txt") as f:
    tree_map = []
    lines = f.readlines()
    for line in lines:
        sanitized_line = line.strip()
        tree_map.append([int(element) for element in sanitized_line])

tree_matrix = np.array(tree_map)

print(f"The max score is {find_scenic_view(tree_matrix)}")
