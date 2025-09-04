class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # i = 0
        # n = len(strs)
        # lenList = [len(s) for s in strs]
        # minN = min(lenList)
        # prefix = []
        # flag = True
        # while flag and i < minN:
        #     char = strs[0][i]
        #     for j in range(1, n):
        #         if strs[j][i] != char:
        #             flag = False
        #             break
        #     else:
        #         prefix.append(char)
        #     i += 1
        
        # return "".join(prefix)

        strs.sort()
        first = strs[0]
        last = strs[-1]

        n1 = len(first)
        n2 = len(last)
        n = min(n1, n2)
        i = 0
        charList = []
        while i < n:
            if first[i] == last[i]:
                charList.append(first[i])
            else:
                break
            i += 1
        return "".join(charList)