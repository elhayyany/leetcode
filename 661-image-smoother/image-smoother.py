class Solution:
    def get_avg(self, x, y, X, Y, img):
        res = 0
        n = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < X and j >= 0 and j < Y:
                    res += img[i][j]
                    n += 1
        return int(res / n)

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(img[0]) for i in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                res[i][j] = self.get_avg(i, j, len(img), len(img[0]), img)
        return res