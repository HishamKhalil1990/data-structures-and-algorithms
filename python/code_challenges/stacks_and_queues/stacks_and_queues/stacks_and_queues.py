class EmptySatckException(Exception):
    def __init_(self):
        return "The Stack is empty"

class EmptyQueueException(Exception):
    def __init_(self):
        return "The Queue is empty"

class Node():
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def is_empty(self):
        if not self.top:
            return False
        return True

    def push(self,value):
        if not self.is_empty():
            self.top = Node(value)
        else:
            top_node = Node(value)
            top_node.next = self.top
            self.top = top_node

    def pop(self):
        if not self.is_empty():
            raise EmptySatckException
        else:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        if not self.is_empty():
            raise EmptySatckException
        else:
            return self.top.value

    def __str__(self):
        if not self.is_empty():
            raise EmptySatckException
        else:
            string = ""
            current = self.top
            while current != None:
                string += f"[{str(current.value)}]"
                current = current.next
                if current != None:
                    string += "->"
            return string

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
            self.front = Node(value)
            self.rear = self.front
        else:
            new_node = Node(value)
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
            raise EmptyQueueException
        else:
            string = ""
            current = self.front
            while current != None:
                string += str(current.value) + ' '
                current = current.next
            return string

if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    print(str(stack))
    stack.pop()
