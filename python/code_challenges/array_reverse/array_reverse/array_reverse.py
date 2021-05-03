message = print('enter a list')
list_value = input()
def reverseArray(arg):
    reversed_list = []
    for item in arg:
        if not (item == '[' or item == " " or item == "," or item == "]"):
            reversed_list.insert(0, item)
    return reversed_list
new_list = reverseArray(list_value)
print(new_list)
