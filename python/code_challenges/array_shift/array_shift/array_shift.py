def insertShiftArray(num_list:list,value):
    list_length = 0
    middle = 0
    counter = 0

    for num in num_list:
        list_length += 1

    shifted_list = [None] * (list_length + 1)

    if not list_length % 2: #even number
        middle = list_length//2
    else: #odd number
        middle = list_length // 2 + 1

    while counter <= list_length:
        if counter == middle:
            shifted_list[counter] = value
        elif counter < middle:
            shifted_list[counter] = num_list[counter]
        elif counter > middle:
            shifted_list[counter] = num_list[counter-1]
        counter += 1

    return shifted_list
