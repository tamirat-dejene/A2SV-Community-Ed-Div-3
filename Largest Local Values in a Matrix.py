class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def get_max(i, j):
            max_ = None
            for a in range(i, i + 3):
                max_of_row = max(grid[a][j:j+3])
                max_ = max(max_of_row, max_ if max_ != None else max_of_row)
            return max_
        
        res = [[0 for i in range(n-2)] for _ in range(n-2)]
        s = n-2
        for r in range(s):
            for c in range(s):
                res[r][c] = get_max(r, c)
        return res
