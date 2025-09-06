class Node:
    def __init__(self):
        self.zero = None
        self.one = None

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char == "0":
                if node.zero is None:
                    node.zero = Node()
                node = node.zero
            elif char == "1":
                if node.one is None:
                    node.one = Node()
                node = node.one
    
    def computeMaxXOR(self, word: str) -> int:
        node = self.root
        res = [0 for i in range(32)]
        for i, char in enumerate(word):
            if char == "0":
                if node.one is not None:
                    node = node.one
                    res[i] = 1
                else:
                    node = node.zero
            elif char == "1":
                if node.zero is not None:
                    node = node.zero
                    res[i] = 1
                else:
                    node = node.one
        num = 0
        for digit in res:
            num = num * 2 + digit
        return num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def getBitStr(num: int) -> str:
            res = []
            i = 0
            while i < 32:
                num, rem = divmod(num, 2)
                res.append(str(rem)) 
                i += 1
            binaryStr = "".join(res[::-1])
            return binaryStr
        
        binaryNums = []
        for num in nums:
            binaryNums.append(getBitStr(num))
        
        n = len(nums)
        trie = Trie()
        for string in binaryNums:
            trie.insert(string)

        maxNum = 0
        for string in binaryNums:
            xor = trie.computeMaxXOR(string)
            maxNum = max(maxNum, xor)
        
        return maxNum
            

    