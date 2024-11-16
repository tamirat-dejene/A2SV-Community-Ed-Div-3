class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr)
        if size < 3:
            return False
        peak = max(arr)
        peak_index = arr.index(peak)

        if peak_index == size - 1 or peak_index == 0:
            return False

        i = peak_index
        j = peak_index

        while i - 1 >= 0:
            if arr[i-1] >= arr[i]:
                return False
            i -= 1
        while j + 1 < size:
            if arr[j + 1] >= arr[j]:
                return False
            j += 1
        return True



