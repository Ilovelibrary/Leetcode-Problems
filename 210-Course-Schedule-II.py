class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for ed in prerequisites:
            graph[ed[0]].append(ed[1])
        
        def dfs(i):
            visited[i] = -1
            for j in graph[i]:
                if visited[j]==-1:
                    self.possible = False
                    return
                if visited[j]==0:
                    dfs(j)
            
            visited[i] = 1
            post.append(i)
                
        
        self.possible = True
        post = []
        for i in range(numCourses):
            if visited[i]==0:
                dfs(i)
        return post if self.possible else []