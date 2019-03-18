def qs(arr, low=0, high=None):

    if high is None:
        high = len(arr)-1
    if low >= high:
        return

    pivot = partition(arr, low, high)
    qs(arr, low, pivot-1)
    qs(arr, pivot+1, high)


def partition(arr, low, high):
    
    pivot_idx = low
    border = low
    pivot_value = arr[pivot_idx]

    for idx in range(low, high+1):

        if arr[idx] < pivot_value:
            border += 1
            arr[idx], arr[border] = arr[border], arr[idx]

    arr[pivot_idx], arr[border] = arr[border], arr[pivot_idx]

    return border




x = [97, 200, 100, 101, 211, 107]
qs(x)
print x