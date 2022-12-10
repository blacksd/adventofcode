import pprint
import numpy as np


def head_movement(starting_point: tuple(), movement: str) -> tuple():
    direction = movement[0]
    steps = int(movement[2])
    horiziontal_position = starting_point[0]
    vertical_position = starting_point[1]
    if direction == "R":
        destination_point = (horiziontal_position + steps, vertical_position)
    elif direction == "L":
        destination_point = (horiziontal_position - steps, vertical_position)
    elif direction == "U":
        destination_point = (horiziontal_position, vertical_position + steps)
    elif direction == "D":
        destination_point = (horiziontal_position, vertical_position - steps)
    return destination_point


def is_adjacent(point_a: tuple(), point_b: tuple()) -> bool:
    if point_a[0] == point_b[0]:
        # same row
        if abs(point_a[1] - point_b[1]) <= 1:
            return True
    elif point_a[1] == point_b[1]:
        # same column
        if abs(point_a[0] - point_b[0]) <= 1:
            return True
    else:
        # check for diagonal adjacency
        if (abs(point_a[1] - point_b[1]) == 1) and (abs(point_a[1] - point_b[1]) == 1):
            return True
    return False


def tail_movements(
    starting_point: tuple(), destination_point: tuple()
) -> list(tuple()):
    movements = []
    horizontal_starting = starting_point[0]
    horizontal_destination = destination_point[0]
    vertical_starting = starting_point[1]
    vertical_destination = destination_point[1]
    # horizontal movement
    if vertical_starting == vertical_destination:
        if horizontal_destination > horizontal_starting:
            # moving right
            for index in range(horizontal_starting + 1, horizontal_destination):
                movements.append((index, vertical_destination))
        else:
            # moving left
            for index in range(horizontal_starting + 1, horizontal_destination, -1):
                movements.append((index, vertical_destination))
    elif horizontal_starting == horizontal_destination:
        # vertical movement
        if vertical_destination > vertical_starting:
            # moving right
            for index in range(vertical_starting + 1, vertical_destination):
                movements.append((horizontal_destination, index))
        else:
            # moving left
            for index in range(horizontal_starting + 1, vertical_destination, -1):
                movements.append((horizontal_destination, index))
    else:
        # diagonal movement
        next

    return movements


if __name__ == "__main__":
    head_locations = []
    current_coordinates = (0, 0)
    with open("09-input-test.txt") as f:
        lines = f.readlines()
        for line in lines:
            sanitized_line = line.strip()
            current_coordinates = head_movement(current_coordinates, sanitized_line)
            head_locations.append(current_coordinates)

    print(f"The head location list is {head_locations}")

    head_location = (0, 0)
    tail_visited = set()
    tail_location = ()
    for head_destination in head_locations:
        tail_visited = tail_visited | set(
            tail_movements(head_location, head_destination)
        )
        print(f"The visited locations are {tail_visited}")
        head_location = head_destination
