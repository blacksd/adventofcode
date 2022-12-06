with open("06-input.txt") as f:
    lines = f.readlines()
    for line in lines:
        sanitized_line = line.strip()
        for char_sequence in range(0, len(sanitized_line) - 3):
            substring = sanitized_line[char_sequence : char_sequence + 14]
            if len(set(substring)) == len(substring):
                print(
                    f"Found first 14 different chars for substring {substring}, marker is set after character {char_sequence+14}"
                )
                break
