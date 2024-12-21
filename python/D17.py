
import math

class Machine:
    def __init__(self, registers):
        [self.A, self.B, self.C] = registers
        self.output = ''

    def print(self):
        print(f'A: {self.A}')
        print(f'B: {self.B}')
        print(f'C: {self.C}')
        print(f'output: {self.output}')

    def combo(self, operand: int):
        if operand <= 3:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        raise Exception("program is not valid")

    # returns the new cursor value
    def execute(self, program, cursor):
        opcode = program[cursor]
        operand = program[cursor + 1]
        if opcode == 0:
            self.adv(operand)
            return cursor + 2
        if opcode == 1:
            self.bxl(operand)
            return cursor + 2
        if opcode == 2:
            self.bst(operand)
            return cursor + 2
        if opcode == 3: #jnz
            if self.A == 0:
                return cursor + 2
            else:
                return operand
        if opcode == 4:
            self.bxc(operand)
            return cursor + 2
        if opcode == 5:
            self.out(operand)
            return cursor + 2
        if opcode == 6:
            self.bdv(operand)
            return cursor + 2
        if opcode == 7:
            self.cdv(operand)
            return cursor + 2

    def adv(self, operand):
        self.A = int(self.A / math.pow(2, self.combo(operand)))
    def bxl(self, operand):
        self.B = self.B^operand
    def bst(self, operand):
        self.B = self.combo(operand) % 8
    def bxc(self, operand):
        self.B = self.B^self.C
    def out(self, operand):
        result = str(self.combo(operand) % 8)
        if self.output == "":
            self.output = result
        else:
            self.output += "," + result
    def bdv(self, operand):
        self.B = int(self.A / math.pow(2, self.combo(operand)))
    def cdv(self, operand):
        self.C = int(self.A / math.pow(2, self.combo(operand)))
        


def part1(machine: Machine, program: list[int]):
    cursor = 0
    while cursor < len(program):
        cursor = machine.execute(program=program, cursor=cursor)
        machine.print()

    return machine.output

def parse(txt):
    [top, bottom] = txt.strip().split('\n\n')
    machine = Machine([int(st.split(": ")[1]) for st in top.splitlines()])
    program = [int(n) for n in bottom.split(":")[1].split(",")]  
    return(machine, program)


example = '''
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''

example2 = '''
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4'''

example3 = '''
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''

assert part1(*parse(example)) == "4,6,3,5,6,3,5,2,1,0"
assert part1(*parse(example2)) == "0,1,2"
assert part1(*parse(example3)) == "4,2,5,6,7,7,7,7,3,1,0"

with open("../input/D17.txt", "r") as file:
    txt = file.read()

print(f'part1: {part1(*parse(txt))}')