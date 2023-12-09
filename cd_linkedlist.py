class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def add_in_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def add_after(self, data, target_data):
        new_node = Node(data)
        if not self.head:
            print("Target node not found. List is empty.")
            return

        t = self.head
        while t.data != target_data:
            t = t.next
            if t == self.head:
                print("Target node not found.")
                return

        new_node.next = t.next
        new_node.prev = t
        t.next.prev = new_node
        t.next = new_node

    def add_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node

    def delete_node(self, m):
        if not self.head:
            print("List is empty. Cannot delete.")
            return

        t = self.head
        count = 0

        while count < m:
            t = t.next
            count += 1
            if t == self.head:
                print("Node at position {} not found.".format(m))
                return

        t.prev.next = t.next
        t.next.prev = t.prev
        if t == self.head:
            self.head = t.next

    def display(self):
        if not self.head:
            print("The list is empty.")
            return

        t = self.head
        while True:
            print(t.data, end=" <-> ")
            t = t.next
            if t == self.head:
                break
        print()



cdlist = DoublyCircularLinkedList()

cdlist.add_in_first(3)
cdlist.add_after(5, 3)
cdlist.add_end(7)


cdlist.display()

cdlist.delete_node(2) 

cdlist.display()
