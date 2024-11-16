class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return not any(i for i in range(left, right + 1) if not any(left <= i <= right for left, right in ranges))


        
