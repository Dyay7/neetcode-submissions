class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list where each source maps to a list of destinations.
        # We only include sources that appear in tickets.
        adj = {src: [] for src, dst in tickets}

        # Sort tickets lexicographically so that when we explore,
        # we always choose the smallest lexical option first.
        tickets.sort()

        # Fill adjacency list in sorted order.
        for src, dst in tickets:
            adj[src].append(dst)
        
        # The itinerary must start at JFK.
        res = ["JFK"]

        def dfs(src):
            # If we have used all tickets, the itinerary is complete.
            # res should contain exactly len(tickets) + 1 airports.
            if len(res) == len(tickets) + 1:
                return True

            # If src has no outgoing flights, we cannot continue.
            if src not in adj:
                return False
            
            # Copy the current list of destinations so we can modify adj[src]
            # while iterating without breaking the loop.
            temp = list(adj[src])

            # Try each possible next destination in lexical order.
            for i, v in enumerate(temp):
                # Choose this ticket: remove it from adjacency.
                adj[src].pop(i)

                # Add destination to the current path.
                res.append(v)

                # Continue DFS from the chosen destination.
                if dfs(v):
                    return True

                # Backtrack:
                # Put the ticket back exactly where it was.
                adj[src].insert(i, v)

                # Remove the destination from the current path.
                res.pop()

            # No valid itinerary found from this source.
            return False

        # Start DFS from JFK.
        dfs("JFK")
        return res
