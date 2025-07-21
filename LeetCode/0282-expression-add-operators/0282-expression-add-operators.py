from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def backtrack(index: int, path: str, current_eval: int, last_operand: int):
            # Base Case: We have processed the entire number string.
            if index == n:
                if current_eval == target:
                    res.append(path)
                return

            # Recursive Step: Try all possible numbers starting from `index`.
            for i in range(index, n):
                # This loop handles multi-digit numbers.
                current_operand_str = num[index : i+1]
                
                # Pruning for leading zeros: "05" is invalid, but "0" is fine.
                if len(current_operand_str) > 1 and current_operand_str[0] == '0':
                    break

                current_operand_int = int(current_operand_str)

                # --- First Number Case ---
                # If it's the first number, we just add it to the path.
                if index == 0:
                    backtrack(i + 1, current_operand_str, current_operand_int, current_operand_int)
                
                # --- Subsequent Numbers Case ---
                else:
                    # Try the '+' operator
                    backtrack(i + 1, path + "+" + current_operand_str, current_eval + current_operand_int, current_operand_int)

                    # Try the '-' operator
                    backtrack(i + 1, path + "-" + current_operand_str, current_eval - current_operand_int, -current_operand_int)
                    
                    # Try the '*' operator (The Trick!)
                    # Eval: (current_eval - last_operand) + (last_operand * current_operand_int)
                    # New last_operand: last_operand * current_operand_int
                    new_eval = (current_eval - last_operand) + (last_operand * current_operand_int)
                    backtrack(i + 1, path + "*" + current_operand_str, new_eval, last_operand * current_operand_int)
        
        backtrack(0, "", 0, 0)
        return res