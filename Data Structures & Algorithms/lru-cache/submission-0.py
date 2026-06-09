class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    # def __init__(self, capacity: int):
    #     self.cache = []
    #     self.capacity = capacity

    # def get(self, key: int) -> int:
    #     for i in range(len(self.cache)):
    #         if self.cache[i][0] == key:
    #             tmp = self.cache.pop(i)
    #             self.cache.append(tmp)
    #             return tmp[1]
    #     return -1

    # def put(self, key: int, value: int) -> None:
    #     for i in range(len(self.cache)):
    #         if self.cache[i][0] == key:
    #             tmp = self.cache.pop(i)
    #             tmp[1] = value
    #             self.cache.append(tmp)
    #             return
    #     if self.capacity == len(self.cache):
    #         self.cache.pop(0) # we remove the oldest element (the first one)
    #     self.cache.append([key, value])

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # The most recently used node is in the right side and the least recently used node is in the left side
        # We create a left dummy before the least recently used node and a right dummy after the most recently used node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # helper function to unlink a node by connecting its prev and next nodes
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # helper function to insert node just before right (mark as most recently used)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]