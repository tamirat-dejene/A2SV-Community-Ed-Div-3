class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        # Make bob pick the smallest pile,
        # Since I and ALice get to pick first we got the chance to pick max, since get 2, I wanna maximize mine [next max]
        bob = 0
        me = len(piles) - 2
        # alice = len(piles) - 1

        tot = 0
        while True:
            tot += sorted_piles[me]
            if bob + 1 == me:
                return tot
            me -= 2
            bob += 1


        
