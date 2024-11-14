class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)

        sum_ = 0

        for i, cost in enumerate(sorted_costs):
            sum_ += cost
            if sum_  > coins:
                return i
        
        return len(costs)
