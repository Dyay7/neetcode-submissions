class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list:
        # edges[u] = list of (v, w) meaning: from u → v with travel time w
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        # Min-heap for Dijkstra:
        # (current_time, node)
        # Start at node k with time 0.
        minHeap = [(0, k)]

        # Set of nodes whose shortest time has been finalized.
        visit = set()

        # Tracks the maximum time among all shortest paths.
        t = 0

        # Standard Dijkstra's algorithm.
        while minHeap:
            # Pop the node with the smallest known arrival time.
            w1, n1 = heapq.heappop(minHeap)

            # If we've already finalized this node, skip it.
            if n1 in visit:
                continue

            # Mark this node as finalized.
            visit.add(n1)

            # Update the answer: this is the shortest time to reach n1.
            t = w1

            # Explore neighbors.
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # Push the new candidate time to reach n2.
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # If we visited all nodes, return the maximum shortest-path time.
        # Otherwise, some node was unreachable → return -1.
        return t if len(visit) == n else -1
