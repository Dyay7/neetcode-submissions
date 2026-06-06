class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # first c that is in closeToOpen should have its opening form as the last one added in the stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # if c is not one of the keys in closeToOpen we populate the stack
        return True if not stack else False