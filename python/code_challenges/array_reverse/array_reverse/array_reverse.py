list_value = [89, 2354, 3546, 23, 10, -923, 823, -12]
def reverseArray(arg):
    first_list = arg + [1]
    loop_counter = 0
    counter = 0
    index = 0
    for item in arg:
        loop_counter += 1
    counter = loop_counter
    while index < loop_counter:
        first_list[index] = arg[counter - 1]
        index += 1
        counter -= 1
    index = 0
    while index < loop_counter:
        arg[index] = first_list[index]
        index += 1
        counter -= 1
    return arg
new_list = reverseArray(list_value)
print(new_list)
