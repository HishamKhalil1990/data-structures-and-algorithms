def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        temp = arr[i]
        if type(temp) is not int:
            raise TypeError("Only integers are allowed")
        while j >= 0 and temp < arr[j]:
           arr[j+1]  = arr[j]
           j  -= 1
           arr[j + 1] = temp
    return arr

if __name__ == "__main__":

    print(insertion_sort([8,4,23,42,16,15]))
    print(insertion_sort([20,18,12,8,5,-2]))
    print(insertion_sort([5,12,7,5,5,7]))
    print(insertion_sort([]))
