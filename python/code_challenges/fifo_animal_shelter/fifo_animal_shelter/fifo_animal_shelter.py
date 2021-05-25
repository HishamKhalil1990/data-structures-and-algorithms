class Cat:
    def __init__(self,value = "cat"):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

class Dog:
    def __init__(self,value = "dog"):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

class Animal_Shelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,animal):
        if animal == "cat":
            new_animal = Cat()
        elif animal == "dog":
            new_animal = Dog()
        else:
            new_animal = None
        if not self.front and new_animal:
            self.front = new_animal
            self.rear = self.front
        elif new_animal:
            self.rear.next = new_animal
            self.rear = new_animal

    def dequeue(self,pref):
        value = None
        if pref == "cat" or pref == "dog":
            current = self.front
            if str(current) == pref:
                value = str(current)
                self.front = self.front.next
            else:
                previous = self.front
                current = previous
                while current:
                    if str(current) == pref:
                        dequeued = current
                        value = str(dequeued)
                        previous.next = dequeued.next
                        break
                    previous = current
                    current = current.next
            return value
        else:
            return value

    def __str__(self):
        string = ""
        current = self.front
        if not current:
            string = 'empty'
        while current:
            string += f"{str(current)}"
            current = current.next
            if current:
                string += " -> "
        return string

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
    shelter.enqueue("dog")
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
