class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        # each time we push one in the minStack we keep track of the min value at that current time
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    
    def pop(self) -> None:
        # if we pop in the main stack we need to pop in hte minStack to have the minimum at the previous point
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]    
