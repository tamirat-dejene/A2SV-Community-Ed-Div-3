class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hm = {}
        cnt = 0

        for word in words:
            w = ''.join(sorted(list(set(list(word)))))
            print(w)
            hm[w] = hm.get(w, 0) + 1

        def factorial(n: int):
            return 1 if n == 0 else n * factorial(n-1)
        
        # calculate the number of combinations
        '''
            C(n)/ (C(n-2) * C(2)) - number of distinct pairs that can be formed
        '''
        for w in hm:
            n = hm.get(w)
            if n > 1:
                cnt += int(factorial(n) /(2 * factorial(n - 2)))
        
        return cnt
        
