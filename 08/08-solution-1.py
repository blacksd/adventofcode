import pprint
import numpy as np


def find_visible_trees(heights, is_transposed: bool):
    visible_trees = set()
    row_size = len(heights[0, :])
    column_size = len(heights[:, 0])

    for row_index in range(0, row_size):
        # Set a bogus height value so for every row the first tree will always match
        highest_tree_in_row = -1
        for column_index in range(0, column_size):
            if row_index == 0 or row_index == row_size - 1:
                if is_transposed:
                    visible_trees.add((column_index, row_index))
                else:
                    visible_trees.add((row_index, column_index))
                next
            elif heights[row_index, column_index] > highest_tree_in_row:
                if is_transposed:
                    visible_trees.add((column_index, row_index))
                else:
                    visible_trees.add((row_index, column_index))
                highest_tree_in_row = heights[row_index, column_index]
    for row_index in range(0, row_size):
        # Set a bogus height value so for every row the first tree will always match
        highest_tree_in_row = -1
        for column_index in range(column_size - 1, -1, -1):
            if row_index == 0 or row_index == row_size - 1:
                if is_transposed:
                    visible_trees.add((abs(column_index), row_index))
                else:
                    visible_trees.add((row_index, abs(column_index)))
                next
            elif heights[row_index, column_index] > highest_tree_in_row:
                if is_transposed:
                    visible_trees.add((abs(column_index), row_index))
                else:
                    visible_trees.add((row_index, abs(column_index)))
                highest_tree_in_row = heights[row_index, column_index]
    return visible_trees


with open("08-input.txt") as f:
    tree_map = []
    lines = f.readlines()
    for line in lines:
        sanitized_line = line.strip()
        tree_map.append([int(element) for element in sanitized_line])

tree_matrix = np.array(tree_map)
look_in_rows = find_visible_trees(tree_matrix, False)
look_in_columns = find_visible_trees(np.transpose(tree_matrix), True)

print(f"The visible trees are {len(look_in_rows | look_in_columns)}")
