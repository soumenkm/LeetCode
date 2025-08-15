class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brMap = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in brMap.keys():
                stack.append(char)
            if char in brMap.values():
                if len(stack) != 0:
                    elem = stack.pop()
                else:
                    return False
                if char != brMap[elem]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True