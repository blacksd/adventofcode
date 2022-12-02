with open('01-input.txt') as f:
    lines = f.readlines()
    elf = 0
    output = { "0": 0 }
    for line in lines:
      if line == "\n":
        elf += 1
        output[str(elf)] = 0
      else:
        output[str(elf)] += int(line)

sorted_values = sorted(output.values())
print("Max elf: {}".format(sorted_values[-1]))
print("Top three elfs: {}".format(sorted_values[-3:]))
print("Top three elfs sum: {}".format(sum(sorted_values[-3:])))
