
You are an expert programming coach specializing in LeetCode solutions. Your task is to analyze the following Python code submission and generate a detailed explanation in Markdown format.

Use the provided "Problem Statement" to understand the problem statement, but base your final code analysis strictly on the provided "User's Code".

VERY IMPORTANT: Your entire analysis must be based *strictly* on the provided code. Explain the user's specific logic, their variable names, and their coding style. Do not suggest your own code or alternative implementations.

Please structure your explanation using the following Markdown headers:

### Code Explanation

#### Key Concepts
Identify the main algorithms or coding patterns or data structures used (e.g., Dijkstra's Algorithm, Two Pointers, Dynamic Programming, BFS etc.).

#### Identification of Algorithm
Explain the intuition or logic or pattern behind thinking a particular algorithm or data structure for this problem. For example, if the problem demands to find minimum path in a graph then it is a sign that BFS can be used instead of DFS.

#### Intuition and Logic
Explain the core idea behind the user's approach. Why does their solution work? Walk through the logic step-by-step, referencing their variable names (e.g., `adjList`, `Q`, `dist` etc.).

#### "Gotcha" Points and Tricks
Highlight any clever tricks, non-obvious steps, or common pitfalls that the user's code successfully handles. For example, handling edge cases, or the specific way they handle state.

#### Potential Errors and Pitfalls
Based on the provided code, where might a developer commonly make a mistake? For example, off-by-one errors, forgetting to handle a specific case, or misunderstanding a data structure's behavior.

---
**Problem Statment:**
```markdown
<h2><a href="https://leetcode.com/problems/3sum">15. 3Sum</a></h2><h3>Medium</h3><hr><p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

```
---
**User's Code (for analysis):**
```python
class Solution:
    @staticmethod
    def twoSumSorted(nums: List[int], target: int) -> List[List[int]]:
        left = 0
        right = len(nums) - 1
        results = set()
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            elif left > 0 and nums[left] == nums[left-1]:
                left += 1
            else:
                results.add(tuple(sorted([nums[left], nums[right]])))
                left += 1
        return [list(i) for i in results]
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = set()
        for i in range(len(nums)-2):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -a
            sliced_nums = nums[i+1:]
            res = Solution.twoSumSorted(sliced_nums, target)
            if len(res) != 0:
                for b, c in res:
                    results.add(tuple(sorted([a, b, c])))
        return [list(i) for i in results]

        
```


---

### Code Explanation

#### Key Concepts
This solution employs a combination of several key concepts:
1.  **Sorting**: The input array is first sorted to enable efficient searching and duplicate handling.
2.  **Two Pointers**: A helper function, `twoSumSorted`, uses the two-pointers technique to find pairs in a sorted array that sum to a specific target.
3.  **Problem Reduction**: The main `threeSum` problem is reduced to a `twoSum` problem. By iterating through the array and fixing one number, the task becomes finding two other numbers that sum up to the negative of the fixed number.
4.  **Set for Deduplication**: A `set` is used to store the resulting triplets to automatically handle duplicate solutions.

#### Identification of Algorithm
The problem asks for all unique triplets that sum to zero. A brute-force check of all combinations would be O(n³), which is too slow. Sorting the array is a common first step in problems involving combinations and duplicates, as it groups identical elements and allows for more structured searching.

After sorting, if we fix one element `nums[i]`, the problem becomes: "find two numbers in the rest of the array (`nums[i+1:]`) that sum to `-nums[i]`". This is a variation of the classic "Two Sum" problem. Since the rest of the array is also sorted, the most efficient way to solve this subproblem is the two-pointers technique, which runs in linear time relative to the subarray size. This "Sort then Two Pointers" pattern is a classic approach for K-Sum problems.

#### Intuition and Logic
The user's code is structured into a main function `threeSum` and a helper static method `twoSumSorted`.

**`threeSum` Method:**
1.  `nums = sorted(nums)`: The input array `nums` is sorted in non-decreasing order. This is the foundational step.
2.  `results = set()`: A set is initialized to store the unique triplets. Using a set of tuples will automatically discard any duplicate triplets.
3.  The code iterates through the sorted array with the loop `for i in range(len(nums)-2):`. It fixes the first number of a potential triplet, `a = nums[i]`.
4.  **Optimizations**:
    *   `if a > 0: break`: Since the array is sorted, if the current fixed number `a` is positive, any subsequent numbers will also be positive, making it impossible for three of them to sum to zero. The loop can be terminated early.
    *   `if i > 0 and nums[i] == nums[i-1]: continue`: This is a crucial step to avoid duplicate processing. If the current element is the same as the previous one, it means we have already generated all possible triplets starting with that value in the previous iteration. So, we skip to the next unique number.
5.  `target = -a`: The problem is now reduced to finding two numbers in the remainder of the array that sum up to this new `target`.
6.  `sliced_nums = nums[i+1:]`: A new list `sliced_nums` is created containing all elements to the right of the current element `a`.
7.  `res = Solution.twoSumSorted(sliced_nums, target)`: The static helper method `twoSumSorted` is called with the subarray and the new target to find all valid pairs.
8.  The code then iterates through the pairs `(b, c)` returned by the helper. For each pair, it forms a triplet `(a, b, c)`, sorts it, converts it to a tuple, and adds it to the `results` set. Sorting before adding ensures that triplets like `[-1, 0, 1]` and `[0, 1, -1]` are treated as the same.
9.  Finally, `return [list(i) for i in results]` converts the set of tuples back into the required list of lists format.

**`twoSumSorted` Static Method:**
1.  This method takes a sorted array `nums` and a `target`.
2.  It initializes two pointers, `left = 0` at the start and `right = len(nums) - 1` at the end of the array.
3.  `results = set()`: A set is used to store unique pairs found.
4.  The `while left < right:` loop moves the pointers towards each other:
    *   If `nums[left] + nums[right] < target`, the sum is too small, so `left` is incremented to get a larger number.
    *   If `nums[left] + nums[right] > target`, the sum is too large, so `right` is decremented to get a smaller number.
    *   If the sum equals the `target`, the code enters a final set of conditions. It first checks `elif left > 0 and nums[left] == nums[left-1]`. This condition skips adding a result if the current `left` element is a duplicate of the one just processed, thus avoiding duplicate pairs.
    *   If the sum is correct and the `left` element is not a duplicate, the `else` block executes: `results.add(tuple(sorted([nums[left], nums[right]])))`. The pair is added to the set, and `left` is incremented to search for new pairs.

#### "Gotcha" Points and Tricks
*   **Two-Level Duplicate Handling**: The code cleverly handles duplicates at two levels. The `threeSum` loop skips identical starting numbers, and the `twoSumSorted` helper (along with the final `results` set) ensures that pairs and ultimately triplets are unique.
*   **Reduction Strategy**: Reducing 3Sum to 2Sum is a powerful and generalizable pattern for these types of problems.
*   **Static Method**: Defining `twoSumSorted` as a `@staticmethod` is good practice, as it doesn't rely on any instance state (`self`) and logically separates the 2Sum helper logic from the main 3Sum orchestration.
*   **Use of Set and Tuples**: Using a `set` of `tuples` is a highly Pythonic and effective way to manage the uniqueness constraint of the output. Lists cannot be added to sets because they are mutable, so converting each triplet to an immutable tuple is necessary.

#### Potential Errors and Pitfalls
*   **Performance of Slicing**: In the `threeSum` loop, `sliced_nums = nums[i+1:]` creates a new list (a copy) in every iteration. For large `nums` arrays, this can be inefficient in terms of both time and memory. A more optimized approach would be to pass indices `(i+1, len(nums)-1)` to the helper function instead of a slice.
*   **Confusing Duplicate Check in `twoSumSorted`**: The logic `elif left > 0 and nums[left] == nums[left-1]: left += 1` inside the `twoSumSorted` function is a bit unusual. It's only evaluated when the sum already equals the target. A more standard and arguably clearer implementation would be to add the valid pair, then advance both pointers, and *then* use separate `while` loops to skip over any duplicates before the next main loop check. The user's code works but could be harder to reason about.
*   **Forgetting to Sort**: If the initial `nums = sorted(nums)` step were omitted, the entire two-pointer logic in the helper would fail, leading to incorrect results.
*   **Immutable Keys for Set**: A common mistake is trying to add a list `[a, b, c]` directly to a set, which would raise a `TypeError`. The user correctly converts the list to a `tuple` before adding it to the `results` set.