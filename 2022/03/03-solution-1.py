def find_common_element(a, b):
    for char_a in a:
        for char_b in b:
            if char_a == char_b:
                return char_a


def convert_element_priority(e):
    if e.islower():
        # item types a through z have priorities 1 through 26
        return ord(e) - 96
    else:
        # item types A through Z have priorities 27 through 52
        return ord(e) - 38


total = 0
with open("03-input.txt") as f:
    lines = f.readlines()
    for line in lines:
        compartment_length = int(len(line) / 2)
        first_compartment = line[:compartment_length]
        second_compartment = line[compartment_length:].strip()
        common_element = find_common_element(first_compartment, second_compartment)
        print(
            f"The common element between {first_compartment} and {second_compartment} is '{common_element}'"
        )
        total += convert_element_priority(common_element)

print(f"The sum of all common item priorities is {total}")
