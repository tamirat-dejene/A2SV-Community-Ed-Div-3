class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mon_stack = []
        mon_stack.append(-1)

        for num in reversed(arr):
            top = mon_stack[-1]
            if num > top:
                mon_stack.append(num)
            else:
                mon_stack.append(top)
        mon_stack.pop()
        return list(reversed(mon_stack))
        
