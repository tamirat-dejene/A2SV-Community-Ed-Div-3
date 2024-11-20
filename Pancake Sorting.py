class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def pancake(end):
            if end == 0:
                return
            
            # get index of max element
            max_index = arr.index(max(arr[:end + 1:]))
            
            # put the max at start / reverse 0 - max_index
            arr[0:max_index + 1:] = arr[max_index::-1]

            # reverse the whole array to put the max at the end
            arr[:end + 1:] = arr[end::-1]

            # Append the two flips to result
            res.append(max_index + 1)
            res.append(end + 1)

            # recurse
            pancake(end - 1)
        
        pancake(len(arr) - 1)
        
        return res
