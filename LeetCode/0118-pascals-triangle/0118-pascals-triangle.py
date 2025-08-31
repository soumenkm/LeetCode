class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def getRow(row: int) -> List[int]:
            ans = 1
            res = [1]
            for col in range(1, row):
                ans = ans * (row - col) / col
                res.append(int(ans))
                
            return res
        
        res = []
        for row in range(1, numRows+1):
            res.append(getRow(row))
        
        return res