class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert_at_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_middle(self, data, position):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    print("Invalid position")
                    return
                current = current.next

            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def delete_at_front(self):
        if not self.head:
            print("List is empty")
            return
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        data = current.data
        if current.prev:
            current.prev.next = None
        else:
            self.head = None
        return data

    def delete_at_middle(self, position):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        for _ in range(position):
            if current is None:
                print("Invalid position")
                return
            current = current.next

        data = current.data
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev

        return data


# Example usage:
my_doubly_linked_list = DoublyLinkedList()
my_doubly_linked_list.insert_at_end(1)
my_doubly_linked_list.insert_at_end(2)
my_doubly_linked_list.insert_at_end(3)
my_doubly_linked_list.display()

my_doubly_linked_list.insert_at_front(0)
my_doubly_linked_list.display()

my_doubly_linked_list.insert_at_middle(100, 2)
my_doubly_linked_list.display()

my_doubly_linked_list.delete_at_end()
my_doubly_linked_list.display()

my_doubly_linked_list.delete_at_front()
my_doubly_linked_list.display()

my_doubly_linked_list.delete_at_middle(1)
my_doubly_linked_list.display()
