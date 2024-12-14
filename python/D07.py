
def plus(a, b):
    return a+b
def mul(a,b):
    return a*b
def concat(a,b):
    return int(str(a)+str(b))

def test1(target: int, inputs:list[int]):
    print(f"******** {target} ***********")
    queue = [(inputs[0], inputs[1:], plus, ["+"]), (inputs[0], inputs[1:],mul, ["*"])]
    while len(queue) > 0:
        (total, to_process, operation, history) = queue.pop(0)
        next_total = operation(total, to_process.pop(0))
        if len(to_process) > 0:
            queue.append((next_total, to_process[:], plus, [*history, "+"]))
            queue.append((next_total, to_process[:], mul, [*history, "*"]))
        elif next_total == target:
            print(history)
            print(inputs)
            return True
    return False

def test2(target: int, inputs:list[int]):
    print(f"******** {target} ***********")
    queue = [
        (inputs[0], inputs[1:], plus, ["+"]), 
        (inputs[0], inputs[1:],mul, ["*"]),
        (inputs[0], inputs[1:],concat, ["||"])
        ]
    while len(queue) > 0:
        (total, to_process, operation, history) = queue.pop(0)
        next_total = operation(total, to_process.pop(0))
        if len(to_process) > 0:
            queue.append((next_total, to_process[:], plus, [*history, "+"]))
            queue.append((next_total, to_process[:], mul, [*history, "*"]))
            queue.append((next_total, to_process[:], concat, [*history, "||"]))
        elif next_total == target:
            print(history)
            print(inputs)
            return True
    return False

def part1(input):
    sum = 0
    lines = [(int(line.split(': ')[0]),[int(n) for n in line.split(': ')[1].split(" ")]) for line in input.strip().splitlines()] 
    for (target, inputs) in lines:
        if test1(target, inputs):
            sum+=target
    return sum


def part2(input):
    sum = 0
    lines = [(int(line.split(': ')[0]),[int(n) for n in line.split(': ')[1].split(" ")]) for line in input.strip().splitlines()] 
    for (target, inputs) in lines:
        if test2(target, inputs):
            sum+=target
    return sum


assert part1('''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
             ''') == 3749

assert part2('''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
             ''') == 11387

with open('../input/D07.txt', 'r') as file:
    input = file.read()

print(f'part 2: {part2(input)}')