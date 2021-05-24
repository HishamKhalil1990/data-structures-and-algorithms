from code_challenges.stacks_and_queues.stacks_and_queues.stacks_and_queues import Node,Stack

class Pseudo_Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,value):
        self.stack1.push(value)

    def dequeue(self):
        current = self.stack1.top
        while current:
            self.stack2.push(current.value)
            current = current.next
            self.stack1.pop()
            if current == None:
                break
        poped = self.stack2.pop()
        current = self.stack2.top
        while current:
            self.stack1.push(current.value)
            current = current.next
            self.stack2.pop()
            if current == None:
                break
        return poped

    def __str__(self):
        return str(self.stack1)

if __name__ == "__main__":
    pq = Pseudo_Queue()
    pq.enqueue(1)
    pq.enqueue(2)
    pq.enqueue(3)
    pq.enqueue(4)
    print(str(pq))
    pq.dequeue()
    pq.dequeue()
    print(str(pq))

