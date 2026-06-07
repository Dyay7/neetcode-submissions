class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # it holds [temp, index]

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp: # if we find a temperature warmer than the one at the top of the stack, we discovered the next warmer day for that earlier day
                stack_temp, stack_index = stack.pop()
                res[stack_index] = idx - stack_index
            stack.append((temp, idx))
        return res

