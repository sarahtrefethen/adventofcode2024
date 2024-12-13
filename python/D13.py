
def parse(input):
    blocks = input.strip().split('\n\n')
    machines = []
    for block in blocks:
        [a_line, b_line, p_line] = block.splitlines()
        ad = [int(substr.split('+')[1]) for substr in a_line.split(': ')[1].split(', ')]
        bd = [int(substr.split('+')[1]) for substr in b_line.split(': ')[1].split(', ')]
        prize = [int(substr.split("=")[1]) for substr in p_line.split(': ')[1].split(", ")]
        machines.append((ad, bd, prize))
    return machines

def part1(input):
    machines = parse(input)
    total = 0
    for ([ax, ay],[bx, by],[px,py]) in machines:
        # solve for the smallest combined values of a,b where:
        # a*ax + b*bx == px
        # a*ay + b*by == py
        solutions = []
        for a in range(0,100):
            for b in range(0,100):
                if (a*ax + b*bx == px and a*ay + b*by == py):
                    solutions.append((a, b))
        if len(solutions) > 0:
            total += min([a*3+b for (a,b) in solutions])
    
    return total


assert part1(
    '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''
) == 480

with open('../input/D13.txt', 'r') as file:
    print(f'part 1: {part1(file.read())}')