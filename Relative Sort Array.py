class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = 0
        res = []
        for num in arr2:
            cnt = arr1.count(num)
            res += [num] * cnt
        res += sorted([num for num in arr1 if num not in arr2])
        return res
