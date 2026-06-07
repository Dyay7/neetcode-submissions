class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or timestamp < self.store[key][0][0]:
            return ""
        # maximization problem, we want to get the higher timestamp that 
        # meets the condition timestamp_prev <= timestamp
        lo = 0
        hi = len(self.store[key])

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.isLessOrEqual(self.store[key][mid][0], timestamp):
                lo = mid
            else:
                hi = mid
        return self.store[key][lo][1]
    
    def isLessOrEqual(self, num, target):
        return num <= target
