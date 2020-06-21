def merge(arr, lb, mid, ub):
	"""
	Merging of two sorted arrays into one sorted array.

	"""
	k = 0; i = lb; j = mid+1
	temp = []

	while i<=mid and j<=ub:
		if arr[i] <= arr[j]:
			temp.append(arr[i])
			i += 1
			k += 1
		else:
			temp.append(arr[j])
			j += 1
			k += 1

	if i<=mid:
		while i<=mid:
			temp.append(arr[i])
			i += 1
			k += 1
	else:
		while j<=ub:
			temp.append(arr[j])
			j += 1
			k += 1

	for i in range(lb, ub+1):
		arr[i] = temp[i-lb]

	return arr

def mergeSort(arr, lb, ub):
	"""
	Sorting array using MergeSort algorithm.
	
	"""
	if lb==ub:
		return
	else:
		mid = (lb+ub)//2
		mergeSort(arr, lb, mid)
		mergeSort(arr, mid+1, ub)
		arr = merge(arr, lb, mid, ub)
		return arr

if __name__ == '__main__':

	print('Enter the elements:')
	arr = list(map(int, input().strip().split()))

	sortedArray = mergeSort(arr, 0, len(arr) - 1)

	print('The sorted array is:')
	print(' '.join(map(str, sortedArray)))
	