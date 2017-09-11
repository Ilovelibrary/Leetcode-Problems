class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(i):
            if visited[i]==-1:
                return False
            if visited[i]==1:
                return True
            visited[i] = -1
            for j in M[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        n = numCourses
        M = [[] for _ in xrange(n)]
        for edge in prerequisites:
            M[edge[0]].append(edge[1])
        visited = [0 for _ in xrange(n)]
        for i in xrange(n):
            if not dfs(i):
                return False
        return True