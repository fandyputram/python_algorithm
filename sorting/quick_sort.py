def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    # Create empty lists to hold elements less than, equal to, and greater than the pivot
    left = []
    middle = []
    right = []

    # Partition the array into three subarrays
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    # Recursively sort the left and right subarrays, and combine them with the middle array
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(my_list)
print("Sorted array:", sorted_list)
