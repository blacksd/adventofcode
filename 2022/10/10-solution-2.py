import pprint

pp = pprint.PrettyPrinter(indent=2)
if __name__ == "__main__":
    with open("10-input.txt") as f:
        lines = f.readlines()
        registry_buffer = [0, 0]
        registry_x = 1
        sprite = range(0, 3)
        cycle_count = 0
        display = [[], [], [], [], [], []]
        for line in lines:
            sanitized_line = line.strip()
            instruction = sanitized_line.split()[0]
            if instruction == "addx":
                cycles = 2
                registry_buffer[0] = int(sanitized_line.split()[1])
            else:
                cycles = 1
            for cycle in range(0, cycles):
                cycle_count += 1
                print(
                    f"During cycle {cycle_count} registry X is {registry_x} and buffer is {registry_buffer}"
                )
                current_line = int((cycle_count - 1) / 40)
                position = (cycle_count - 1) % 40
                if position in sprite:
                    pixel = "█"
                    # pixel = "#"
                else:
                    pixel = "░"
                    # pixel = "."
                display[current_line].append(pixel)
                print(
                    f"Line {current_line} position {position} cycle {cycle_count} registry X is {registry_x} sprite is {sprite} pixel {pixel}"
                )
                if registry_buffer:
                    registry_x += registry_buffer[1]
                    registry_buffer[1] = registry_buffer[0]
                    registry_buffer[0] = 0
                sprite = range(registry_x - 1, registry_x + 2)
                # print(f"At the end of cycle {cycle_count} registry X is {registry_x}")


pp.pprint(["".join(line) for line in display])
