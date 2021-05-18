from typing import Counter


def zip_Lists(list1, list2):
    counter_list1 = 0
    counter_list2 = 0
    value1 = []
    value2 = []
    not_finish = True
    while not_finish:
        value = list1.kth_from_end(counter_list1)
        if value != None:
            counter_list1 += 1
            value1.append(value)
        else:
            not_finish = False
    not_finish = True
    while not_finish:
        value = list2.kth_from_end(counter_list2)
        if value != None:
            counter_list2 += 1
            value2.append(value)
        else:
            not_finish = False
    rev_value1 = value1[::-1]
    rev_value2 = value2[::-1]
    not_finish = True
    counter = 0
    if counter_list1 >= counter_list2:
        while(not_finish):
            list1.insert_after(rev_value1[counter],rev_value2[counter])
            if counter == counter_list2 - 1:
                break
            counter += 1
    elif counter_list1 < counter_list2:
        while(not_finish):
            list1.insert_after(rev_value1[counter],rev_value2[counter])
            if counter == counter_list1 - 1:
                break
            counter += 1
        counter += 1
        for index in range(counter,counter_list2):
            print(rev_value2[index])
            list1.append(rev_value2[index])
    return str(list1)
