class node():
    def __init__(self,data):
        d=self.data
        self.next=None
class linkedList():
    def __init__(self):
        self.head=None

    def display(self):
        t=self.head
        while t!=None:
            print(t.data,end="-->")
            t=t.next
        print("None")
    def addin(self,data):
        n=node(data)
        n.next=self.head
        self.head=n
    def addinend(self,data):
        n=node(data)
        t=self.head
        if t==None:
            self.head=n
        else:
         while t.next:
            t=t.next
         t.next=n
    def midadd(self,data,m):
        n=node(data)
        t= self.head
        while t.data !=m:
            t=t.next
        n.next=t.next
        t.next=n
 
    def dellF(self):
        if self.head==None:return "None"
        else:self.head=self.head.next
    def dellL(self):
        t=self.head
        while t.next!=None:
           t= t.next
        t.next=None
    def dellM(self,m):
        t=self.head
        while t.data!=m:
            t=t.next
        t.next=t.next.next
    