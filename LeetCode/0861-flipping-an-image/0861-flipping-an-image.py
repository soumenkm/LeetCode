class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        res = [[None for i in range(n)] for i in range(n)]
        for i, row in enumerate(image):
            for j, elem in enumerate(row[::-1]):
                res[i][j] = 0 if elem == 1 else 1
        return res