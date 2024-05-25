def longest_increasing_subsequence(nums):
    n = len(nums)
    memo = {}

    def helper(i):
        if i in memo:
            return memo[i]

        max_length = 1
        max_subsequence = [nums[i]]
        
        # print('max_subsequence: ', max_subsequence)

        for j in range(i):
            # print('j: ', nums[i] > nums[j])
            if nums[i] > nums[j]:
                length, subsequence = helper(j)
                if length + 1 > max_length:
                    max_length = length + 1
                    max_subsequence = subsequence + [nums[i]]

        memo[i] = (max_length, max_subsequence)
        return memo[i]

    max_length = 0
    max_subsequence = []

    for i in range(n):
        # print(i)
        length, subsequence = helper(i)
        # print('length: ', length)
        # print('subsequence: ', subsequence)
        if length > max_length:
            max_length = length
            max_subsequence = subsequence

    return max_length, max_subsequence


nums = [10, 22, 9, 33, 21, 50, 41, 60, 80, 99, 189, 200]
length, subsequence = longest_increasing_subsequence(nums)
print(length, ":", subsequence)