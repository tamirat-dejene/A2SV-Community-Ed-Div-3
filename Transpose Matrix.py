class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        # m * n --> n * m

        res = [[0 for _ in range(m)] for _ in range(n)]

        rp = cp = 0

        for i in range(n):
            for j in range(m):
                res[i][j] = matrix[rp][cp]

                if rp < m - 1:
                    rp += 1
                else:
                    rp = 0
                    cp += 1
        return res

        
