class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        size = len(sorted_nums)
        num_of_op = 0
        j = 0

        while True:
            # largest
            largest = sorted_nums[0]
            while j + 1 < size and sorted_nums[j + 1] == largest:
                j += 1
            
            # next largest index
            j += 1

            if j == size:
                return num_of_op
            
            num_of_op += j
            sorted_nums[0] = sorted_nums[j]

        return num_of_op


        
