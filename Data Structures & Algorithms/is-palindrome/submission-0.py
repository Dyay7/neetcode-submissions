class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # we first check if we have a alphanumeric char, if not we move the index to the next one
            while l < r and not self.is_alphanum(s[l]):
                l += 1
            while r > l and not self.is_alphanum(s[r]):
                r -= 1
            # if the chars don't match then it is False
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def is_alphanum(self, ch: str) -> bool:
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))
        # we add capital letters for completness, although we do lower() the letters so we won't have capital letters
