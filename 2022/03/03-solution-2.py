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
    for i in range(0, len(lines) - 1, 3):
        line0 = lines[i].strip()
        line1 = lines[i + 1].strip()
        line2 = lines[i + 2].strip()
        common = list(set(line0) & set(line1) & set(line2))
        if len(common) != 1:
            raise "Nope. That should not happen. By specs, common should be of length 1"

        total += convert_element_priority(common[0])

print(f"The total is {total}")
