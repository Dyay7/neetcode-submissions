class Solution:

    def encode(self, strs: List[str]) -> str:
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
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

        # while i < len(s):
        #     while s[i] != "#":
        #         i += 1
        #     length = int(s[i-1])
        #     res.append(s[i + 1 : i + 1 + length])
        #     i += 1 + length
        # return res