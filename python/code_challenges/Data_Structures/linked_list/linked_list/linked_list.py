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
            if type(self.head.data) == int:
                charr1 = "["
                charr2 = "]"
            else:
                charr1 = "{"
                charr2 = "}"
            stored_data = "head -> "f"{charr1}{self.head.data}{charr2} "
            current_node = self.head
            while current_node:
                current_node = current_node.next
                if current_node:
                    if type(current_node.data) == int:
                        charr1 = "["
                        charr2 = "]"
                    else:
                            charr1 = "{"
                            charr2 = "}"
                    stored_data += "-> "f"{charr1}{current_node}{charr2} "
                else:
                    stored_data += "-> X"
        else:
            return "empty"
        return stored_data

    def append(self,value):
        if self.head is not None:
            current = self.head
            while (current):
                if current.next == None:
                    current.next = Node(value)
                    break
                current = current.next
        else:
            self.head = Node(value)

    def insert_before(self,value,new_value):
        not_found = True
        current = self.head
        if current.data == value:
            new_node = Node(new_value)
            new_node.next = current
            self.head = new_node
            not_found = False
        else:
            while (current.next):
                if current.next.data == value:
                    new_node = Node(new_value)
                    new_node.next = current.next
                    current.next = new_node
                    not_found = False
                    break
                current = current.next
        if not_found:
            raise ValueError

    def insert_after(self,value,new_value):
        not_found = True
        current = self.head
        while (current):
            if current.data == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                not_found = False
                break
            current = current.next
        if not_found:
            raise ValueError

