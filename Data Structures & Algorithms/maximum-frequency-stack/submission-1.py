class FreqStack:

    def __init__(self):
        self.heap = []
        self.count = []
        self.count_map = defaultdict(int)
        

    def push(self, val: int) -> None:
        self.count_map[val] += 1
        heapq.heappush(self.heap, (-self.count_map[val], -(len(self.heap)), val))
        

    def pop(self) -> int:
        freq, idx, val = heapq.heappop(self.heap)
        self.count_map[val] -= 1
        return val  
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()