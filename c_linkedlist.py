class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_in_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_after(self, data, target_data):
        new_node = Node(data)
        if not self.head:
            print("Target node not found. List is empty.")
            return

        t = self.head
        while t and t.data != target_data:
            t = t.next

        if not t:
            print("Target node not found.")
            return

        new_node.next = t.next
        t.next = new_node

    def add_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        t = self.head
        while t.next:
            t = t.next

        t.next = new_node

    def delete_node(self, m):
        if not self.head:
            print("List is empty. Cannot delete.")
            return

        if m == 0:
            self.head = self.head.next
            return

        t = self.head
        count = 0

        while t and count < m - 1:
            t = t.next
            count += 1

        if not t or not t.next:
            print("Node at position {} not found.".format(m))
            return

        t.next = t.next.next

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print()



listt = LinkedList()

listt.add_in_first(3)
listt.add_after(5, 3)
listt.add_end(7)

listt.display()

listt.delete_node(1)
listt.display()
