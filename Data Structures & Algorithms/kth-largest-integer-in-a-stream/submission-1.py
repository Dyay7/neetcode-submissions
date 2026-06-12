class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.kth = k

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        return self.stream[len(self.stream) - self.kth]