def mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = int(n/2)
        left = arr[0:mid]
        right = arr[mid:n]
        mergesort(left)
        mergesort(right)
        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

if __name__ == "__main__":
    arr = [8,4,23,42,16,15,3,19,7,30,0]
    print(mergesort(arr))
    # print(mergesort([10,5,2,7,0,'three']))
