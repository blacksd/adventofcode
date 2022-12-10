if __name__ == "__main__":
    with open("10-input.txt") as f:
        lines = f.readlines()
        signal_strenghts = []
        registry_buffer = [0, 0]
        registry_x = 1
        cycle_count = 0
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
                # print(
                #     f"During cycle {cycle_count} registry X is {registry_x} and buffer is {registry_buffer}"
                # )
                if (cycle_count - 20) % 40 == 0:
                    signal_strenghts.append(registry_x * cycle_count)
                    print(
                        f"On cycle {cycle_count} registry X is {registry_x} and strength is {registry_x * cycle_count}"
                    )
                if registry_buffer:
                    registry_x += registry_buffer[1]
                    registry_buffer[1] = registry_buffer[0]
                    registry_buffer[0] = 0
                # print(f"At the end of cycle {cycle_count} registry X is {registry_x}")

print(f"The sum of the signal strenghts is {sum(signal_strenghts)}")
