class Solution:

    def encode(self, strs: List[str]) -> str:
        # We save the len of the string followed by #
        encoded_string = ""
        for s in strs:
            string_code = str(len(s)) + "#"
            encoded_string += string_code + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # we need to get every digit preceding the #, the length can be > 9, that's why it's better to use 2 pointers
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res