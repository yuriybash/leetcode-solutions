def qs(arr, begin=0, end=None):

    end = end or len(arr)-1
    if begin >= end:
        return

    pivot = partition(arr, begin, end)
    qs(arr, begin, pivot-1)
    qs(arr, pivot+1, end)

def partition(arr, begin, end):
    
    pivot = begin
    border = pivot
    pivot_val = arr[pivot]

    for idx in range(begin, end+1):

        if arr[idx] < pivot_val:
            border+=1
            arr[idx], arr[border] = arr[border], arr[idx]

    arr[pivot], arr[border] = arr[border], arr[pivot]
    return border


x = [97, 200, 100, 101, 211, 107]
qs(x)
print x