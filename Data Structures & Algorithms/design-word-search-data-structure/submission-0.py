class TrieNode:
    def __init__(self):
        # Each node stores its children in a dictionary:
        #   key = character
        #   value = next TrieNode
        # Using a dict lets us support ANY character and makes "." wildcard easy.
        self.children = {}
        
        # Marks whether a complete word ends at this node
        self.word = False


class WordDictionary:

    def __init__(self):
        # Root of the trie (empty node)
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        # Insert characters one by one
        for c in word:
            # Create a new node if this character path doesn't exist
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node
            cur = cur.children[c]
        # Mark the end of a valid word
        cur.word = True

    def search(self, word: str) -> bool:
        # DFS allows us to branch when encountering "."
        def dfs(j, root):
            cur = root

            # Iterate through the word starting at index j
            for i in range(j, len(word)):
                c = word[i]

                # Case 1: wildcard "."
                if c == ".":
                    # Try ALL possible children because "." can match any letter
                    for child in cur.children.values(): # if we used a dict here we would need to iterate over all the values and many would be None
                        # If ANY path leads to a match, return True
                        if dfs(i + 1, child):
                            return True
                    # If none of the children worked, this path fails
                    return False

                # Case 2: normal character
                else:
                    # If the character path doesn't exist, fail immediately
                    if c not in cur.children:  # O(1) lookup thanks to using a dict
                        return False
                    # Move to the next node
                    cur = cur.children[c]

            # After processing all characters, return True only if
            # we are standing on a node that marks a complete word
            return cur.word

        # Start DFS from the root
        return dfs(0, self.root)
 
