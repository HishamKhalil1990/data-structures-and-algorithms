class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return f"{node.data} is inserted"

    def includes(self,value):
        included = False
        current_node = self.head
        while current_node:
            if current_node.data == value:
                included = True
                break
            current_node = current_node.next
        return included

    def __str__(self):
        if self.head:
            stored_data = "{"f"{self.head.data}""} "
            current_node = self.head
            while current_node:
                current_node = current_node.next
                if current_node:
                    stored_data += "-> ""{"f"{current_node}""} "
                else:
                    stored_data += "-> Null"
        else:
            return "empty"
        return stored_data

# print(actual)
