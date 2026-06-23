class Solution:
    def getSum(self, a: int, b: int) -> int:
        # mask to keep numbers within 32 bits (simulate 32‑bit signed integer behavior)
        mask = 0xFFFFFFFF

        # max positive 32‑bit integer (used to detect negative results)
        max_int = 0x7FFFFFFF

        # keep looping while there is a carry to add
        while b != 0:
            # carry = bits where BOTH a and b have 1s, shifted left because carry affects next bit
            carry = (a & b) << 1

            # sum without carry = XOR (because XOR adds bits without carrying)
            # mask ensures we stay within 32 bits
            a = (a ^ b) & mask

            # next b becomes the carry (also masked to 32 bits)
            b = carry & mask

        # if a is within positive 32‑bit range, return it directly
        if a <= max_int:
            return a

        # otherwise convert from 32‑bit two's complement to Python's negative integer
        return ~(a ^ mask)
