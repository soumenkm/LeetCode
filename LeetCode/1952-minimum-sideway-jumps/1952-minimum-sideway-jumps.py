from functools import lru_cache
from typing import List
import sys

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        sys.setrecursionlimit(1_000_000)  # safety for large n
        n = len(obstacles) - 1
        lanes = (1, 2, 3)

        @lru_cache(None)
        def dp(i: int, lane: int) -> int:
            # move forward greedily while next cell in this lane is free
            j = i
            while j < n and obstacles[j + 1] != lane:
                j += 1
            if j == n:
                return 0  # reached end

            # at point j, lane is blocked at j+1 -> side jump now
            best = float("inf")
            for nl in lanes:
                if nl != lane and obstacles[j] != nl:  # cannot land on obstacle at j
                    best = min(best, 1 + dp(j, nl))
            return best

        return dp(0, 2)
