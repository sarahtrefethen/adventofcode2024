
import numpy

def parse1(input):
    blocks = input.strip().split('\n\n')
    machines = []
    for block in blocks:
        [a_line, b_line, p_line] = block.splitlines()
        ad = [int(substr.split('+')[1]) for substr in a_line.split(': ')[1].split(', ')]
        bd = [int(substr.split('+')[1]) for substr in b_line.split(': ')[1].split(', ')]
        prize = [int(substr.split("=")[1]) for substr in p_line.split(': ')[1].split(", ")]
        machines.append((ad, bd, prize))
    return machines

def parse2(input):
    blocks = input.strip().split('\n\n')
    machines = []
    for block in blocks:
        [a_line, b_line, p_line] = block.splitlines()
        ad = [int(substr.split('+')[1]) for substr in a_line.split(': ')[1].split(', ')]
        bd = [int(substr.split('+')[1]) for substr in b_line.split(': ')[1].split(', ')]
        prize = [int(substr.split("=")[1])+10000000000000 for substr in p_line.split(': ')[1].split(", ")]
        machines.append((ad, bd, prize))
    return machines

def solve(machines):
        total = 0
        for ([ax, ay],[bx, by],[px,py]) in machines:
            if (ax/ay > px/py and bx/by > px/py) or (ax/ay < px/py and bx/by < px/py):
                #small optimization -- some things are non-starters 
                continue 
           
            # this feels like cheating but here we are
            [a,b] = numpy.linalg.lstsq([[ax, bx],[ay,by]],[px,py], rcond=None)[0]
            a=round(a)
            b=round(b)
            if (a*ax + b*bx == px and a*ay + b*by == py):
                total += a*3+b
        return total        

def part1(input):
    machines = parse1(input)
    return solve(machines)

def part2(input):
    machines = parse2(input)
    return solve(machines)

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
    input = file.read()
print(f'part 1: {part1(input)}')
print(f'part 2: {part2(input)}')