class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        j = n-1
        res = []
        while j >= 0:
            while j >= 0 and s[j] == " ":
                j -= 1
            end = j+1
            while j >= 0 and s[j] != " ":
                j -= 1
            start = j+1
            res.append(s[start: end])
        return " ".join(res).strip()
            