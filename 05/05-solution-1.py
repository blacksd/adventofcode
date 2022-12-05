import pprint
import re


def build_stack_columns(stack_columns: list, line: str) -> list():
    """
    This will build a list of lists for each column, index 0 is the bottom of the stack
    [   ['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'],
        ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
        ['Z', 'H', 'V'],
        ['M', 'Z', 'J', 'F', 'G', 'H'],
        ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
        ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
        ['T', 'F', 'P', 'L', 'Z'],
        ['Q', 'V', 'W', 'S'],
        ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']]
    """
    for i in range(1, len(line) - 1, 4):
        if line[i] != " ":
            stack_columns[int(i / 4)].insert(0, line[i])
    return stack_columns


def stack_movement(crates: list, from_row: int, to_row: int, quantity: int):
    """
    The neat part: pop the exact quantity in a buffer, already reversed, and append it to the destination we need
    """
    buffer = []
    for i in range(0, quantity):
        buffer = crates[from_row].pop()
        crates[to_row].append(buffer)


def find_top_stack(crates: list) -> str:
    result = []
    for crate in crates:
        result.append(crate[-1])
    return "".join(result)


pp = pprint.PrettyPrinter(indent=2, width=240)
crates = [[], [], [], [], [], [], [], [], []]
with open("05-input.txt") as f:
    lines = f.readlines()
    for line in lines:
        sanitized_line = line.strip()
        if (
            sanitized_line == ""
            or sanitized_line == "1   2   3   4   5   6   7   8   9"
        ):
            next
        elif sanitized_line[0] == "[":
            build_stack_columns(crates, sanitized_line)
            print("Crate row initial definition updated to:")
            pp.pprint(crates)
        else:
            print("This is a movement def")
            line_regex = re.findall(r"\d+", sanitized_line)
            quantity = int(line_regex[0])
            from_row = int(line_regex[1]) - 1
            to_row = int(line_regex[2]) - 1
            print(f"Moving {quantity} from {from_row} to {to_row}")
            stack_movement(crates, from_row, to_row, quantity)
            pp.pprint(crates)

print(f"The final top stack is {find_top_stack(crates)}")
