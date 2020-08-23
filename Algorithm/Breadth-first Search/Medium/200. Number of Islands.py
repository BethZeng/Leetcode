'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

Solution:

# BFS / DFS 这题比较经典， 可以直接套模板

# DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 对每个有“1"的位置进行 DFS，把和它四联通的位置全部变成“0”，
        # 这样就能把一个点推广到一个岛。
        # 所以，我们总的进行了 DFS 的次数，就是总过有多少个岛的数目。
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res
        
    # 已知当前是1，把它周围相邻的所有1全部转成0.
    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)
                    
# BFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        que = collections.deque()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    que.append((i, j))
                    while que:
                        x, y = que.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                que.append((nx, ny))
        return res
