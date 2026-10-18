class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        res = 0
        directions = [(0,1), (1,0),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for k, l in directions:
                        if 0 <= i + k < len(grid) and 0 <= l + j < len(grid[i]):
                            if grid[i+k][l+j] == 0 :
                                res += 1
                        else:
                            res += 1
        return res