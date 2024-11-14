class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []

        for x, y in points:
            dis.append([x, y, math.sqrt(x**2 + y**2)])
        
        dis = sorted(dis, key=lambda c: c[2])
        
        res = []
        c = 0
        for x, y, d in dis:
            res.append([x, y])
            c += 1
            if c == k:
                return res
