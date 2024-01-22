class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return map(itemgetter(0), sorted(dict(Counter(nums)).items(), key=lambda i: i[1], reverse=True)[:k])