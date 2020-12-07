from day07.part1 import parse


def solve(rules):
    contained_bags = {}
    processed = set()

    while len(processed) < len(rules):
        for color in rules:
            # skip the rule if already processed
            if color in processed:
                continue
            # process the rule if it is an empty bag
            if not len(rules[color]):
                contained_bags[color] = 0
                processed.add(color)
                continue
            # skip if all rules of the contained bags are not processed yet
            if not all([item_color in processed for (_, item_color) in rules[color]]):
                continue
            # process the rule if all rules of contained bags are processed
            bags = 0
            for (quantity, item_color) in rules[color]:
                bags += quantity * (1 + contained_bags[item_color])
            contained_bags[color] = bags
            processed.add(color)

    return contained_bags['shiny gold']


if __name__ == '__main__':
    print(solve(parse('data.txt')))
