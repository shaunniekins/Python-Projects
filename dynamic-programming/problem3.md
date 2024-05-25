## Brute Force

To visualize the algorithm, we can create a tree where each node represents a recursive call to wordConstruct. The root of the tree is the initial call to wordConstruct with the target word. Each child node is a recursive call to wordConstruct with the remaining suffix after removing a word from the word bank that matches the prefix of the current target.

Here's a step-by-step plan to create the tree:

Create a root node with the initial target word.
For each word in the word bank that matches the prefix of the current target, create a child node with the remaining suffix.
Repeat the process for each child node until the target word is empty.
Here's a pseudocode representation of the tree:

- "purple"
  - "urple" (after removing "p")
    - "rple" (after removing "ur")
      - "ple" (after removing "p")
        - "le" (after removing "p")
          - "" (after removing "le")
  - "rple" (after removing "purp")
    - "le" (after removing "p")
      - "" (after removing "le")
  - "le" (after removing "purpl")
    - "" (after removing "le")

This tree represents all the possible ways to construct the word "purple" from the word bank. Each path from the root to a leaf node represents a valid way to construct the word.

## Memoization

The tree visualization for the memoized version of the wordConstruct function would be similar to the non-memoized version, but with fewer nodes due to the memoization. The memoization allows us to store the results of previous computations and avoid redundant computations.

Here's a step-by-step plan to create the tree:

Create a root node with the initial target word.
For each word in the word bank that matches the prefix of the current target, create a child node with the remaining suffix.
If the remaining suffix has been computed before (exists in the memo), return the stored result and do not create further child nodes.
Repeat the process for each child node until the target word is empty.
Here's a pseudocode representation of the tree:

- "purple"
  - "urple" (after removing "p")
    - "rple" (after removing "ur")
      - "ple" (after removing "p")
        - "le" (after removing "p")
          - "" (after removing "le")
  - "rple" (after removing "purp") [No further child nodes as "rple" is already computed]
  - "le" (after removing "purpl")
    - "" (after removing "le")

This tree represents all the possible ways to construct the word "purple" from the word bank. Each path from the root to a leaf node represents a valid way to construct the word. The memoization reduces the number of nodes in the tree by avoiding redundant computations.

## Tabulation

The tabulation version of the wordConstruct function uses a bottom-up approach, so the tree visualization would be a bit different. Instead of a tree, it's more accurate to visualize it as a table where each cell represents the possible combinations to construct the substring up to that index.

Here's a step-by-step plan to create the table:

Create a table with a length of the target word plus one.
Initialize the first cell (index 0) with an empty list.
For each cell in the table, iterate over the word bank.
If the word in the word bank matches the substring of the target word starting at the current index, create new combinations by appending the word to the combinations in the current cell.
Extend the cell at the index of the current index plus the length of the word with the new combinations.
Repeat the process for each cell in the table.
Here's a pseudocode representation of the table:

Index: 0 1 2 3 4 5 6
Word: p u r p l e
Table:
0 -> [[]]
1 -> [["p"]]
2 -> [["p", "u"]]
3 -> [["p", "u", "r"], ["purp"]]
4 -> [["p", "u", "r", "p"], ["purp", "p"]]
5 -> [["p", "u", "r", "p", "l"], ["purp", "p", "l"]]
6 -> [["p", "u", "r", "p", "l", "e"], ["purp", "p", "l", "e"], ["purp", "le"], ["purpl"]]

This table represents all the possible ways to construct the word "purple" from the word bank. Each cell in the table represents a valid way to construct the substring of the target word up to that index.

### Difference of the time complexities of the brute force approach and dynamic programming.

The time complexity of the brute force approach, the memoization approach, and the tabulation approach are different due to the way they handle the problem.

- Brute Force Approach: The time complexity of the brute force approach is O(n^m \* m), where n is the length of the wordBank array and m is the length of the target string. This is because for each word, we are trying to match it with the prefix of the target string and recursively solving the sub-problems. The multiplication by m is due to the time taken to copy the combination array. This leads to a lot of repeated computations as the same sub-problems are solved multiple times.

- Memoization Approach: The time complexity of the memoization approach is O(n \* m^2), where m is the length of the target string and n is the length of the wordBank array. This is because we are storing the results of the sub-problems in a memoization table (dictionary in Python). So, we avoid repeated computations by checking if the result of a sub-problem is already available in the memoization table. The m^2 term is due to the time taken to copy the combination array.

- Tabulation Approach: The time complexity of the tabulation approach is also O(n \* m^2), where m is the length of the target string and n is the length of the wordBank array. This is because we are iteratively solving the sub-problems and storing the results in a table. Unlike the memoization approach, the tabulation approach solves the sub-problems in a bottom-up manner. The m^2 term is due to the time taken to copy the combination array.

In conclusion, dynamic programming (both memoization and tabulation) provides a more efficient solution to the problem by avoiding repeated computations, which are prevalent in the brute force approach. However, the time taken to copy the combination array adds to the time complexity in all three approaches.
