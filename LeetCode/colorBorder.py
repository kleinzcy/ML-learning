# 深度优先搜索，这里主要学习的是列表复制。
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        if grid[r0][c0]==color:
            return grid
        
        # new_grid = grid.copy()
        new_grid = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                new_grid[i][j] = grid[i][j]
        searched = []
        target = grid[r0][c0]
        def search(r,c):
            if (r,c) not in searched:
                searched.append((r,c))
                edge = False

                # top
                if r!=0 and target==grid[r-1][c]:
                    search(r-1, c)
                # left
                if c!=0 and target==grid[r][c-1]:
                    search(r, c-1)
                # down
                if r!=len(grid)-1 and target==grid[r+1][c]:  
                    search(r+1, c)
                # right
                if c!=len(grid[0])-1 and target==grid[r][c+1]:
                    search(r, c+1)
                
                if (r==0 or c==0 or r==len(grid)-1 or c==len(grid[0])-1) or (target!=grid[r-1][c] or target!=grid[r][c-1] or target!=grid[r+1][c] or target!=grid[r][c+1]):
                    new_grid[r][c] = color


                    
        search(r0, c0)
        
        return new_grid
