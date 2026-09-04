class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        res = 0
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        return res

        # O(1) or O(n) space complexity depending on the sorting algo, O(nlogn) time complexity

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m+1)
        for p in people:
            count[p] += 1  # count has the frequency of each weight [0, 1, 2, 2] for [1, 3, 2, 3, 2]

        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0: 
                i += 1
            people[idx] = i # The next smallest remaining person's weight is i, so put that weight into the next
                            # position of the sorted array
            count[i] -= 1
            idx += 1        
    
        l = 0
        r = len(people) - 1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        return res
        # O(m) space complexity, O(n) time complexity