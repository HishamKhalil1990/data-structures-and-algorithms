import math

def find_index(num_list,value,acc = 0):
    middle = (len(num_list)-1)//2
    if len(num_list) == 1 and num_list[middle] != value or num_list == []:
        return -(acc+1)
    elif num_list[middle] == value:
        return middle
    elif num_list[middle] < value:
        right = num_list[middle+1:]
        acc += (middle + 1)
        return middle + (find_index(right,value,acc) + 1)
    elif num_list[middle] > value:
        left = num_list[:middle]
        return find_index(left,value,acc)

