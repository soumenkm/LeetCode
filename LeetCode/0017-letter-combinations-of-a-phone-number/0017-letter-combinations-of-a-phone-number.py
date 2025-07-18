class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        charMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def func(index: int, comb: List[str]):
            if index >= n:
                res.append("".join(comb.copy()))
                return
            else:
                digit = digits[index]
                letters = charMap[digit]
                for letter in letters:
                    comb.append(letter)
                    func(index+1, comb)
                    comb.pop()
        
        func(0, [])
        return res
