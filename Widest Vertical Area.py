class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_cord = sorted(points, key=lambda point: point[0])
        widest = 0

        for i in range(1, len(sorted_cord)):
            widest = max(widest, sorted_cord[i][0] - sorted_cord[i-1][0])
        return widest
