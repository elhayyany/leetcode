class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        temp = [0,0]
        for i in range(1, len(points)):
            temp[0] = abs(points[i][0] - points[i - 1][0])
            temp[1] = abs(points[i][1] - points[i - 1][1])
            res += max(temp)
        return res