class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat
        res = [[0 for i in range(c)] for j in range(r)]
        
        # reshape
        rp = cp = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = mat[rp][cp]
                if cp < n - 1:
                    cp += 1
                else:
                    cp = 0
                    rp += 1
        return res






        




        
