class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        size = len(nums)
        sorted_nums = sorted(nums)
        i = 0
        while i < size:
            l = r = i
            while r < size and sorted_nums[r] == sorted_nums[l]:
                r += 1
            dict[sorted_nums[l]] = i
            i = r

        print(dict)
        res = []
        for num in nums:
            res.append(dict[num])
        return res




        
