from .linked_list import Linked_List

class HashTable():
    def __init__(self,size=1024):
        self.size = size
        self._buckets = [None]*size

    def _hash(self,key):
        sum = 0
        for char in key:
            sum += ord(char)
        hash_key = (sum*23)%(self.size)
        return hash_key

    def add(self,key,value):
        index = self._hash(key)
        if not self._buckets[index]:
            self._buckets[index] = Linked_List()
        return self._buckets[index].append([key,value])

    def get(self,key):
        index = self._hash(key)
        if not self._buckets[index]:
            return None
        else:
            current = self._buckets[index].head
            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next
            return None

    def contains(self,key):
        index = self._hash(key)
        bucket = self._buckets[index]
        if not bucket:
            return False
        else:
            if bucket.includes(key):
                return True
            return False

if __name__ == "__main__":
    hashtable = HashTable()
    print(hashtable.add("ahmad", 30))
    print(hashtable.add("silent", True))
    print(hashtable.add("listen", 'to him'))
    print(hashtable.get("ahmad"))
    print(hashtable.get("silent"))
    print(hashtable.get("listen"))
    print(hashtable.contains("ahmad"))
    print(hashtable.contains("silent"))
    print(hashtable.contains("listen"))
    print(hashtable.contains("hisham"))
    print(hashtable._hash('house'))
    # print(hashtable.get("hisham"))


