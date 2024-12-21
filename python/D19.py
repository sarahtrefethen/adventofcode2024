
def is_possible(pattern, available_towels):
    queue = [(pattern)]
    while len(queue) > 0:
        queued_p = queue.pop(0)
        if queued_p in available_towels:
            return True
        for i in range(1, len(queued_p)):
            segment = queued_p[:i]
            if segment in available_towels:
                queue.append(queued_p.removeprefix(segment))
    return False


def part1(input):

    [top, bottom] = input.strip().split('\n\n')

    available_towels = set(top.split(', '))


    filtered_towels = set()
    for towel in available_towels: 
        if not is_possible(towel, available_towels-{towel}):
            filtered_towels.add(towel)

    target_patterns = bottom.splitlines()

    total = 0
    for pattern in target_patterns:
        if is_possible(pattern, filtered_towels):
            total += 1

    return total


example = '''
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''

assert part1(example) == 6

with open("../input/D19.txt", "r") as file:
    input = file.read()

print(f'part 1: {part1(input)}')