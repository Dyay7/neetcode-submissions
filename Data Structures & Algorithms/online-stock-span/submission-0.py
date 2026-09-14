class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        i = len(self.arr) - 2 # to not take into account today in the loop
        while i >= 0 and self.arr[i] <= price:
            i -= 1
        return len(self.arr) - i - 1 # price:  100  80   60   70 -> len(self.arr) = 4, i = 1, result = 2, because i points to the first value that does not meet the condition


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)