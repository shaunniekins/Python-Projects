def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    max_index = dp.index(max_length)

    lis = [nums[max_index]]
    current_length = max_length - 1

    for i in range(max_index - 1, -1, -1):
        if dp[i] == current_length:
            lis.insert(0, nums[i])
            current_length -= 1

    return max_length, lis


nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length, subsequence = longest_increasing_subsequence(nums)
print(length, ":", subsequence)
