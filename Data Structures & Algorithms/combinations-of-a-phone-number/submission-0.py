class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            # If the current string has one letter per digit,
            # we have formed a complete combination
            if len(curStr) == len(digits):
                res.append(curStr)   # store the completed combination
                return

            # Otherwise, look at the current digit (digits[i])
            # and try every possible letter it can map to
            for c in digitToChar[digits[i]]:
                # Instead of mutating a list and popping later,
                # we build a NEW string (curStr + c)
                # so no explicit "backtrack" step is needed, strings are inmutable
                backtrack(i + 1, curStr + c)

        # Only start backtracking if digits is non‑empty
        if digits:
            backtrack(0, "")

        return res
