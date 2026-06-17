class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list: course -> list of prerequisites
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []        # topological order (postorder)
        visit = set()      # courses that are fully processed (safe, no cycles)
        cycle = set()      # courses currently in the DFS recursion stack

        def dfs(crs):
            # If we revisit a course in the current DFS path → cycle
            if crs in cycle:
                return False

            # If already processed before, no need to redo work
            if crs in visit:
                return True

            # Mark this course as being explored in the current path
            cycle.add(crs)

            # DFS on all prerequisites
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            # Done exploring this course → remove from cycle path
            cycle.remove(crs)

            # Mark as fully processed
            visit.add(crs)

            # Add to topological order (postorder)
            output.append(crs)

            return True

        # Run DFS on every course
        for c in range(numCourses):
            if dfs(c) == False:
                return []   # cycle detected → no valid order

        return output        # valid topological order
