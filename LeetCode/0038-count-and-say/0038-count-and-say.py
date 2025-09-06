class Solution:
    def countAndSay(self, n: int) -> str:
        def func(n: int) -> str:
            if n == 1:
                return "1"
            
            string = func(n-1)
            m = len(string)
            i = 0
            res = []
            while i < m:
                count = 0
                start = i
                while i < m and string[start] == string[i]:
                    count += 1
                    i += 1
                res.append(str(count))
                res.append(string[start])
            
            return "".join(res)
        
        return func(n)