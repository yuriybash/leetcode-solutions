def quicksort(arr, begin=0, end=None):

    if end is None:
        end = len(arr)-1
    if begin >= end:
        return
    pivot = partition(arr, begin, end)
    quicksort(arr, begin, pivot-1)
    quicksort(arr, pivot+1, end)


def partition(arr, low, high):

    pivot_index = low
    border = low

    pivot_value = arr[pivot_index]

    for i in range(low, high+1):
        if arr[i] < pivot_value:
            border+=1
            arr[i], arr[border] = arr[border], arr[i]

    arr[low], arr[border] = arr[border], arr[low]

    return border








    # pivot = begin
    # for i in xrange(begin+1, end+1):
    #     if arr[i] <= arr[begin]:
    #         pivot += 1
    #         arr[i], arr[pivot] = arr[pivot], arr[i]
    # arr[pivot], arr[begin] = arr[begin], arr[pivot]
    # return pivot



x = [97, 200, 100, 101, 211, 107]
quicksort(x)
print x