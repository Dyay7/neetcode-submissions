class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l, r = 0, k
        # retArray = []

        # while r <= len(nums):
        #     retArray.append(max(nums[l:r])) # this is O(k) so it makes the algo become O(n*k) where n = len(nums)
        #     l+=1
        #     r+=1

        # return retArray

        output = []
        q = deque() # this will store the indexes of elements in decreasing order of their values
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # q[-1] is the right side of the queue, the backside
                q.pop()
            q.append(r) # we append to the right

            if l > q[0]:
                q.popleft() # we delete the element from the left side of the queue, from the front
                # this is because the left pointer passed the front index, so we remove it because it is outside the window

            if (r+1) >= k: # at first full window the condition is r+1 == k, from that point onwards r+1 > k
                output.append(nums[q[0]]) # q[0] is the left side of the queue, the frontside
                l += 1
            r += 1
        return output