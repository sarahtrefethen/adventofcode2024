
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self, a_list):
        if len(a_list) == 0:
            raise Exception("LinkedList cannot be initialized empty")
        self.head = Node(a_list[0])
        self.tail = self.head
        self.index = self.head
        for entry in a_list[1:]:
            new_node = Node(entry)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def current(self):
        return self.index.val if self.index else None
    
    def move_forward(self):
        self.index = self.index.next

    def insert(self, val):
        new_node = Node(val)
        if self.index.next:
            new_node.next = self.index.next
            new_node.next.previous = new_node
        new_node.previous = self.index
        self.index.next = new_node
        self.index = new_node
    
    def remove_current(self):
        self.index.previous.next = self.index.next
        self.index.next.previous = self.index.previous
    
    def length(self):
        ptr = self.head
        count = 0
        while(ptr):
            count += 1
            ptr = ptr.next
        return count
    
    def print(self):
        ptr = self.head
        while(ptr):
            print(ptr.val)
            ptr = ptr.next
    
    def set_current_index_val(self, new_val):
        self.index.val = new_val

    def reset_index(self):
        self.index = self.head

class Stones:

    def __init__(self, input):
        self.stones = LinkedList([n for n in input.strip().split(" ")])
    
    def blink(self):
        stone_val = self.stones.current()
        while (stone_val != None):
            # print(stone_val)
            if stone_val == "0":
                self.stones.set_current_index_val("1")
            elif len(stone_val) % 2 == 0:
                first_half = stone_val[0:int(len(stone_val)/2)]
                second_half = stone_val[int(len(stone_val)/2):len(stone_val)]
                self.stones.set_current_index_val(first_half)
                self.stones.insert(str(int(second_half)))
            else:
                self.stones.set_current_index_val(str(int(stone_val)*2024))
            self.stones.move_forward()
            stone_val = self.stones.current()
        self.stones.reset_index()


def part1(input):
    stones = Stones(input)
    for i in range(0,25):
        stones.blink()
    # stones.stones.print()
    return stones.stones.length()

assert part1("125 17") == 55312

with open('../input/D11.txt', 'r') as file:
    input = file.read()

print(f'part 1: {part1(input)}')