class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # if the current value is less than the last one in the stack
                index, height = stack.pop()
                maxArea = max(maxArea, (i-index) * height) # index holds from where we can expand the rectangle
                start = index # we overwrite start with the index of the place from where we can expand the rectangle of height h
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea
