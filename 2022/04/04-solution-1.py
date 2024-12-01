def interval_contained(container: list, contained: list):
    if (int(container[0]) <= int(contained[0])) and (
        int(container[1]) >= int(contained[1])
    ):
        return True
    return False


total = 0
with open("04-input.txt") as f:
    lines = f.readlines()
    for line in lines:
        sanitized_line = line.strip()
        first_pair = sanitized_line.split(",")[0].split("-")
        second_pair = sanitized_line.split(",")[1].split("-")
        if (interval_contained(first_pair, second_pair)) or (
            interval_contained(second_pair, first_pair)
        ):
            total += 1

print(f"The fully contained pairs are {total}")
