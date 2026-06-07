class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            stack.append((target - p) / s) # seconds to reach the target
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop() 
                # if the seconds to reach the target of the new element is less or equal to the time before it
                # then the car forms a fleet so we can pop it from the stack
                # if it doesn't, at the top of the stack it's gonna be a new time that marks the 2nd fleet and
                # posterior timestamps would check against that 2nd time and so on
        return len(stack)
        
