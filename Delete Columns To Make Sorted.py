class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cp = 0
        col_size = len(strs[0])
        cnt = 0

        while cp < col_size:
            b = False
            for i in range(1, len(strs)):
                if strs[i][cp] >= strs[i-1][cp]:
                    pass
                else:
                    b = True
                    cnt += 1
                    cp += 1
                    break
            if not b:
                cp += 1
        return cnt

        
