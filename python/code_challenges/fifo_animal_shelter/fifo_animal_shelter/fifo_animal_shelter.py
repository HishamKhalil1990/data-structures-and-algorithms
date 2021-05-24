class Animal:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if not self.front:
            return False
        return True

    def enqueue(self,value):
        if not self.is_empty():
            self.front = Animal(value)
            self.rear = self.front
        else:
            new_node = Animal(value)
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            raise EmptyQueueException
        else:
            value = self.front.value
            self.front = self.front.next
            return value

    def peek(self):
        if not self.is_empty():
            raise EmptyQueueException
        else:
            return self.front.value

    def __str__(self):
        if not self.is_empty():
            return ""
        else:
            string = ""
            current = self.front
            while current != None:
                string += str(current.value) + ' -> '
                current = current.next
            return string

class Cat_queue(Queue):
    def __init__(self):
        super().__init__()

class Dog_queue(Queue):
    def __init__(self):
        super().__init__()

class Animal_Shelter:
    def __init__(self):
        self.cat_q = Cat_queue()
        self.dog_q = Dog_queue()

    def enqueue(self,animal):
        if animal == "cat":
            self.cat_q.enqueue("cat")
        elif animal == "dog":
            self.dog_q.enqueue("dog")

    def dequeue(self,pref):
        value = None
        if pref == "cat":
            value = self.cat_q.dequeue()
        elif pref == "dog":
            value = self.dog_q.dequeue()
        return value

    def __str__(self):
        return str(f"{self.cat_q}{self.dog_q}")

# class Animal_Shelter:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def enqueue(self,animal):
#         if animal == "cat":
#             new_animal = Cat()
#         elif animal == "dog":
#             new_animal = Dog()
#         else:
#             new_animal = None
#         if not self.front and new_animal:
#             self.front = new_animal
#             self.rear = self.front
#         elif new_animal:
#             self.rear.next = new_animal
#             self.rear = new_animal

#     def dequeue(self,pref):
#         value = None
#         if pref == "cat" or pref == "dog":
#             current = self.front
#             if str(current) == pref:
#                 value = str(current)
#                 self.front = self.front.next
#             else:
#                 previous = self.front
#                 current = previous
#                 while current:
#                     if str(current) == pref:
#                         dequeued = current
#                         value = str(dequeued)
#                         previous.next = dequeued.next
#                         break
#                     previous = current
#                     current = current.next
#                 return value
#         else:
#             return value

#     def __str__(self):
#         string = ""
#         current = self.front
#         if not current:
#             string = 'empty'
#         while current:
#             string += f"{str(current)}"
#             current = current.next
#             if current:
#                 string += " -> "
#         return string

if __name__ == "__main__":
    shelter = Animal_Shelter()
    shelter.enqueue("bird")
    print(shelter)
    shelter.enqueue("cat")
    print(shelter)
    shelter.enqueue("horse")
    print(shelter)
    shelter.enqueue("cat")
    print(shelter)
    shelter.enqueue("dog")
    print(shelter)
    shelter.enqueue("dog")
    print(shelter)
    shelter.enqueue("cat")
    print(shelter)
    shelter.enqueue("dog")
    print(shelter)
    shelter.enqueue("cat")
    print(shelter)
    print(shelter.dequeue("bird"))
    print(shelter)
    print(shelter.dequeue("cat"))
    print(shelter)
    print(shelter.dequeue("dog"))
    print(shelter)
    print(shelter.dequeue("dog"))
    print(shelter)
    print(shelter.dequeue("cat"))
    print(shelter)
