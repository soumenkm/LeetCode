class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            n, rem = divmod(n, 2)
            num = num * 2 + rem
        return num