class Solution:
    def smallestNumber(self, num: int) -> int:
        copy = abs(num)
        digits = [int(d) for d in str(copy)]
        digits = sorted(digits, reverse=True) if num < 0 else sorted(digits)

        if num < 0:
            return -1 * int(''.join(map(str, digits)))
        for i, d in enumerate(digits):
            if d != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break
        return int(''.join(map(str, digits)))

        return 0



        
