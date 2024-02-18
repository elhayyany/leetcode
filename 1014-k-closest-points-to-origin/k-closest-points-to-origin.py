class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = {(x[0], x[1]):[x[0]**2 + x[1]**2, 0] for x in points}
        for x in points:
            dist[(x[0], x[1])][1] += 1
        dist = sorted(dist.items(), key=lambda t:t[1] )
        i = 0
        res = []
        j = 0
        while len(res) < k:
            j = 0
            while len(res) < k and j < dist[i][1][1]:
                res.append(dist[i][0])
                j += 1
            i += 1
        return res