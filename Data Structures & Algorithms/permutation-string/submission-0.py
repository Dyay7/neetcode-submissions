class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # try also with counts, hashmap with counts and move fixed window
        # sorted_s1 = sorted(s1)
        # print(sorted_s1)
        # l = 0
        # r = len(s1)
        # while r < len(s2):
        #     if sorted(s2[l:r]) == sorted_s1:
        #         return True
        #     else:
        #         print([s2[l:r]])
        #         l += 1
        #         r += 1
        # return False

        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: #the count was equal before, but know it is not since we added 1 to s2Count[index]
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
            
