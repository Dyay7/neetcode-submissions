class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # A max-heap is perfect for this because it lets us efficiently extract the largest values.
        # Most languages provide min-heaps, so a common trick is to store negative values.
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: # in this case add first-second to the heap, else both are destroyed
                heapq.heappush(stones, first-second)
        
        # we return the absolute value of the remaining stone
        stones.append(0) # if None remain
        return abs(stones[0])

