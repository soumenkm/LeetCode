class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def isPalin(string: str) -> bool:
            n = len(string)
            if n == 0 or n == 1:
                return True
            else:
                res = isPalin(string[1:n-1])
                if res and string[0] == string[n-1]:
                    return True
                else:
                    return False

        res = []
        def func(index: int, part: List[str]):
            if index >= n:
                res.append(part.copy())
                return
            else:
                for i in range(index, n):
                    elem = s[index:i+1]
                    if isPalin(elem):
                        part.append(elem)
                        func(i+1, part)
                        part.pop()
        
        func(0, [])
        return res