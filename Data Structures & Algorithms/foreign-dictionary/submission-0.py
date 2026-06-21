class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            # If we've already visited this character before,
            # return its stored value:
            #   True  → means this node is currently in the recursion stack (cycle)
            #   False → means this node is fully processed (safe)
            if char in visited:
                return visited[char]

            # Mark this node as "in the recursion stack".
            # This is how we detect cycles.
            visited[char] = True

            # Explore all neighbors (characters that must come AFTER this one)
            for neighChar in adj[char]:
                # If DFS returns True, it means a cycle was found.
                if dfs(neighChar):
                    return True

            # If we reach here, no cycle was found from this node.
            # Mark it as fully processed.
            visited[char] = False

            # Add this character to the topological order.
            res.append(char)


        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)