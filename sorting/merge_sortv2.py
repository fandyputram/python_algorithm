def merge_sort(arr: list[int]):
    if len(arr) < 2:
        return arr
    mid_number = len(arr) // 2
    left_arr = arr[:mid_number]
    right_arr = arr[mid_number:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left_arr: list[int], right_arr: list[int]):
    result = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] < right_arr[0]:
            result.append(left_arr.pop(0))
        else:
            result.append(right_arr.pop(0))
    return result + left_arr + right_arr

def test_merge_sort():
    # Test case untuk list dengan elemen acak
    arr1 = [3, 7, 2, 9, 1, 6, 4, 8, 5]
    expected_output1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort(arr1) == expected_output1, "Test case 1 failed"

    # Test case untuk list yang sudah terurut secara terbalik
    arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_output2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort(arr2) == expected_output2, "Test case 2 failed"

    # Test case untuk list yang sudah terurut
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort(arr3) == expected_output3, "Test case 3 failed"

    # Test case untuk list kosong
    arr4 = []
    expected_output4 = []
    assert merge_sort(arr4) == expected_output4, "Test case 4 failed"

    # Test case untuk list dengan satu elemen
    arr5 = [42]
    expected_output5 = [42]
    assert merge_sort(arr5) == expected_output5, "Test case 5 failed"

    print("Semua test cases berhasil dijalankan!")

# Jalankan test case
test_merge_sort()
