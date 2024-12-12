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

assert part1("125 17") == 55312

with open('../input/D11.txt', 'r') as file:
    input = file.read()

print(f'part 1: {part1(input)}')