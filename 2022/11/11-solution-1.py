import logging

logging.basicConfig(level=logging.INFO)


class Monkey:
    def __init__(self, name: str, worry_levels: list, operation, test):
        self.name = name
        self.worry_levels = worry_levels
        self.operation = operation
        self.test = test
        self.inspection_count = 0
        # logging.debug(f"Created instance {self.name} with id {id(self)}")

    def set_target_monkeys(self, monkeys: list):
        self.target_monkey_true = monkeys[0]
        self.target_monkey_false = monkeys[1]

    def inspect(self):
        logging.info(
            f"Starting inspection of {self.name} for worry levels {self.worry_levels}"
        )

        def throw(worry_level: int):
            if self.test(worry_level):
                logging.debug(f"Item is thrown to {self.target_monkey_true.name}")
                self.target_monkey_true.worry_levels.append(worry_level)
            else:
                logging.debug(f"Item is thrown to {self.target_monkey_false.name}")
                self.target_monkey_false.worry_levels.append(worry_level)

        for index, worry_level in enumerate(self.worry_levels):
            logging.debug(f"Examining item {index}")
            current_worry_level = int(self.operation(worry_level) / 3)
            logging.debug(
                f"Worry level after monkey gets bored is {current_worry_level}"
            )
            throw(current_worry_level)
            self.inspection_count += 1
        logging.debug("Resetting worry levels")
        self.worry_levels = []


def divisible_by(div_by: int):
    return lambda n: (n % div_by) == 0


def multiply_by(mult_by: int):
    return lambda n: n * mult_by


def sum_with(sum_with: int):
    return lambda n: n + sum_with


def sum_with(sum_with: int):
    return lambda n: n + sum_with


if __name__ == "__main__":
    with open("11-input.txt") as f:
        lines = f.readlines()
        monkey_definitions = {}
        for line in lines:
            sanitized_line = line.strip()
            if sanitized_line[0:6] == "Monkey":
                id = sanitized_line[7]
                monkey_definitions[id] = {"target_monkeys": []}
            elif sanitized_line[0:8] == "Starting":
                monkey_definitions[id]["worry_levels"] = [
                    int(item) for item in sanitized_line[16:].split(", ")
                ]
            elif sanitized_line[0:9] == "Operation":
                operation = sanitized_line[17:].split(" ")
                if operation[1] == "+":
                    monkey_definitions[id]["operation"] = sum_with(int(operation[2]))
                elif operation[1] == "*":
                    if operation[0] == operation[2] == "old":
                        monkey_definitions[id]["operation"] = lambda n: n * n
                    else:
                        monkey_definitions[id]["operation"] = multiply_by(
                            int(operation[2])
                        )
            elif sanitized_line[0:4] == "Test":
                test_condition = sanitized_line[6:]
                if test_condition[0:12] == "divisible by":
                    monkey_definitions[id]["test"] = divisible_by(
                        int(test_condition[13:])
                    )
            elif sanitized_line[3:7] == "true":
                destination_monkey_true = int(sanitized_line[-1])
                monkey_definitions[id]["target_monkeys"].append(destination_monkey_true)
            elif sanitized_line[3:8] == "false":
                destination_monkey_false = int(sanitized_line[-1])
                monkey_definitions[id]["target_monkeys"].append(
                    destination_monkey_false
                )

# monkeys = [0, 1, 2, 3]
# monkeys[0] = Monkey(monkeys[0], [79, 98], lambda l: l * 19, divisible_by(23))
# monkeys[1] = Monkey(monkeys[1], [54, 65, 75, 74], sum_with(6), divisible_by(19))
# monkeys[2] = Monkey(monkeys[2], [79, 60, 97], lambda l: l * l, divisible_by(13))
# monkeys[3] = Monkey(monkeys[3], [74], sum_with(3), divisible_by(17))
#
# monkeys[0].set_target_monkeys([monkeys[2], monkeys[3]])
# monkeys[1].set_target_monkeys([monkeys[2], monkeys[0]])
# monkeys[2].set_target_monkeys([monkeys[1], monkeys[3]])
# monkeys[3].set_target_monkeys([monkeys[0], monkeys[1]])
#
# monkeys[0].inspect()
# monkeys[1].inspect()
# monkeys[2].inspect()
# monkeys[3].inspect()

monkeys = []
for monkey in monkey_definitions.keys():
    monkeys.append(
        Monkey(
            int(monkey),
            monkey_definitions[monkey]["worry_levels"],
            monkey_definitions[monkey]["operation"],
            monkey_definitions[monkey]["test"],
        )
    )

for monkey in monkey_definitions:
    target_monkeys = [
        monkeys[monkey_definitions[monkey]["target_monkeys"][0]],
        monkeys[monkey_definitions[monkey]["target_monkeys"][1]],
    ]
    monkeys[int(monkey)].set_target_monkeys(target_monkeys)

for i in range(0, 20):
    for monkey in monkeys:
        monkey.inspect()

inspection_counts = []
for monkey in monkeys:
    logging.info(
        f"After {i + 1} rounds, worry levels for monkey {monkey.name} are {monkey.worry_levels} and its inspection count is {monkey.inspection_count}"
    )
    inspection_counts.append(monkey.inspection_count)


result = 1
for element in sorted(inspection_counts)[-2 : len(inspection_counts)]:
    result = result * element

print(f"The total is {result}")
