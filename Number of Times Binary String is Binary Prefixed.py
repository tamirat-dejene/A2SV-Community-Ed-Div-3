class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        size = len(flips)
        pre_sum = 0
        cnt = 0

        for i, flip in enumerate(flips):
            pre_sum += flip
            if pre_sum == int((i + 1) * ((i + 1)  + 1) / 2):
                cnt += 1
        return cnt
