class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums += nums[::1]
        return nums
