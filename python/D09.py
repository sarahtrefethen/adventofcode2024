

class Compactor:
    input: str
    head: int
    tail: int
    checksum_total: int
    checksum_index: int
    compacted: str
    added: set

    def __init__(self, input):
        print(f'received input of length {len(input)}')
        if len(input) % 2 ==1:
            self.input = input+'0'
        else:
            self.input = input
        self.head = 0
        self.tail = len(self.input)-2 
        self.checksum_total = 0
        self.checksum_index = 0
        self.compacted = ''
        self.added = set()

    def move_head(self):
        # print(f'moving head from {self.head}')
        self.head += 2
        # print(f'new head block: {self.head_block()}')
    def move_tail(self):
        # print(f'moving tail from {self.tail}')
        self.tail -= 2
    def head_block(self):
        pair = self.input[self.head:self.head+2]
        # print(f'head block {pair}')
        return (int(self.head/2), int(pair[0]), int(pair[1]))
    def tail_block(self):
        pair = self.input[self.tail:self.tail+2]
        # print(f'tail block {pair}')
        return (int(self.tail/2), int(pair[0]), int(pair[1]))
    def add_range_to_checksum(self, count: int, val:int):
        # print(f'adding {count} instances of {val} starting at {self.checksum_index}')
        for i in range(self.checksum_index, self.checksum_index+count):
            # self.compacted += str(val)
            self.checksum_total += val*i
        self.checksum_index += count
    def reallocate(self):
        (h_index, h_blocks, h_space) = self.head_block()
        (t_index, t_blocks, t_space) = self.tail_block()
        self.add_range_to_checksum(val=h_index, count=h_blocks)

        while True:
            if h_space <= 0:
                self.move_head()
                (h_index, h_blocks, h_space) = self.head_block()
                # print(f" added: {self.added}")
                # print(f'{self.compacted}')
                if h_index in self.added:
                    # print(f'already added {h_index}')
                    break
                if h_index != t_index:
                    self.add_range_to_checksum(val=h_index, count=h_blocks)
                    # print(f'adding {h_index} to added')
                    self.added.add(h_index)
                    if h_space == 0:
                        continue
            
            if t_blocks == 0:
                self.added.add(t_index)
                if self.tail <= 0:
                    break
                self.move_tail()
                (t_index, t_blocks, t_space) = self.tail_block()
                if t_index in self.added:
                    # print(f'already added {t_index}')
                    break
            

            if t_blocks > 0 and h_space > 0 and t_index not in self.added:
                self.add_range_to_checksum(val=t_index, count=1)

            if self.head >= len(self.input)-2:
                # print(f'head is {self.head}, attaching final tail blocks and breaking')
                self.add_range_to_checksum(val=t_index, count=t_blocks)
                break
            t_blocks -= 1
            h_space -= 1

    
    def get_checksum(self):
        # print(self.input)
        # print(self.compacted)
        return self.checksum_total


with open('../input/D09.txt', 'r') as file:
    input = file.read()

compactor = Compactor(input)

compactor.reallocate()

print(f'part 1: {compactor.get_checksum()}')
