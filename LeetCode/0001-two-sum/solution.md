
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
<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?
```
---
**User's Code (for analysis):**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hash_map:
                return [i, hash_map[comp]]
            else:
                hash_map[num] = i
        return []

        
```


---

### Code Explanation

#### Key Concepts
The solution utilizes a **Hash Map** (implemented as a Python dictionary) to achieve a time-efficient lookup. The overall algorithmic pattern is a **single-pass iteration** through the input array.

#### Identification of Algorithm
The problem requires finding two indices in an array that correspond to values summing to a target. A brute-force approach would involve nested loops, comparing every pair of numbers, resulting in O(n²) time complexity. To optimize this, a faster way to check for the existence of the second number (`target - current_number`) is needed. A hash map provides an average time complexity of O(1) for insertions and lookups. This makes it the ideal data structure to store previously seen numbers and their indices, allowing the algorithm to check for the required complement in constant time during a single pass, thus achieving an overall O(n) time complexity.

#### Intuition and Logic
The core idea is to iterate through the `nums` array once, and for each number, determine its "complement" – the other number that would sum up to the `target`. While iterating, the code maintains a `hash_map` that stores the numbers it has already seen as keys and their corresponding indices as values.

The logic proceeds as follows:
1.  An empty dictionary `hash_map` is initialized to store `number: index` pairs.
2.  The code iterates through the `nums` list using `enumerate`, which provides both the index `i` and the value `num` for each element.
3.  For each `num`, it calculates the complement `comp` needed to reach the `target` (`comp = target - num`).
4.  It then checks if this `comp` already exists as a key in the `hash_map`.
    *   If `comp` is in `hash_map`, it means the complement was encountered at a previous index. The solution has been found. The function immediately returns a list containing the current index `i` and the stored index of the complement, `hash_map[comp]`.
    *   If `comp` is not in `hash_map`, it means the other half of the pair has not been seen yet. The code then adds the *current* number `num` and its index `i` to the `hash_map`. This prepares the map for future iterations, in case a subsequent number needs the current `num` as its complement.
5.  The final `return []` is technically unreachable given the problem constraint that exactly one solution exists, but it serves as a fallback.

#### "Gotcha" Points and Tricks
*   **Single-Pass Optimization:** The code cleverly performs the check and the map-update in a single loop. It doesn't need to pre-populate the hash map in a separate first pass, making the solution more memory and time-efficient.
*   **Check Before Add:** The most critical trick is the order of operations inside the loop. The code first checks if the complement `comp` is in the `hash_map` *before* adding the current `num` to it. This correctly handles cases where a number is its own complement (e.g., `nums = [3,2,4], target = 6`). If the code added `num` first, it would find itself when checking for its complement, violating the rule of not using the same element twice.
*   **Pythonic Iteration:** Using `enumerate` is a clean and efficient way to get both the index and value from the list, avoiding more verbose or less efficient methods like `range(len(nums))` or `nums.index()`.

#### Potential Errors and Pitfalls
*   **Incorrect Order of Operations:** A common pitfall is to place `hash_map[num] = i` before the `if comp in hash_map:` check. This would cause the algorithm to fail on inputs like `[3, 2, 4]` with `target = 6`. When processing the `3` at index 0, it would add `{3: 0}` to the map and then incorrectly find itself as its own complement, returning `[0, 0]`. The user's code correctly avoids this.
*   **Mishandling Duplicates:** If an implementation were to populate the hash map first and then loop again, it could overwrite indices for duplicate numbers, potentially losing the correct answer. For example, in `[3, 3]` with `target = 6`, a pre-population pass would result in `hash_map = {3: 1}`, losing the index of the first `3`. The user's single-pass approach naturally handles this correctly.
*   **Returning the Wrong Values:** A developer might mistakenly store the index as the key and the value as the value in the hash map (e.g., `hash_map[i] = num`), which would defeat the purpose of O(1) lookups for the complement value. The user's code correctly maps `value -> index`.