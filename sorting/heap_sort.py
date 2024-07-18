def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)
        
def heap_sort(arr):
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
heap_sort(my_list)
print("Sorted array:", my_list)
