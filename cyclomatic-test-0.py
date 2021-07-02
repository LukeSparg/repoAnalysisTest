
# Iterative Binary Search Function
# It returns index of x in given array arr present,
# returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # we reach here, then the element was not present
    return -1
