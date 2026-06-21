class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the endWord is not even in the dictionary, no transformation is possible.
        if endWord not in wordList:
            return 0

        # nei maps a pattern like "h*t" to all words that match that pattern.
        # Example: "hot", "hit", "hut" all map to "h*t".
        nei = collections.defaultdict(list)

        # Include beginWord in the list so we can generate patterns for it too.
        wordList.append(beginWord)

        # Build the pattern → word adjacency.
        # For each word, replace each character with '*' to create a pattern.
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # Standard BFS setup.
        # visit ensures we don't revisit words (prevents cycles).
        visit = set([beginWord])
        q = deque([beginWord])

        # res counts the number of transformation steps (levels in BFS).
        res = 1

        # BFS: shortest path in an unweighted graph.
        while q:
            # Process one BFS level at a time.
            for i in range(len(q)):
                word = q.popleft()

                # If we reached the target word, return the number of steps.
                if word == endWord:
                    return res

                # Try all possible one-letter transformations.
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    # All words that match this pattern are neighbors.
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            # After finishing one BFS layer, increase the transformation count.
            res += 1

        # If BFS finishes without finding endWord, no transformation exists.
        return 0
