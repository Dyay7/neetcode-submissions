class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # a collision can only happen with this pattern: positive ->  <- negative,
        # so a negative asteroid can only collide with positive asteroids already sitting in the stack.
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
