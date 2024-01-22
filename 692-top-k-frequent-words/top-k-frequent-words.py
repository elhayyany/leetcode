def f(i):
    return (-i[1], i[0])
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return map(itemgetter(0), sorted(Counter(words).items(), key=f)[:k])