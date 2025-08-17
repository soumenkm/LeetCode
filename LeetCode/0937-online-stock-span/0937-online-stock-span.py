class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        if self.stack:
            pge, pgeIndex = self.stack[-1]
        else:
            pge, pgeIndex = -1, -1

        self.stack.append((price, self.index))
        return self.index - pgeIndex

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)