class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            heights[i] = [heights[i], names[i]]
        heights = sorted(heights, key=lambda h_n: (h_n[0], h_n[1]), reverse=True)
        print(heights)
        res = []
        for h, n in heights:
            res.append(n)
        return res
