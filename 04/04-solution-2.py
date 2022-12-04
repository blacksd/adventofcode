def overlapping_sections(interval_a: list, interval_b: list):
    # range -> set will be non-inclusive of the last element
    a = range(int(interval_a[0]), int(interval_a[1]) + 1)
    b = range(int(interval_b[0]), int(interval_b[1]) + 1)
    if len(set(a).intersection(set(b))) > 0:
        return True


total = 0
with open("04-input.txt") as f:
    lines = f.readlines()
    for line in lines:
        sanitized_line = line.strip()
        first_pair = sanitized_line.split(",")[0].split("-")
        second_pair = sanitized_line.split(",")[1].split("-")
        if overlapping_sections(first_pair, second_pair):
            total += 1

print(f"The pairs with overlapping sections are {total}")
