class Solution:
    def reverseString(self, s: List[str]) -> None:
        size= len(s)
        mid = size // 2
        
        to_l = mid - 1 if size % 2 == 0 else mid
        to_r = mid 

        while to_l >= 0 and to_r < size:
            temp = s[to_l]
            s[to_l] = s[to_r]
            s[to_r] = temp

            to_l -= 1
            to_r += 1
        
        
