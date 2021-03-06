def quickSort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quickSort(arr, left, position - 1)
        quickSort(arr, position + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)
    swap(arr, right, low + 1)
    return low + 1

def swap(arr, i, low):
    temp = 0
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

if __name__ == "__main__":
    arr = [8,4,23,42,16,15,9,3,35,55,27,1]
    quickSort(arr,0,len(arr)-1)
    print(arr)
