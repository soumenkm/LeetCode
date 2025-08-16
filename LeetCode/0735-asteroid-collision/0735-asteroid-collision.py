class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if abs(ast) < stack[-1]:
                    ast = 0
                    break
                
                if abs(ast) == stack[-1]:
                    stack.pop()
                    ast = 0
                    break
                
                if abs(ast) > stack[-1]:
                    stack.pop()
            
            if ast != 0:
                stack.append(ast)
        
        return stack