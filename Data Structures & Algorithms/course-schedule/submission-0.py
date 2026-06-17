class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()  # courses in the current DFS path

        def dfs(crs):
            if crs in visiting:
                return False  # cycle detected

            if preMap[crs] == []:
                return True  # no prerequisites left

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            preMap[crs] = []  # memoization, once a course is confirmed to have no cycles (it's 
                                # prereq returned True) we delete de prereq from that course
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
