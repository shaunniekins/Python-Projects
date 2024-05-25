## Brute Force

This algorithm is a recursive solution to the problem of finding the shortest combination of numbers that add up to a target sum. It uses a brute force approach, trying all possible combinations of the numbers.

Here's a step-by-step visualization of the algorithm in a tree-like structure:

Start with the target sum at the root of the tree.
For each number in the list, subtract it from the target sum and create a new branch for the remainder.
Repeat this process for each remainder until you either hit a remainder that is in the list of numbers (in which case you've found a valid combination) or a remainder that is less than the smallest number in the list (in which case there's no valid combination down that branch).
Whenever you find a valid combination, compare its length to the shortest combination found so far. If it's shorter, it becomes the new shortest combination.
Continue this process until all branches have been explored. The shortest combination found is the result.
Here's a text representation of the tree for ShortestSum(7, [5, 3, 4, 7]):

7
|-- 7-5 = 2
| |-- 2-5 = -3 (invalid, stop this branch)
| |-- 2-3 = -1 (invalid, stop this branch)
| |-- 2-4 = -2 (invalid, stop this branch)
| |-- 2-7 = -5 (invalid, stop this branch)
|-- 7-3 = 4
| |-- 4-5 = -1 (invalid, stop this branch)
| |-- 4-3 = 1
| | |-- 1-5 = -4 (invalid, stop this branch)
| | |-- 1-3 = -2 (invalid, stop this branch)
| | |-- 1-4 = -3 (invalid, stop this branch)
| | |-- 1-7 = -6 (invalid, stop this branch)
| |-- 4-4 = 0 (valid combination: [4, 3])
| |-- 4-7 = -3 (invalid, stop this branch)
|-- 7-4 = 3
| |-- 3-5 = -2 (invalid, stop this branch)
| |-- 3-3 = 0 (valid combination: [3, 4])
| |-- 3-4 = -1 (invalid, stop this branch)
| |-- 3-7 = -4 (invalid, stop this branch)
|-- 7-7 = 0 (valid combination: [7])

The shortest combination is [7], so that's the result of the function.

7
|-- 7 - 5 = 2
| |-- 2 - 5 = -3 (invalid, return None)
| |-- 2 - 2 = 0 (valid, return [2])
| | Result: [5, 2]
|-- 7 - 2 = 5
| |-- 5 - 5 = 0 (valid, return [5])
| | Result: [2, 5]

## Memoization

This algorithm is a memoized version of the previous one. It uses a dictionary memo to store previously computed results, which significantly improves the performance by avoiding redundant computations.

Here's a step-by-step visualization of the algorithm in a tree-like structure:

Start with the target sum at the root of the tree.
Check if the target sum is in the memo. If it is, return the stored result.
For each number in the list, subtract it from the target sum and create a new branch for the remainder.
Repeat this process for each remainder until you either hit a remainder that is in the list of numbers (in which case you've found a valid combination) or a remainder that is less than the smallest number in the list (in which case there's no valid combination down that branch).
Whenever you find a valid combination, compare its length to the shortest combination found so far. If it's shorter, it becomes the new shortest combination.
Before returning the result, store it in the memo with the target sum as the key.
Continue this process until all branches have been explored. The shortest combination found is the result.
Here's a text representation of the tree for ShortestSum(7, [5, 3, 4, 7]):

7
|-- 7-5 = 2 (memoized)
| |-- 2-5 = -3 (invalid, stop this branch)
| |-- 2-3 = -1 (invalid, stop this branch)
| |-- 2-4 = -2 (invalid, stop this branch)
| |-- 2-7 = -5 (invalid, stop this branch)
|-- 7-3 = 4 (memoized)
| |-- 4-5 = -1 (invalid, stop this branch)
| |-- 4-3 = 1 (memoized)
| | |-- 1-5 = -4 (invalid, stop this branch)
| | |-- 1-3 = -2 (invalid, stop this branch)
| | |-- 1-4 = -3 (invalid, stop this branch)
| | |-- 1-7 = -6 (invalid, stop this branch)
| |-- 4-4 = 0 (valid combination: [4, 3])
| |-- 4-7 = -3 (invalid, stop this branch)
|-- 7-4 = 3 (memoized)
| |-- 3-5 = -2 (invalid, stop this branch)
| |-- 3-3 = 0 (valid combination: [3, 4])
| |-- 3-4 = -1 (invalid, stop this branch)
| |-- 3-7 = -4 (invalid, stop this branch)
|-- 7-7 = 0 (valid combination: [7])

The shortest combination is [7], so that's the result of the function. The memoization significantly reduces the number of branches that need to be explored.

## Tabulation

This is a tabulation (bottom-up) dynamic programming solution to the problem of finding the shortest combination of numbers that add up to a target sum. It uses a table to store the shortest combination for each possible sum up to the target sum.

Here's a step-by-step visualization of the algorithm in a tree-like structure:

Initialize a table with targetSum + 1 slots, all set to None, except for the 0th slot which is set to an empty list.
For each possible sum (from 0 to targetSum), if a combination exists (i.e., the table slot is not None), try adding each number in the list to the current sum.
If the new sum is within the target sum, and either no combination for the new sum exists yet, or the new combination is shorter than the existing one, store the new combination in the table.
Continue this process until all possible sums have been explored. The shortest combination for the target sum, if it exists, is stored in the last slot of the table.
Here's a text representation of the table for ShortestSum(7, [5, 3, 4, 7]):

Index: 0 1 2 3 4 5 6 7
Table: [] None None [3] [4] [5] [3,3] [7]

The shortest combination is [7], so that's the result of the function. The tree-like structure in this case is not as clear as in the recursive solutions, because the algorithm fills up a table in a linear fashion rather than branching out.

### Difference of the time complexities of the brute force approach and dynamic programming.

The time complexity of the brute force approach, the memoization approach, and the tabulation approach are different due to the way they handle the problem.

- Brute Force Approach: The time complexity of the brute force approach is O(n^m \* m), where n is the length of the numbers array and m is the target sum. This is because for each number, we are trying to subtract it from the target sum and recursively solving the sub-problems. The multiplication by m is due to the time taken to copy the combination array. This leads to a lot of repeated computations as the same sub-problems are solved multiple times.

- Memoization Approach: The time complexity of the memoization approach is O(m^2 \* n), where m is the target sum and n is the length of the numbers array. This is because we are storing the results of the sub-problems in a memoization table (dictionary in Python). So, we avoid repeated computations by checking if the result of a sub-problem is already available in the memoization table. The m^2 term is due to the time taken to copy the combination array.

- Tabulation Approach: The time complexity of the tabulation approach is also O(m^2 \* n), where m is the target sum and n is the length of the numbers array. This is because we are iteratively solving the sub-problems and storing the results in a table. Unlike the memoization approach, the tabulation approach solves the sub-problems in a bottom-up manner. The m^2 term is due to the time taken to copy the combination array.

In conclusion, dynamic programming (both memoization and tabulation) provides a more efficient solution to the problem by avoiding repeated computations, which are prevalent in the brute force approach. However, the time taken to copy the combination array adds to the time complexity in all three approaches.
