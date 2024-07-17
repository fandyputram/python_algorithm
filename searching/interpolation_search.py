def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 1
result = interpolation_search(my_list, target_value)
if result != -1:
    print(f"Target value {target_value} found at index {result}")
else:
    print(f"Target value {target_value} not found")


# [1, 3, 5, 7, 9, 11, 13] Uniformly distributed 1-3 = 2, 3-5 = 2, 5-7
# [1, 3, 5, 7, 9, 11, 14] Not uniformly distributed