def blink(stones):
    for stone_val in stones:
        # print(stone_val)
        if stone_val == "0":
            yield "1"
        elif len(stone_val) % 2 == 0:
            first_half = stone_val[0:int(len(stone_val)/2)]
            second_half = stone_val[int(len(stone_val)/2):len(stone_val)]
            yield first_half
            yield str(int(second_half))
        else:
            yield str(int(stone_val)*2024)

def part1(input):
    stones = [n for n in input.strip().split(" ")]
    for i in range(0,25):
        stones = list(blink(stones))
    return len(stones)

memo25 = {}

def blink25(stone):
    if stone in memo25:
        return memo25[stone]
    s = [stone]
    for i in range(0,25):
        s = list(blink(s))  
    memo25[stone] = s
    return s

def blink75(stone):
    print(stone)
    twentyfive = blink25(stone)
    fifty = []
    for stone in twentyfive:
        fifty.extend(blink25(stone))
    total = 0
    for stone in fifty:
        total += len(blink25(stone))
    return total

def part2(input):
    stones = [n for n in input.strip().split(" ")]
    total = 0
    for stone in stones:
        total += blink75(stone)
    return total

assert part1("125 17") == 55312

with open('../input/D11.txt', 'r') as file:
    input = file.read()

print(f'part 1: {part1(input)}')
print(f'part 2: {part2(input)}')