from ..hashtable.hashtable import HashTable

def left_join(hashtable_left,hashtable_right):
    joind_list = []
    for key in hashtable_left.keys():
        if hashtable_right.contains(key):
            joind_list.append([key,hashtable_left.get(key),hashtable_right.get(key)])
        else:
            joind_list.append([key,hashtable_left.get(key),'Null'])
    return joind_list

if __name__ == "__main__":
    hashtable_one = HashTable()
    hashtable_two = HashTable()
    hashtable_one.add('fond','enamored')
    hashtable_one.add('warth','anger')
    hashtable_one.add('diligent','employed')
    hashtable_one.add('outfit','grab')
    hashtable_one.add('guide','usher')
    hashtable_two.add('fond','averse')
    hashtable_two.add('warth','delight')
    hashtable_two.add('diligent','idle')
    hashtable_two.add('guide','follow')
    hashtable_two.add('flow','jam')
    print(left_join(hashtable_left=hashtable_one,hashtable_right=hashtable_two))
    hashtable_three = HashTable()
    print(left_join(hashtable_left=hashtable_one,hashtable_right=hashtable_three))
    print(left_join(hashtable_left=hashtable_three,hashtable_right=hashtable_one))
    print(left_join(hashtable_left=hashtable_three,hashtable_right=hashtable_three))

