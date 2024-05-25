## Brute Force

The howSum function uses a recursive approach to solve the problem. It tries to subtract each number in the numbers list from the targetSum until it reaches zero (successful case) or a negative number (unsuccessful case).

Here's a simplified tree visualization of the algorithm for a smaller problem, howSum(7, [5, 3, 4, 7]):

7
|-- 7-5=2
| |-- 2-5=-3 (unsuccessful)
| |-- 2-3=-1 (unsuccessful)
| |-- 2-4=-2 (unsuccessful)
| `-- 2-7=-5 (unsuccessful)
|-- 7-3=4
|   |-- 4-5=-1 (unsuccessful)
|   |-- 4-3=1
|   |   |-- 1-5=-4 (unsuccessful)
|   |   |-- 1-3=-2 (unsuccessful)
|   |   |-- 1-4=-3 (unsuccessful)
|   |   `-- 1-7=-6 (unsuccessful)
| |-- 4-4=0 (successful)
| `-- 4-7=-3 (unsuccessful)
|-- 7-4=3
|   |-- 3-5=-2 (unsuccessful)
|   |-- 3-3=0 (successful)
|   |-- 3-4=-1 (unsuccessful)
|   `-- 3-7=-4 (unsuccessful)
`-- 7-7=0 (successful)

7
|-- 7 - 5 = 2
| |-- 2 - 5 = -3 (invalid, return None)
| |-- 2 - 2 = 0 (valid, return [2])
| | Result: [5, 2]
|-- 7 - 2 = 5
| |-- 5 - 5 = 0 (valid, return [5])
| | Result: [2, 5]

In this tree, each node represents a recursive call to howSum with the remaining sum after subtracting a number from the numbers list. The tree branches represent the different choices of numbers to subtract. The leaf nodes represent the base cases: when the remaining sum is zero (successful case) or negative (unsuccessful case).

## Memoization

The howSum function with memoization works similarly to the previous version, but it stores the results of previous computations in a memo dictionary to avoid redundant work. When a result is already in the memo, it returns that result immediately instead of making more recursive calls.

Here's a simplified tree visualization of the algorithm for howSum(7, [5, 3, 4, 7]) with memoization:

7
|-- 7-5=2 (not in memo)
| |-- 2-5=-3 (unsuccessful, store in memo)
| |-- 2-3=-1 (unsuccessful, store in memo)
| |-- 2-4=-2 (unsuccessful, store in memo)
| `-- 2-7=-5 (unsuccessful, store in memo)
|-- 7-3=4 (not in memo)
|   |-- 4-5=-1 (unsuccessful, retrieve from memo)
|   |-- 4-3=1 (not in memo)
|   |   |-- 1-5=-4 (unsuccessful, retrieve from memo)
|   |   |-- 1-3=-2 (unsuccessful, retrieve from memo)
|   |   |-- 1-4=-3 (unsuccessful, retrieve from memo)
|   |   `-- 1-7=-6 (unsuccessful, retrieve from memo)
| |-- 4-4=0 (successful, store in memo)
| `-- 4-7=-3 (unsuccessful, retrieve from memo)
|-- 7-4=3 (retrieve from memo)
`-- 7-7=0 (successful, store in memo)

In this tree, each node represents a recursive call to howSum with the remaining sum after subtracting a number from the numbers list. The tree branches represent the different choices of numbers to subtract. The leaf nodes represent the base cases: when the remaining sum is zero (successful case) or negative (unsuccessful case). Nodes that are retrieved from the memo are marked as such.

## Tabulation

The howSum function with tabulation works differently from the recursive versions. Instead of a tree, it builds a table from 0 to targetSum. Each index i in the table represents a subproblem of how to sum up to i using the numbers in the list.

Here's a simplified visualization of the algorithm for howSum(7, [5, 3, 4]) with tabulation:

Index: 0 1 2 3 4 5 6 7
Table: [] \_ \_ \_ \_ \_ \_ \_

Iteration 1 (i=0):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ \_ \_ _ [5] _ \_

Iteration 2 (i=1):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ \_ \_ _ [5] _ \_

Iteration 3 (i=2):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ \_ \_ _ [5] _ \_

Iteration 4 (i=3):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ _ [3] _ [5] \_ \_

Iteration 5 (i=4):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ _ [3] [4] [5] _ \_

Iteration 6 (i=5):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ _ [3] [4] [5,5] _ \_

Iteration 7 (i=6):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ _ [3] [4] [5,5] [3,3] _

Iteration 8 (i=7):
Index: 0 1 2 3 4 5 6 7
Table: [] \_ \_ [3] [4] [5,5] [3,3] [4,3]

In this table, each index i represents a subproblem of how to sum up to i using the numbers in the list. The value at each index is the first combination of numbers that sums up to i (or \_ if no combination is found). The algorithm iterates over each index and each number, and if it can reach a new index by adding the current number to the current index, it updates the new index with the current combination plus the current number.

### Difference of the time complexities of the brute force approach and dynamic programming.

The time complexity of the brute force approach, the memoization approach, and the tabulation approach are different due to the way they handle the problem.

- Brute Force Approach: The time complexity of the brute force approach is O(n^m), where n is the length of the numbers array and m is the target sum. This is because for each number, we are trying to subtract it from the target sum and recursively solving the sub-problems. This leads to a lot of repeated computations as the same sub-problems are solved multiple times.

- Memoization Approach: The time complexity of the memoization approach is O(m\*n), where m is the target sum and n is the length of the numbers array. This is because we are storing the results of the sub-problems in a memoization table (dictionary in Python). So, we avoid repeated computations by checking if the result of a sub-problem is already available in the memoization table.

- Tabulation Approach: The time complexity of the tabulation approach is also O(m\*n), where m is the target sum and n is the length of the numbers array. This is because we are iteratively solving the sub-problems and storing the results in a table. Unlike the memoization approach, the tabulation approach solves the sub-problems in a bottom-up manner.

In conclusion, dynamic programming (both memoization and tabulation) provides a more efficient solution to the problem by avoiding repeated computations, which are prevalent in the brute force approach.
