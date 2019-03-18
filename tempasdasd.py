import ipdb

def quicksort(arr, begin=0, end=None):

	if end is None:
		end = len(arr)-1
	if begin >= end:
		return
	pivot = partition(arr, begin, end)
	quicksort(arr, begin, pivot-1)
	quicksort(arr, pivot+1, end)


def partition(arr, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot += 1
            if arr[i] == arr[pivot]:
            	print 'equal'
            else:
            	print 'not equal'
            	print arr
            	print "begin: ", begin, " i: ", i, " pivot: ", pivot
            arr[i], arr[pivot] = arr[pivot], arr[i]
    print "outer swap"
    print "begin: ", begin, " i: ", i, " pivot: ", pivot
    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    return pivot



x = [97, 200, 100, 101, 211, 107]
#ipdb.set_trace()
quicksort(x)
print x