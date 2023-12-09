class stack():
    def __init__(self,limit):
        self.stack=[]
        self.limit=limit
    def peek(self):
        if (len(self.stack))<=0:
            return -1
        else:
          print(self.stack[len(self.stack)-1])
    def pop(self):
        if (len(self.stack))<=0:
            return False
        else:
            return self.stack.pop()
    def push (self,data):
        if (len(self.stack))>=self.limit:
            return False
        else:
            self.stack.append(data)
    def display(self):
        if (len(self.stack))<=0:
            return False
        else:
            for i in self.stack:
                print(i)
    def is_empty(self):
        if (len(self.stack))<=0:
            return True
        else : return False
    def reverse(lst):
        s = stack(100)
        for e in lst:
         s.push(e)
        for i in range(len(lst)):
         lst[i] = s.pop()
        return lst
    def rev_stacks(s):
        s1=stack(100)
        s2=stack(100)
        while not s.is_empty():
            s1.push(s.pop())
        while not s1.is_empty():
            s2.push(s1.pop())
        while not s2.is_empty():
            s.push(s2.pop())
    def postfix(lst):
        s=stack((len(lst))//2)
        for e in lst:
            if e =="*":
             t2=s.pop()
             t1=s.pop()
             t=t1*t2
             s.push(t)
            elif e =="/":
             t2=s.pop()
             t1=s.pop()
             t=t1/t2
             s.push(t)
            elif e =="-":
             t2=s.pop()
             t1=s.pop()
             t=t1-t2
             s.push(t)
            elif e=="+":
             t2=s.pop()
             t1=s.pop()
             t=t1+t2
             s.push(t)
            else:
                s.push(e)
                return s.stack[0]
        def match_s(str):
            s=stack()
            for i in str:
                if i in "([{":
                    s.push(i)
                elif i in ")]}":
                    if s.peek()==i:
                        s.pop()
                    else:
                        return False
            if s.is_empty():
                return True
            else:
                return False
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
