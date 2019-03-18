def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) / 2;

        # Check if x is present at mid 
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half 
        else:
            r = mid - 1

    # If we reach here, then the element was not present 
    return -1

arr = [1, 2, 5, 8, 12, 20, 25]
print binarySearch(arr, 0, len(arr)-1, -1)