class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):

        t = self.head
        if self.head==None:
            print("LIST KHALIST")
            return
        print(end="None<-->")
        while t:
            
            print(t.data , end="<--> ")
            t = t.next
        print(end="None")
        print()

    def addfirst(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = new_node
            new_node.prev = t

    def addafter(self, data, position):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            t = self.head
            for _ in range(position - 1):
                if t is None:
                    print("Invalid")
                    return
                t = t.next

            new_node.next = t.next
            new_node.prev = t
            if t.next:
                t.next.prev = new_node
            t.next = new_node

    def delfirst(self):
        if not self.head:
            print("List is empty")
            return
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data
    def deldata(self, data):
        if not self.head:
            print("List is empty")
            return

        t = self.head
        while t.next!=data:
            if t.data == data:
                if t.prev:
                    t.prev.next = t.next
                else:
                    self.head = t.next

                if t.next:
                    t.next.prev = t.prev

         #       print(f"Node {data} deleted ")
                return

            t = t.next

        #print(f"Node with {data} not found")

    def delend(self):
        if not self.head:
            print("List is empty")
            return
        t = self.head
        while t.next:
            t = t.next
        data = t.data
        if t.prev:
            t.prev.next = None
        else:
            self.head = None
        return data

    def delafter(self, position):
        if not self.head:
            print("List is empty")
            return
        t = self.head
        for _ in range(position):
            if t is None:
                print("Invalid position")
                return
            t = t.next

        data = t.data
        if t.prev:
            t.prev.next = t.next
        else:
            self.head = t.next

        if t.next:
            t.next.prev = t.prev

        return data
    def found(self):
     if not self.head or not self.head.next:
        print("List 2 ta data nadarad")
        return

     first_max = second_max = 0
     t = self.head

     while t.next!=None:
        if t.data > first_max:
            second_max, first_max = first_max, t.data
        elif  t.data > second_max:
            second_max = t.data

        t = t.next

     if second_max is None:
        print("peyda nashod")
     else:
        print("dovomin bozorgtar:", second_max)
        return second_max
     
alikazemi=DoublyLinkedList()
alikazemi.display()
alikazemi.addfirst(50)
alikazemi.addafter(150,1)
listt=DoublyLinkedList()
listt.addfirst(1)
listt.addend(76)
listt.addend(59)
listt.addend(31)
listt.addend(39)
listt.display()
listt.found()