class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            bit = n & 1 # if the last bit is 0 return 0 and if the last bit is 1 returns 1, it is to get the last one
            result = (result << 1) | bit # shift answer left and append that bit
            n >>= 1 # move to the next bit in n
        return result