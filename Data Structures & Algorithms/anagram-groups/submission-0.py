class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping ChartCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # this is gonna be like the representation of the word, each index will have the count of a ch in the str
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            res[tuple(count)].append(s) # res is {() -> [] , () -> [], ...} the index is a tuple of size 26 and the values the list of strings that match the index
        return list(res.values())

        # O(n * m) time complexity being n the number of strings and m the average size of a string
        # since we loop over all the strings, then loop over all the characters of each string and
        # we update a fixed size array of length 26 -> O(1)

        # Space Complexity
        # We create an array count which is constant size, independent of output -> O(26) = O(1)
        # Number of keys = n
        # Total stored characters across all lists = total input size = n*m
        # But storing the strings is unavoidable, the output itself contains them
        # So it is O(n*m), but if we ignore the output O(n) (for the dictionary keys) [this would be the aux space]
