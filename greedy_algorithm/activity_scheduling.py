# Time Complexity: O(nlogn)

def max_activities(activities):
    activities.sort(key = lambda x: x[1])

    i = 0
    count = 1

    for j in range(1, len(activities)):
        if activities[j][0] >= activities[i][1]:
            i = j
            count += 1

    return count

activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
print(max_activities(activities))