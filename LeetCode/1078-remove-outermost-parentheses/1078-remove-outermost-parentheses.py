class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0
        for par in s:
            if count > 0 and par == "(":
                res.append("(")
                count += 1
            elif count > 1 and par == ")":
                res.append(")")
                count -= 1
            elif count == 0 and par == "(":
                count += 1
            elif count == 1 and par == ")":
                count -= 1
                
        return "".join(res)