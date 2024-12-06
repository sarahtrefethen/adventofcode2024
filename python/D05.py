from functools import cmp_to_key
import math

class Rules:
    before_table: dict
    after_table: dict

    def __init__(self, input):
        self.before_table = {}
        self.after_table = {}
        pairs = [line.split("|") for line in input.splitlines()]
        print(pairs)
        for [a, b] in pairs:
            if a not in self.before_table:
                self.before_table[a] = [b]
            else:
                self.before_table[a].append(b)
            if b not in self.after_table:
                self.after_table[b] = [a]
            else:
                self.after_table[b].append(a)

    def before(self, a, b):
        return b in self.before_table.get(a,[])
    def after(self, a, b):
        return b in self.after_table.get(a,[])
    def compare(self, a, b):
        if self.before(a, b):
            return -1
        elif self.after(a, b):
            return 1
        else:
            return 0


with open('../input/D05.txt', 'r') as file:
    [rules_input, updates_input] = file.read().split("\n\n")

rules = Rules(rules_input)
total = 0
p2total = 0
for line in updates_input.splitlines():
    nums = line.split(",")
    sorted_nums = sorted(nums, key=cmp_to_key(rules.compare))
    midpoint = math.floor(len(nums)/2)
    if nums == sorted_nums:
        total += int(nums[midpoint])
    else:
        p2total += int(sorted_nums[midpoint])

print(f'part1: {total}')
print(f'part2: {p2total}')