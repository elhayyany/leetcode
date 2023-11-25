class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=itemgetter(0))
        res = []
        m = intervals[0]
        for val in intervals:
            if val[0] <= m[1]:
                if val[1] > m[1]:
                    m[1] = val[1]
            else:
                res.append(m)
                m = val
        res.append(m)
        return res