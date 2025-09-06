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
        if node.zero is None and node.one is None:
            return -1

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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(list(set(nums)))
        n = len(nums)
        queries = [(i, val) for i, val in enumerate(queries)]
        queries = sorted(queries, key=lambda elem: elem[1][1])

        def BS(i: int, j: int, key: int) -> int:
            if i > j:
                return i
            mid = (i + j) // 2
            if key == nums[mid]:
                return mid+1
            elif key < nums[mid]:
                return BS(i, mid-1, key)
            else:
                return BS(mid+1, j, key)
        
        def getBitStr(num: int) -> str:
            res = []
            i = 0
            while i < 32:
                num, rem = divmod(num, 2)
                res.append(str(rem)) 
                i += 1
            binaryStr = "".join(res[::-1])
            return binaryStr

        indexList = []
        for _, (x, m) in queries:
            indexList.append(BS(0, n-1, key=m))
        
        binaryNums = []
        for num in nums:
            binaryNums.append(getBitStr(num))
        
        xorRes = [None for i in range(len(indexList))]
        trie = Trie()
        prev = 0
        for i in range(len(indexList)):
            index = indexList[i]
            x = queries[i][1][0]
            resIndex = queries[i][0]
            for string in binaryNums[prev:index]:
                trie.insert(string)
            prev = index
            xor = trie.computeMaxXOR(getBitStr(x))
            xorRes[resIndex] = xor
        
        return xorRes