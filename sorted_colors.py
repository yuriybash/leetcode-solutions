def largestRectangleArea(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans


def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)


x = [2, 3, 1, 4, 8, 7, 5, 6]
quicksort(x)
print x



