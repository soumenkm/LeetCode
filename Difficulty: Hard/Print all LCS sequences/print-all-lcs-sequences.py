from typing import List, Tuple, Set

class Solution:
    def allLCS(self, s1_str: str, s2_str: str) -> List[str]:
        n = len(s1_str)
        m = len(s2_str)
        
        # --- Phase 1: Build DP table and Adjacency List (your code) ---
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1_str[i - 1] == s2_str[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # --- Phase 2: Memoized Recursive Search (Replaces your DFS) ---
        memo: Dict[Tuple[int, int], Set[str]] = {}

        def find_all(i: int, j: int) -> Set[str]:
            # If we've solved this subproblem, return the stored result
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: Reached the start, the only LCS is the empty string
            if i == 0 or j == 0:
                return {""}

            # Recursive Step
            result_set = set()
            
            # If characters match, this char is part of the LCS
            if s1_str[i - 1] == s2_str[j - 1]:
                # We must have come from the diagonal
                prev_lcs_set = find_all(i - 1, j - 1)
                for s in prev_lcs_set:
                    result_set.add(s + s1_str[i - 1])
            
            # If characters do not match, explore parent(s) that gave the max value
            else:
                # If we could have come from the top
                if dp[i - 1][j] >= dp[i][j - 1]:
                    result_set.update(find_all(i - 1, j))
                
                # If we could have come from the left
                if dp[i][j - 1] >= dp[i - 1][j]:
                    result_set.update(find_all(i, j - 1))

            # Store the result for this state and return it
            memo[(i, j)] = result_set
            return result_set

        # Initial call and sorting
        all_lcs_set = find_all(n, m)
        return sorted(list(all_lcs_set))