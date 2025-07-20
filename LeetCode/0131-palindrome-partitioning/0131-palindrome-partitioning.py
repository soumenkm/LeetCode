class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        DP = defaultdict(bool)
        def isPalin(string: str) -> bool:
            if DP[string]:
                return DP[string]
            else:
                n = len(string)
                if n == 0 or n == 1:
                    DP[string] = True
                    return True
                else:
                    res = isPalin(string[1:n-1])
                    if res and string[0] == string[n-1]:
                        DP[string] = True
                        return True
                    else:
                        DP[string] = False
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