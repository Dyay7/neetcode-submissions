class Solution:
    def decodeString(self, s: str) -> str:
        cur = ""
        string_stack = []
        count_stack = []
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                string_stack.append(cur)
                count_stack.append(k)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = string_stack.pop()
                count = count_stack.pop()
                cur += temp * count
            else:
                cur += c
        return cur